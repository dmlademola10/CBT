function $(selector) {
    return document.querySelector(selector);
}
function $A(selectors) {
    return document.querySelectorAll(selectors);
}
function $forms(form, elem) {
    if (elem) {
        return document.forms[form][elem];
    }
    return document.forms[form];
}
function clear_input(element) {
    $("#" + element).value = "";
    $("#" + element).focus();
}
function toggle_vis(psw, icon1, icon2, hide) {
    if (hide == true) {
        psw.type = "password";
    } else {
        psw.type = "text";
    }
    icon1.style.display = "none";
    icon2.style.display = "block";
    psw.focus();
}
function msg(message) {
    if (typeof hide != 'undefined') {
        clearTimeout(hide);
    }
    $(".floating_msg").style.display = "block";
    $(".floating_msg").innerHTML = message;
    hide = setTimeout(() => {
        $(".floating_msg").style.display = "none";
    }, 5000);
}
function close_msg() {
    clearTimeout(hide);
    $(".floating_msg").style.display = "none";
}
