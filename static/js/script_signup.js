$A("span.clear").forEach(function (element) {
    element.onclick = function () {
        inputs = this.getAttribute("data-id").split(", ");
        inputs.forEach((element) => {
            clear_input(element)
        });
        $("#" + inputs[0]).focus();
    }
})
$A(".hide").forEach((element) => {
    element.onclick = function () {
        toggle_vis($("#" + this.getAttribute("data-id")), this, this.previousElementSibling, true);
    }
})
$A(".unhide").forEach((element) => {
    element.onclick = function () {
        toggle_vis($("#" + this.getAttribute("data-id")), this, this.nextElementSibling, false);
    }
})
