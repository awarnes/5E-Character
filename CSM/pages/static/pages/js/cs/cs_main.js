$(document).ready(function(){
    "use strict";

    $('#tabs').tabs();

    $('#spells').tabs();

    $('.search_query').on('click', function (evt){

        var $query = $(this).data('slug');

        var re = /\s/g;

        var $type = $(this).data('type').toLowerCase();

        $type = $type.replace(re, '_');

        $('#output').modal('toggle');

        const $equipment = ['weapons', 'armors', 'items', 'tools'];

        if ($type === 'spells') {
            $.get('/api/v1/spells/spell/'+$query, function (data){
                $('#name').text(data.name);
                $('#name').data('type', $type);
                $('#name').data('slug', $query);
                $('#description').text(data.description);
                $('#output').find($('div.modal-footer')).append($spell_ready);
            })
        }   else if ($equipment.indexOf($type) != -1) {
            $.get('/api/v1/equipment/' + $type + '/' + $query, function (data){
                $('#name').text(data.name);
                $('#name').data('type', $type);
                $('#name').data('slug', $query);
                $('#description').text(data.description);
            })
        }  else {
            $.get('/api/v1/rules/' + $type + '/' + $query, function (data){
                $('#name').text(data.name);
                $('#name').data('type', $type);
                $('#name').data('slug', $query);
                $('#description').text(data.description);
            })
        }


    });

    $('#open_details').on('click', function(evt){
            var $type = $('#name').data('type');
            var $slug = $('#name').data('slug')
            window.location.href='/' + $type + '/details/' + $slug + '/'

    });

    $('#add_point').on('click', function(evt){
        var $cur = $('#id_current_points');
        var $max = $('#id_max_points');

        var next = Number($cur.val()) + 1;

        if (next <= Number($max.val())){
            $cur.val(next);
        }
    });

    $('#sub_point').on('click', function(evt){
        var $cur = $('#id_current_points');

        var next = Number($cur.val()) - 1;

        if (next >= 0){
            $cur.val(next);
        }
    });

    $('#add_hp').on('click', function(evt){
        var $cur = $('#id_cur_hp');
        var $max = $('#id_max_hp');

        var next = Number($cur.val()) + 1;

        if (next <= Number($max.val())){
            $cur.val(next);
            $('#death_saves').prop('hidden', true);
        }

    });

    $('#sub_hp').on('click', function(evt){
        var $cur = $('#id_cur_hp');

        var next = Number($cur.val()) - 1;

        if ($('#id_temp_hp').val() == 0){
            if (next >= 0){
            $cur.val(next);
            }
            if (next <= 0) {
                $('#death_saves').prop('hidden', false);
            }
        } else if ($('#id_temp_hp').val() > 0){
            $('#id_temp_hp').val((Number($('#id_temp_hp').val())-1));
        }

    });

    $('#add_temp_hp').on('click', function(evt){
        var $cur = $('#id_temp_hp');

        var next = Number($cur.val()) + 1;

        $cur.val(next);

    });

    $('#sub_temp_hp').on('click', function(evt){
        var $cur = $('#id_temp_hp');

        var next = Number($cur.val()) - 1;

        if (next >= 0){
            $cur.val(next);
        }
    });

    $('#add_death_succ').on('click', function(evt){
        var $id = $('#death_saves');

        var $saves = $id.data('succs');
        var $fails = $id.data('fails');

        $saves = $saves + 1;

        if ($saves >= 3){
            $('#death_saves').prop('hidden', true);
            $('#id_cur_hp').val(1);
            $.each($('[data-succ]'), function(){
                $(this).hide();
            });
            $.each($('[data-fail]'), function(){
                $(this).hide();
            });
            $id.data('succs', 0);
            $id.data('fails', 0);
        } else {
            var $succs = $('[data-succ]');

            $.each($succs, function(){
                if ($(this).data('succ') <= $saves){
                    $(this).show()
                }
            })
            $id.data('succs', $saves);
        }

    });

    $('#add_death_fail').on('click', function(){
        var $id = $('#death_saves');

        var $fails = $id.data('fails');

        $fails = $fails + 1;

        if ($fails >= 3){
            $.each($('[data-fail]'), function(){
                $(this).hide();
            });
            $.each($('[data-succ]'), function(){
                $(this).hide();
            });
            $id.data('succs', 0);
            $id.data('fails', 0);
            $('#death_saves').prop('hidden', true);
            alert('You have died!');
        } else {
            var $fail_els = $('[data-fail]');

            $.each($fail_els, function(){
                if ($(this).data('fail') <= $fails){
                    $(this).show()
                }
            })
            $id.data('fails', $fails);
        }

    });

    $('#sub_death_fail').on('click', function(){
        var $id = $('#death_saves');

        var $fails = $id.data('fails');

        $fails = $fails - 1;

        if ($fails > 0){
            var $fail_els = $('[data-fail]');

            $.each($fail_els, function(){
                if ($(this).data('fail') <= $fails){
                    $(this).hide()
                }
            });
            $id.data('fails', $fails);

        } else if ($fails == 0){
            var $fail_els = $('[data-fail]');

            $.each($fail_els, function(){
                $(this).hide();
            });
            $id.data('fails', 0);
        }
    });

    $('#sub_death_succ').on('click', function(){
        var $id = $('#death_saves');

        var $succs = $id.data('succs');

        $succs = $succs - 1;

        if ($succs > 0){
            var $succ_els = $('[data-succ]');

            $.each($succ_els, function(){
                if ($(this).data('succ') <= $succs){
                    $(this).hide()
                }
            });
            $id.data('succs', $succs);

        } else if ($succs == 0){
            var $succ_els = $('[data-succ]');

            $.each($succ_els, function(){
                $(this).hide();
            });
            $id.data('succs', 0);
        }
    });

    $('.search_type').on('click', function (evt){

        var $type_data = $(this).attr('data-type');

        var queries = document.getElementsByClassName('search_query');

        for (var i=0; i<queries.length; i++){
            if (queries[i].dataset.search_type === $type_data) {
                $(queries[i]).slideToggle();
            }
        }
    });

    $('#save').on('click', function(){
        var $inputs = $('#battle_tab :input');

        $.each($inputs, function(){
            $(this).prop('disabled', false);
        });

        $('#battle_tab').submit();
    });

    $('#no_save').on('click', function(evt){
        $('#delete_check').modal('toggle');
    });

    $('#delete_yes').on('click', function(){
    });

    $('#delete_no').on('click', function(){
        $('#delete_check').modal('toggle');
    });

    $.fn.spellNotReady = function (){
        alert('That spell is not ready!');
    }

    $.fn.spellReady =  function (){

            var spell_level = $(this).parent().parent().data('level');
            var $spell_input = $('#id_spell_slots_'+spell_level+'_current');
            if ((Number($spell_input.val()) - 1) < 0){
                alert("You don't have enough slots left to cast " + $(this).next().text() + "!");
            } else {
                $spell_input.val(Number($spell_input.val())-1);
            }

    }
    $('.cast_spell_ready').on('click', $.fn.spellReady);
    $('.cast_spell_notready').on('click', $.fn.spellNotReady)

    $('#short_rest').on('click', function(){
        var $hit_dice = $('#id_hit_dice_current');
        var $hp_cur = $('#id_cur_hp');
        var $hp_max = $('#id_max_hp');
        $('#rest').modal('toggle');
        $('#rest #name').text('Short Rest');
        $('#rest #desc_title').text('Roll Hit Dice:');
        $('#rest #description').text('You can roll as many hit dice as you have to regain health. After a long rest you' +
            ' regain a number equal to half your level (minimum 1).');
        $('#rest #description').append($('<br>'));
        var $short_button = $('<button>').text('Roll Die!').on('click', function(){
            if ($hit_dice.val() > 0){
                var $roll = $('<p>').text(Math.floor(Math.random() * 6) + 1 + (char_CON_bonus));
                $hit_dice.val(Number($hit_dice.val())-1);
                if (Number($roll.text()) + Number($hp_cur.val()) >= Number($hp_max.val())){
                    $hp_cur.val($hp_max.val());
                    $('#rest #description').append("Nice, you're at full health!");
                } else {
                    $hp_cur.val(Number($roll.text()) + Number($hp_cur.val()));
                    $('#rest #description').append('You regained ' + $roll.text() + ' hit points!');
                }
            } else {
                var $sorry = $('<p>').text("Sorry, you don't have enough hit dice left!");
                $('#rest #description').append($sorry);
            }
        });

        $('#rest #description').append($short_button);

    });

    $('#long_rest').on('click', function(){

        $('#rest').modal('toggle');
        $('#rest #name').text('Long Rest');
        $('#rest #desc_title').text('');
        $('#rest #description').text('You rest for a minimum of eight hours, during which you do not stand watch for' +
            ' more than two hours, or spend one or more hours engaged in strenuous activity such as Spell casting, walking' +
            ' or fighting. At the end of the long rest you gain the following benefits:');

        var $list = $('<ul>');
        var $li_1 = $('<li>').text('You regain all hit points.').appendTo($list);
        var $li_2 = $('<li>').text('You regain all spent spell slots.').appendTo($list);
        var $li_3 = $('<li>').text('You regain all used ability uses.').appendTo($list);
        var $li_4 = $('<li>').text('You regain hit dice equal to half your level (minimum 1).').appendTo($list);

        $('#rest #description').append($('<br>')).append($list);

        $('#id_hit_dice_current').val(Number($('#id_hit_dice_current').val()) + (Math.floor(char_level/2) + 1));

        $('#id_cur_hp').val($('#id_max_hp').val());

        $('#id_current_points').val($('#id_max_points').val());

        for (var i=0;i<10;i++){
            $('#id_spell_slots_'+i+'_current').val($('#id_spell_slots_'+i+'_maximum').val())
        }
    });

    $('#level_up').on('click', function(){

        if ((Number($('#id_char_level').val()) + 1) > 20){
            alert('Sorry, level 20 is the highest!')
        } else {
            $('#id_char_level').val(Number($('#id_char_level').val()) + 1);

            var $inputs = $('#battle_tab :input');

            $.each($inputs, function(){
                $(this).prop('disabled', false);
            });

            $('#battle_tab').submit();
        }


    })
});