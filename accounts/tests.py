from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Products
from categories.models import Category
from django.urls import reverse

class LoginTest(TestCase):

    def test_login_page_loads(self):
        response = self.client.get("/signin/")
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        User.objects.create_user(
            username="rahulrameshm0",
            password="724850"
        )

        response = self.client.post("/signin/",
                                {"username":"rahulrameshm0",
                                "password":"724850"}
                                    )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)


    def test_login_with_invalid_password(self):
        User.objects.create_user(
            username = "testuser",
            password = "testpassword"
        )

        response = self.client.post(
            "/signin/",
            {"username": "testuser", "password":"wrongpassword"}
        )

        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_with_nonexistent_username(self):

        response = self.client.post(
            "/signin/",
            {
                "username": "nonexisting",
                "password": "testpassword",
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_empty_username_valid_password(self):
        response = self.client.post(
            "/signin/",
            {
                "username":"",
                "password": "testpassword"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_empty_password(self):

        User.objects.create_user(
            username="testusername",
            password="testpassword"
        )

        response = self.client.post(
            '/signin/',
            {
                "username": "testusername",
                "passowrd": ""
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        


class RegisterTest(TestCase):

    def test_register_page_loads(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200) 

    def test_user_registration_working(self):
        response = self.client.post(

            "/register/",
            {
                "username": "testusername",
                "email": "test@gmail.com",
                "password": "testpassword",
                "confirm_password": "testpassword",
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username="testusername").exists())
    
    def test_duplicate_user(self):

        User.objects.create_user(
            username="testusername",
            email="test@gmail.com",
            password="testpassword"
        )

        response = self.client.post(

            "/register/",
            {
                "username": "testusername",
                "email": "test@gmail.com",
                "password": "testpassword",
                "confirm_password": "testpassword",
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="testusername").exists())
    
    def test_registration_with_valid_email(self):

        response = self.client.post(
        '/register/',
        {
            "username":"testusername",
            "email":"test@gmail.com",
            "password":"testpassword",
            "confirm_password":"testpassword",
            }
        )

        self.assertEqual(response.status_code, 302)

    def test_registration_with_invalid_email(self):
        response = self.client.post(
            '/register/',
            {
                "username":"testusername",
                "email":"not-email",
                "password":"testpassword",
                "confirm_password":"testpassword",
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
        User.objects.filter(username="testusername").exists()
    )

    def test_registration_empty_username(self):
        response = self.client.post(
            '/register/',
            {
                "username":"",
                "email":"test@gmail.com",
                "password":"testpassword",
                "confirm_password":"testpassword",
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            User.objects.filter(username="testusername").exists()
        )

    def test_registration_empty_password(self):
        response = self.client.post(
            '/register/',
            {
                "username":"testusername",
                "email":"test@gmail.com",
                "password":"",
                "confirm_password":"testpassword",
            }
        )

        self.assertEqual(response.status_code, 302)

    def test_registration_empty_cofirm_password(self):
        response = self.client.post(
            '/register/',
            {
                "username":"testusername",
                "email":"test@gmail.com",
                "password":"testpassword",
                "confirm_password":"",
            }
        )
        self.assertEqual(response.status_code, 302)

class EmailVarificationTest(TestCase):
    def test_email_varification_page_loads(self):
        response = self.client.get("/email_varification/")
        self.assertEqual(response.status_code, 200)

class PasswordResetTest(TestCase):
    def test_password_reset_page_loads(self):
        response = self.client.get("/password_reset_sent/")
        self.assertEqual(response.status_code, 200)

