/**
 * Created by alexanderwarnes on 3/20/17.
 */

"use strict";

$(document).ready(function(){

    $('.draggable').draggable({
        revert: true,

    });



    $('.droppable').droppable({
        drop: function (event, ui) {
            $(this).val(ui.draggable.text());
        },
        accept: ".draggable"
    });


});