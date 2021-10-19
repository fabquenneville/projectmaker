
function refresh_event_listeners() {
    /*
    Attach actions to various tags.

    Args:

    Returns:
    */
    document.querySelectorAll('.classname').forEach(tag => {
        tag.onkeyup = (event) => {
            if (event.keyCode !== 13) {
                console.log(tag);
            }
        };
    });

    document.querySelectorAll('#tagid').forEach(tag => {
        tag.onchange = (event) => {
            console.log(tag);
        };
    });
}

function load_data() {
    /*
    Trigger a UI reload of the data in the localstorage. If none exists fetch fresh data first.

    Args:

    Returns:
    */
    if (!localStorage.getItem('data')) {
        get_data(function () {
            load_show_data();
        });
    } else {
        load_show_data();
    }
}

function load_show_data() {
    /*
    Load the data in the localstorage to the UI

    Args:

    Returns:
    */
    let data = JSON.parse(localStorage.getItem('data'));
    let container = document.getElementById("show_data_container");
    if (!container) return false;
    container.innerHTML = "";

    for (let [key, value] of Object.entries(data)) {
        let div = build({
            type: "div",
            classes: ["lmarg", "tmarg", "bordered", "padded"],
            id: "data_" + value.id
        });

        container.append(div);

        // Title
        let titlediv = build({
            type: "div",
            classes: ["split_title_div_just", ]
        });
        div.append(titlediv);
        titlediv.append(build({
            type: "span",
            classes: ["uline", "mousehand"],
            click: function () { console.log(value); },
            innerhtml: '<i class="fas fa-check"></i> '
        }));

        let titleh = build({
            type: "h3",
            innerhtml: ucFirst(value.formal)
        });
        if (value.favicon) {
            titleh.innerHTML = value.favicon.html + " " + ucFirst(value.formal);
        }
        titlediv.append(titleh);

        // list
        let listdiv = build({
            type: "div",
            classes: ["lmarg", "grid2"]
        });
        div.append(listdiv);

        for (let [k, v] of Object.entries(value)) {
            if (isNaN(k) && !(v == null)) {
                listdiv.append(build({
                    type: "span",
                    innerhtml: ucFirst(k).replace("_", " ") + ": "
                }));

                let itemspan = build({
                    type: "span",
                    classes: ["wwrap", ],
                    innerhtml: v
                });
                if (k == "favicon") {
                    itemspan.innerHTML = v.html;
                }
                listdiv.append(itemspan);
            }
        }
    }
}

function get_page_data(callback) {
    changeCursor("wait");
    let request = new XMLHttpRequest();
    request.open("POST", "api");
    // Add data to send with request
    const data = new FormData();
    data.append('action', "get_page_data");

    // Send request
    request.send(data);
    request.onload = () => {

        // Extract JSON data from request
        const data = JSON.parse(request.responseText);

        // Update the result div
        if (data.success) {
            localStorage.clear();
            store_api_response(data);
            callback();
            changeCursor();
        } else {
            changeCursor("not-allowed");
            setTimeout(() => { changeCursor(); }, 3000);
        }
    };
}

function get_data(callback) {
    changeCursor("wait");
    let request = new XMLHttpRequest();
    request.open("POST", "api");
    // Add data to send with request
    const data = new FormData();
    data.append('action', "get_data");

    // Send request
    request.send(data);
    request.onload = () => {

        // Extract JSON data from request
        const data = JSON.parse(request.responseText);

        // Update the result div
        if (data.success) {
            localStorage.clear();
            store_api_response(data);
            callback();
            changeCursor();
        } else {
            changeCursor("not-allowed");
            setTimeout(() => { changeCursor(); }, 3000);
        }
    };
}

function store_api_response(data) {
    if ('data' in data) {
        localStorage.setItem('data', JSON.stringify(data.data));
    }
}

function initPage() {
    get_page_data(function () {
        if (localStorage.getItem('data')) load_data();
        refresh_event_listeners();
    });
}

if (document.readyState !== 'loading') {
    initPage();
} else {
    document.addEventListener('DOMContentLoaded', function () {
        initPage();
    });
}