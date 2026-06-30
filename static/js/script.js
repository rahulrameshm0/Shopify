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

//popup
window.onload = function() {
    const popup = document.getElementById('popup');
    if (popup) {
        popup.style.display = 'flex';  // ← this shows the popup
    }
}
