// Javascript Show/Hide toggle button for password field

let password = document.getElementById('password');
let eyeIcon = document.getElementById('eye-icon');

eyeIcon.onclick = function(){
    if(password.type === "password"){
        password.type = "text";
        eyeIcon.src = eyeOpensrc;
    }else {
        password.type = "password";
        eyeIcon.src = eyeClosedsrc;
    }
}
