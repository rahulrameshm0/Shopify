from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
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


    def test_login_with_invalid_password(self):
        User.objects.create_user(
            username = "testuser",
            password = "testpassword"
        )

        response = self.client.post(
            "signin",
            {"username": "rahulrameshm0", "password":"wrongpassword"}
        )

        self.assertFalse(response.wsgi_request.user.is_authenticated)

class RegisterTest(TestCase):
    def test_register_page_loads(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200) 

class EmailVarificationTest(TestCase):
    def test_email_varification_page_loads(self):
        response = self.client.get("/email_varification/")
        self.assertEqual(response.status_code, 200)
        
class PasswordResetTest(TestCase):
    def test_password_reset_page_loads(self):
        response = self.client.get("/password_reset_sent/")
        self.assertEqual(response.status_code, 200)