/**
 * Created by alexanderwarnes on 3/20/17.
 */

$(document).ready(function(){

    $('#tabs').tabs();

    $('.score').draggable({
        containment: '#containment-wrapper',
        // helper: function (event) {
        //     var ctrl = $(this);
        //     var val = ctrl.data('score');
        // },

    });

    $('.droppable').droppable({
        drop: function (event, ui) {
            $(this).val(ui.draggable.data('score'));
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

});