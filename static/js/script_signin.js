$("span.clear").onclick = function () {
    inputs = this.getAttribute("data-id").split(", ");
    inputs.forEach((element) => {
        clear_input(element)
    });
    $("#" + inputs[0]).focus();
}
$(".hide").onclick = function () {
    toggle_vis($("#" + this.getAttribute("data-id")), this, $(".unhide"), true);
}
$(".unhide").onclick = function () {
    toggle_vis($("#" + this.getAttribute("data-id")), this, $(".hide"), false);
}
