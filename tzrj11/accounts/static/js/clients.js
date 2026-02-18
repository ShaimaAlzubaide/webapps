window.onload = function () {
    var currentUrl = window.location.pathname.split("/").pop();
    var links = document.querySelectorAll(".link");
    var clientTypes = document.querySelectorAll(".type-item");

    links.forEach(function (link) {
        if (link.getAttribute("href") === currentUrl) {
            link.classList.add("active");
        }
    });

    clientTypes.forEach(function (type) {
        var linkHref = type.querySelector('a').getAttribute("href");
        if (linkHref === currentUrl) {
            type.classList.add("activates");
        }
    });
};
