/**
 * Created by alexanderwarnes on 3/21/17.
 */


$(document).ready(function(){

    var subraces = {'1': ['1', '2'], '2': ['3', '4', '5'], '3': ['6', '7'], '4': ['8', '11'], '5': ['11'],
                    '6': ['9', '10'], '7': ['11'], '8': ['11'], '9': ['11']};

    var $subrace = $('#id_subrace');
    var $race = $('#id_race');

    $subrace.attr('disabled', true);
    $('#id_subrace>option').each(function(){
        $(this).attr('disabled', true)
    });

    $race.on('change', function(){
        var $race_query = $('#id_race option:selected').text();

        $subrace.val('')

        if ($(this).val() !== ''){
            $.get('/api/v1/rules/races/' + $race_query.toLowerCase(), function(data){
                $('#race_name').empty();
                $('#race_abilities').empty();
                $('#race_features').empty();

                $('#race_name').text(data.name)
                var $ability_1 = $('<p>', {text: data.ability_score_1 + ' +' + data.ability_score_1_bonus});
                $('#race_abilities').append($ability_1)
                if (data.ability_score_2 !== 'None'){
                    var $ability_2 = $('<p>', {text: data.ability_score_2 + ' +' + data.ability_score_2_bonus});
                    $('#race_abilities').append($ability_2)
                }

                for (var i=0; i<data.features.length; i++) {
                    var $feature = $('<li>', {text: data.features[i].name});
                    $('#race_features').append($feature);
                }

            })
            $subrace.attr('disabled', false);
            var $race_val = $race.val();
            $('#id_subrace>option').each(function(){
                if (subraces[$race_val].indexOf($(this).val()) >= 0){
                    $(this).attr('disabled', false);
                } else {
                    $(this).attr('disabled', true);
                }
            })

        } else {
            $subrace.attr('disabled', true);
        }

    });

    $subrace.on('change', function(){
        if ($(this).val() !== ''){
            var $subrace_query = $('#id_subrace option:selected').text();

            var re = /\s/

            $subrace_query = $subrace_query.replace(re, '-').toLowerCase()

            $.get('/api/v1/rules/subraces/'+ $subrace_query, function(data){
                $('#subrace_name').empty();
                $('#subrace_abilities').empty();
                $('#subrace_features').empty();

                $('#subrace_name').text(data.name)
                var $ability_1 = $('<p>', {text: data.ability_score_1 + ' +' + data.ability_score_1_bonus});
                $('#subrace_abilities').append($ability_1)
                if (data.ability_score_2 !== 'None'){
                    var $ability_2 = $('<p>', {text: data.ability_score_2 + ' +' + data.ability_score_2_bonus});
                    $('#race_abilities').append($ability_2)
                }

                for (var i=0; i<data.features.length; i++) {
                    var $feature = $('<li>', {text: data.features[i].name});
                    $('#subrace_features').append($feature);
                }
            })
        }
    })

    // $(".ct option[value='x']").each(function(){
    //     $(this).remove();
    // })

});

