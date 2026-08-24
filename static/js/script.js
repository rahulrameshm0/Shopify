// Javascript Show/Hide toggle button for password field

let password = document.getElementById('password');
let confirmPassword = document.getElementById('confirm-password');
let eyeIcon = document.getElementById('eye-icon');
let eyeIconConfirm = document.getElementById('eye-icon-2');

// const razorpay = new Razorpay(options);

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