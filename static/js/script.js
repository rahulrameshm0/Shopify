// Javascript Show/Hide toggle button for password field

let password = document.getElementById('password');
let confirmPassword = document.getElementById('confirm-password');
let eyeIcon = document.getElementById('eye-icon');
let eyeIconConfirm = document.getElementById('eye-icon-2');

eyeIcon.onclick = function(){
    if(password.type === "password"){
        password.type = "text";
        eyeIcon.src = eyeOpensrc;

    } else {
        password.type = "password";
        eyeIcon.src = eyeClosedsrc;
    }
}

eyeIconConfirm.onclick = function(){
    if(confirmPassword.type === "password"){
        confirmPassword.type = "text";
        eyeIconConfirm.src = eyeOpensrc;
    }else {
        confirmPassword.type = "password";
        eyeIconConfirm.src = eyeClosedsrc;
    }
}

//sidebar toggle
function toggleSidebar() {
        document.getElementById('sidebar').classList.toggle('open');
        document.getElementById('mainContent').classList.toggle('shifted');
    }


// checkout section

     const options = {
            key: "{{ razorpay_key_id }}",

            amount: "{{ amount }}",

            currency: "{{ currency }}",

            name: "Your Store",

            description: "Order #{{ order.id }}",

            order_id: "{{ razorpay_order_id }}",

            handler: function (response) {

                console.log("Payment successful");

                console.log(response);

            },

            theme: {
                color: "#3399cc"
            }
        };

        const razorpay = new Razorpay(options);

        document.getElementById("pay-button").onclick = function(e) {
            razorpay.open();
            e.preventDefault();
        };