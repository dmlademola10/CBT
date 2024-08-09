window.addEventListener("load", () => {
    $("#add_exam").addEventListener("click", () => {
        $("#message").style.display = "none";
        open_box("#" + $("#add_exam").getAttribute("data-id"));
    });
    $A(".background>div").forEach((elem) => {
        elem.addEventListener("click", (event) => {
            event.stopImmediatePropagation();
        });
    })
    $(".floating_msg").addEventListener("click", () => {
        close_msg();
    });
    $(".background").addEventListener("click", () => {
        $(".background").style.display = "none";
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
    $A(".edit").forEach((elem) => {
        elem.addEventListener("click", () => {
            elem.classList.remove("fa-pencil");
            elem.classList.add("fa-spinner");
            elem.classList.add("fa-spin-pulse");
            get_exam(elem.parentElement.getAttribute("data-id"), elem);
        });
    });
    $A(".del").forEach((elem) => {
        elem.addEventListener("click", () => {
            elem.classList.remove("fa-trash-can");
            elem.classList.add("fa-spinner");
            elem.classList.add("fa-spin-pulse");
            if (confirm("Are you sure you want to delete this exam? \n" + elem.parentElement.outerText + "\nThis action can't be undone!")) {
                del_exam(elem.parentElement.getAttribute("data-id"), elem);
            }
        });
    });
    $forms("new_exam", "label").addEventListener("input", () => {
        $("#message").style.display = "none";
        $("#message").innerHTML = "";
    });
    $forms("new_exam", "course").addEventListener("change", function () {
        $("#message").style.display = "none";
        $("#message").innerHTML = "";
    });
    $forms("edit_exam", "edit_label").addEventListener("input", () => {
        $("#edit_message").style.display = "none";
        $("#edit_message").innerHTML = "";
    });
    $forms("edit_exam", "edit_course").addEventListener("change", function () {
        $("#edit_message").style.display = "none";
        $("#edit_message").innerHTML = "";
    });
    $forms("new_exam").addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData($forms("new_exam"));

        if (window.XMLHttpRequest) {
            var xmlhttp = new XMLHttpRequest();
        } else {
            var xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }

        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                const response = JSON.parse(xmlhttp.responseText);
                if (response.result == true) {
                    $("#message").classList.add("success");
                    $("#message").classList.remove("failure");
                    $forms("new_exam").reset();
                } else {
                    $("#message").classList.add("failure");
                    $("#message").classList.remove("success");
                }
                $("#message").style.display = "block";
                $("#message").innerHTML = response.message;
            }
        }

        xmlhttp.onerror = function () {
            $("#message").classList.add("failure");
            $("#message").classList.remove("success");
            $("#message").innerHTML = response.message;
            // console.error(xmlhttp.statusText);
        };

        xmlhttp.open("POST", "/exams/fetch/create/", true);
        xmlhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xmlhttp.send(formData);
    });

    $forms("edit_exam").addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData($forms("edit_exam"));

        if (window.XMLHttpRequest) {
            var xmlhttp = new XMLHttpRequest();
        } else {
            var xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }

        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                const response = JSON.parse(xmlhttp.responseText);
                if (response.result == true) {
                    $("#edit_message").classList.add("success");
                    $("#edit_message").classList.remove("failure");
                } else {
                    $("#edit_message").classList.add("failure");
                    $("#edit_message").classList.remove("success");
                }
                $("#edit_message").style.display = "block";
                $("#edit_message").innerHTML = response.message;
            }
        }

        xmlhttp.onerror = function () {
            $("#edit_message").classList.add("failure");
            $("#edit_message").classList.remove("success");
            $("#edit_message").innerHTML = response.message;
        };

        xmlhttp.open("POST", "/exams/fetch/edit/", true);
        xmlhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xmlhttp.send(formData);
    });

    window.setInterval(() => {
        if (window.XMLHttpRequest) {
            var xmlhttp = new XMLHttpRequest();
        } else {
            var xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }

        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                const response = JSON.parse(xmlhttp.responseText);
                if (response.result == true) {
                    $(".exams").innerHTML = "";
                    items = JSON.parse(response.message);
                    if (items.length < 1) {
                        h1 = document.createElement("h1");
                        text_ = document.createTextNode("No exam found!")
                        h1.appendChild(text_);
                        $(".exams").appendChild(h1);
                    }
                    items.forEach((item) => {
                        div = document.createElement("div");
                        div.classList.add("exam");
                        for_ = document.createAttribute("data-id");
                        div.attributes.setNamedItem(for_);
                        div.setAttribute("data-id", item.id);
                        text_ = document.createTextNode(item.label);
                        div.appendChild(text_);

                        span = document.createElement("span");
                        span.classList.add("fa");
                        span.classList.add("fa-trash-can");
                        span.classList.add("icon");
                        span.classList.add("del");
                        title_ = document.createAttribute("title");
                        span.attributes.setNamedItem(title_);
                        span.setAttribute("title", "Delete");
                        div.appendChild(span);

                        span = document.createElement("span");
                        span.classList.add("fa");
                        span.classList.add("fa-pencil");
                        span.classList.add("icon");
                        span.classList.add("edit");
                        title_ = document.createAttribute("title");
                        span.attributes.setNamedItem(title_);
                        span.setAttribute("title", "Edit");
                        div.appendChild(span);

                        $(".exams").appendChild(div);
                    });
                    $A(".edit").forEach((elem) => {
                        elem.addEventListener("click", () => {
                            elem.classList.remove("fa-pencil");
                            elem.classList.add("fa-spinner");
                            elem.classList.add("fa-spin-pulse");
                            get_exam(elem.parentElement.getAttribute("data-id"), elem);
                        });
                    });
                    $A(".del").forEach((elem) => {
                        elem.addEventListener("click", () => {
                            elem.classList.remove("fa-trash-can");
                            elem.classList.add("fa-spinner");
                            elem.classList.add("fa-spin-pulse");
                            if (confirm("Are you sure you want to delete this exam? \n" + elem.parentElement.outerText + "\nThis action can't be undone!")) {
                                del_exam(elem.parentElement.getAttribute("data-id"), elem);
                            }
                        });
                    });
                } else {
                    msg("<span class='fa fa-triangle-exclamation'></span> " + response.message);
                }
            }
        }

        xmlhttp.onerror = function () {
            msg("<span class='fa fa-link-slash'></span> You are offline!");
            // console.error(xmlhttp.statusText);
        };

        xmlhttp.open("GET", "/exams/fetch/refresh/", true);
        xmlhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xmlhttp.send();
    }, 3000);
});

function get_exam(id, icon) {
    if (window.XMLHttpRequest) {
        var xmlhttp = new XMLHttpRequest();
    } else {
        var xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            const response = JSON.parse(xmlhttp.responseText);
            if (response.result == true) {
                var inputs = JSON.parse(response.message);
                $forms("edit_exam", "id").value = id;
                $forms("edit_exam", "edit_label").value = inputs.label;
                $A("select[name=edit_course] optgroup option").forEach((opt) => {
                    if (opt.getAttribute("selected") != null) {
                        opt.attributes.removeNamedItem("selected");
                    }
                    if (opt.value == inputs.course) {
                        var sel = document.createAttribute("selected");
                        opt.attributes.setNamedItem(sel);
                    }
                });
                $("#edit_message").style.display = "none";
                open_box("#edit_exam_box")
            } else {
                msg("<span class='fa fa-triangle-exclamation'></span> " + response.message);
            }
            icon.classList.add("fa-pencil");
            icon.classList.remove("fa-spinner");
            icon.classList.remove("fa-spin-pulse");
        }
    }

    xmlhttp.onerror = function () {
        msg("<span class='fa fa-link-slash'></span> You are offline!");
        // console.error(xmlhttp.statusText);
    };

    xmlhttp.open("GET", "/exams/fetch/get/" + id, true);
    xmlhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xmlhttp.send();
}

function open_box(child) {
    $A(".background>div").forEach((elem) => {
        elem.style.display = "none";
    })
    $(child).style.display = "flex";
    $(".background").style.display = "flex";
}

function del_exam(id, icon) {
    if (window.XMLHttpRequest) {
        var xmlhttp = new XMLHttpRequest();
    } else {
        var xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            const response = JSON.parse(xmlhttp.responseText);
            if (response.result == true) {
                msg("<span class='fa fa-check'></span> " + response.message);
            } else {
                msg("<span class='fa fa-triangle-exclamation'></span> " + response.message);
            }
            icon.classList.add("fa-pencil");
            icon.classList.remove("fa-spinner");
            icon.classList.remove("fa-spin-pulse");
        }
    }

    xmlhttp.onerror = function () {
        msg("<span class='fa fa-link-slash'></span> You are offline!");
        // console.error(xmlhttp.statusText);
    };

    xmlhttp.open("GET", "/exams/fetch/delete/" + id, true);
    xmlhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xmlhttp.send();
}


// disable submit button on ajax forms until response has been received from server or an error occurs
