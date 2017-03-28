/**
 * Created by alexanderwarnes on 3/20/17.
 */

"use strict";

$(document).ready(function(){

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('#submit_button').on('click', function(evt){
        evt.preventDefault();

        var $sections = $('form section p').children();

        var types = new Array();
        var results = new Array();


        for (var i=0; i<$sections.length/2;i++){
            types.push($('#id_form-'+i+'-feature_type').val());
            results.push($('#id_form-'+i+'-feature_choices').val());

            $.post('/choice_set/', {types: types, results: results}, function(data){

                "Post the data to an end point, possibly a totally different function, also need to" +
                "get the redirect information to decide where to redirect next." +
                "will also need to make sure that the min_choices and max_choices are respected (validation)"

                alert(data)
            })
        }

    })


});