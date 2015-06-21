// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

Backbone._sync = Backbone.sync;
Backbone.sync = function(method, model, options) {
    if (method != 'get') {
        var csrfToken = getCookie('csrftoken');
        options.beforeSend = function(xhr){
            xhr.setRequestHeader('X-CSRFToken', csrfToken);
        };
    }
    return Backbone._sync(method, model, options);
};
