window.addEventListener("load", () => {
    document.body.addEventListener("click", function () {
        if ($(".sidebar").style.width != "0px") {
            $(".sidebar").style.width = "0px";
            $(".sidebar").style.borderRight = "0";
            $(".open_menu").style.display = "unset";
            $(".close_menu").style.display = "none";
        }
    });
    $(".open_menu").addEventListener("click", function (event) {
        event.stopImmediatePropagation();
        $(".sidebar").style.width = "200px";
        $(".sidebar").style.borderRight = "1px solid whitesmoke";
        $(".open_menu").style.display = "none";
        $(".close_menu").style.display = "unset";
    });
    $(".sidebar").addEventListener("click", function (event) {
        event.stopImmediatePropagation();
        $(".open_menu").style.display = "none";
        $(".close_menu").style.display = "unset";
    });
    $A(".sidelink").forEach((elem) => {
        elem.addEventListener("click", () => {
            window.location.assign(elem.getAttribute("data-for"));
        });
    })
});
