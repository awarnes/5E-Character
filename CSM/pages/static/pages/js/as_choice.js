/**
 * Created by alexanderwarnes on 3/20/17.
 */

$(document).ready(function(){

    $('#tabs').tabs();

    $('.score').draggable({
        containment: '#containment-wrapper',

    });



    $('.droppable').droppable({
        drop: function (event, ui) {
            $(this).val(ui.draggable.data('score'));
        },
        accept: ".score"
    });


    $('#ability_buy .droppable').droppable({
        drop: function (event, ui) {

            if ($(this).val() === ui.draggable.data('score')){

            } else {

                if ($(this).val() !== ''){
                    var points = Number($('#points_left').text());
                    var cost = Number($("[data-buy='" + $(this).val() + "']").data('cost'));
                    $('#points_left').text(points + cost);
                }

                $(this).val(ui.draggable.data('score'));
                var points = Number($('#points_left').text());
                var cost = Number($("[data-buy='" + $(this).val() + "']").data('cost'));

                if (points - cost < 0) {
                    alert('Not enough points left for that!');
                    $(this).val('');
                    $('#points_left').text(0);
                } else {
                    $('#points_left').text(points - cost);
                }

            }
        },
        accept: ".score"
    });

    // $('#choice_next').on('click', function(evt){
    //     var empty_keys = Array();
    //     var $scores = {
    //         'STR': $('.droppable:eq(0)').value,
    //         'DEX': $('.droppable:eq(1)').data('score'),
    //         'CON': $('.droppable:eq(2)').data('score'),
    //         'INT': $('.droppable:eq(3)').data('score'),
    //         'WIS': $('.droppable:eq(4)').data('score'),
    //         'CHA': $('.droppable:eq(5)').data('score')
    //     }
    //
    //     $.each($scores, function(key, value){
    //
    //         if (typeof(value) === 'undefined'){
    //
    //             empty_keys.push(key);
    //         }
    //     })
    //
    //     if (empty_keys.length > 0){
    //         $.each(empty_keys, function(key, value){
    //             alert('Please choose a ' + value + ' score!');
    //         })
    //     } else {
    //         $.post('/cc_check/', {'scores': $scores})
    //     }
    //
    // })

    $('#roll').on('click', function(evt){
        evt.preventDefault();

        for (var i=1; i<7; i++){
            var die_1 = Math.floor((Math.random() * 6) + 1);
            var die_2 = Math.floor((Math.random() * 6) + 1);
            var die_3 = Math.floor((Math.random() * 6) + 1);
            var die_4 = Math.floor((Math.random() * 6) + 1);

            var min = Math.min(die_1, die_2, die_3, die_4);

            var total = (die_1 + die_2 + die_3 + die_4) - min;

            $('[data-roll='+i+']').data('roll', total);
            $('[data-roll='+i+']').data('score', total);
            $('[data-roll='+i+']').text(total);
        }

    })

    $('#ability_buy #id_Strength').val('').on('change', function() {
        var points = Number($('#points_left').text());
        var cost = Number($("[data-buy='" + $('#ability_buy #id_Strength').val() + "']").data('cost'))
        $('#points_left').text(points - cost);

    });




});