window.addEventListener("load", () => {
    $("#create").addEventListener("click", () => {
        $("#message").style.display = "none";
        open_box("#" + $("#create").getAttribute("data-id"));
    });
    $A("span.clear").forEach((elem) => {
        elem.addEventListener("click", () => {
            inputs = elem.getAttribute("data-id").split(", ");
            inputs.forEach((element) => {
                clear_input(element)
            });
            $("#" + inputs[0]).focus();
        })
    });
    $A(".background>div").forEach((elem) => {
        elem.addEventListener("click", (event) => {
            event.stopImmediatePropagation();
        });
    });
    $A(".edit").forEach((elem) => {
        elem.addEventListener("click", () => {
            elem.classList.remove("fa-pencil");
            elem.classList.add("fa-spinner");
            elem.classList.add("fa-spin-pulse");

            const headers = new Headers();
            headers.set("X-Requested-With", "XMLHttpRequest");
            const options = {
                headers: headers,
            }
            const req = new Request("/faculties/fetch/get/" + elem.parentElement.getAttribute("data-id"), options);
            fetch(req, { method: "GET" }).then(res => {
                if (!res.ok) {
                    msg("<span class= 'fa fa-link-slash'></span> You are offline!");
                }
                return res.json();
            }).then(response => {
                if (response.result == true) {
                    const inputs = JSON.parse(response.message);
                    $forms("edit_faculty", "id").value = elem.parentElement.getAttribute("data-id");
                    $forms("edit_faculty", "edit_name").value = inputs.name;
                    $("#edit_message").style.display = "none";
                    open_box("#edit_faculty_box")
                } else {
                    msg("<span class='fa fa-triangle-exclamation'></span> " + response.message);
                }
            }, reason => {
                msg("<span class='fa fa-link-slash'></span> An error occured!");
                console.error(reason);
            }).then(() => {
                elem.classList.add("fa-pencil");
                elem.classList.remove("fa-spinner");
                elem.classList.remove("fa-spin-pulse");
            });
        });
    });
    $(".floating_msg").addEventListener("click", () => {
        close_msg();
    });
    $(".background").addEventListener("click", () => {
        $(".background").style.display = "none";
    });
    $forms("new_faculty", "name").addEventListener("input", () => {
        $("#message").style.display = "none";
        $("#message").innerHTML = "";
    });
    $forms("new_faculty").addEventListener("submit", function (event) {
        event.preventDefault();
        const formData = new FormData($forms("new_faculty"));
        const headers = new Headers();
        headers.set("X-Requested-With", "XMLHttpRequest");
        const options = {
            headers: headers,
        }
        const req = new Request("/faculties/fetch/create/", options);
        fetch(req, { method: "POST", body: formData }).then(res => {
            if (!res.ok) {
                $("#message").classList.add("failure");
                $("#message").classList.remove("success");
                $("#message").innerHTML = "An error occured!";
                msg(response.message);
            }
            return res.json();
        }).then(response => {
            if (response.result == true) {
                $("#message").classList.add("success");
                $("#message").classList.remove("failure");
                $forms("new_faculty").reset();
            } else {
                $("#message").classList.add("failure");
                $("#message").classList.remove("success");
            }
            $("#message").style.display = "block";
            $("#message").innerHTML = response.message;
        }, reason => {
            msg("<span class='fa fa-triangle-exclamation'></span> An error occurred while contacting the server!");
            console.error(reason);
        });
    })
    $forms("edit_faculty").addEventListener("submit", function (event) {
        event.preventDefault();
        const formData = new FormData($forms("edit_faculty"));
        const headers = new Headers();
        headers.set("X-Requested-With", "XMLHttpRequest");
        const options = {
            headers: headers,
        }
        const req = new Request("/faculties/fetch/edit/", options);
        fetch(req, { method: "POST", body: formData }).then(res => {
            if (!res.ok) {
                $("#edit_message").classList.add("failure");
                $("#edit_message").classList.remove("success");
                $("#edit_message").innerHTML = "An error occured!";
                msg(response.message);
            }
            return res.json();
        }).then(response => {
            if (response.result == true) {
                $("#edit_message").classList.add("success");
                $("#edit_message").classList.remove("failure");
                $forms("new_faculty").reset();
            } else {
                $("#edit_message").classList.add("failure");
                $("#edit_message").classList.remove("success");
            }
            $("#edit_message").style.display = "block";
            $("#edit_message").innerHTML = response.message;
        }, reason => {
            msg("<span class='fa fa-triangle-exclamation'></span> An error occurred while contacting the server!");
            console.error(reason);
        });
    })
});

function open_box(child) {
    $A(".background>div").forEach((elem) => {
        elem.style.display = "none";
    })
    $(child).style.display = "flex";
    $(".background").style.display = "flex";
}
