$(document).ready(function(){
    "use strict";

    $.get('/user/characters/specific_one/', {query_char: current_char}, function(data){

        var features = data[0].features;

        $.each($('[data-skill]'), function(skill){
            $(this).data('skill')
        })

        })

    $('#tabs').tabs();




})