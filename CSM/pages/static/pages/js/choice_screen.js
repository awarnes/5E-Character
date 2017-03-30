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
        evt.stopImmediatePropagation();

        var $sections = $('form section p').children();

        var $features = $('form .feature')

        var $feature_data = new Object();

        for (var k = 0; k < $features.length; k++) {
            var type = $($features[k]).children().children('.feature_type').children().val();
            var min = $($features[k]).children().children('.min_choices').children().val();
            var max = $($features[k]).children().children('.max_choices').children().val();
            var choices = $($features[k]).children().children('.feature_choice').children().val();
            var redirect = $($features[k]).children().children('.redirected_from').children().val();

            if (choices.length > Number(max)){
                var too_many_error = "Too many choices! Please select only " + max;
                var $error = $('<p>').text(too_many_error)
                $($features[k]).children('.panel-title').append($error)
                return
            } else if (choices.length < Number(min)){
                var too_few_error = "Too few choices! Please select at least " + min;
                var $error = $('<p>').text(too_few_error)
                $($features[k]).children('.panel-title').append($error)
                return
            }

            $feature_data[k.toString()] = [type, choices.toString(), redirect]


        }

        $.ajax({
            url: '/choice_set/',
            type: 'POST',
            json: true,
            data: $feature_data,
            success: function(resp){
                window.location.href= '/' + resp + '/'
            },
            error: function(err){
                alert(err);
            },

        });


    })


});