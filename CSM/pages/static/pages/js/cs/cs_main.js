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

    $('.cast_spell_notready').on('click', function(evt){
        alert('That spell is not ready!');
    });

    $('.cast_spell_ready').on('click', function(){
        var spell_level = $(this).parent().parent().data('level');
        var $spell_input = $('#id_spell_slots_'+spell_level+'_current');
        if (($spell_input - 1) < 0){
            alert("You don't have enough slots left to cast " + $(this).next().text() + "!");
        } else {
            $spell_input.val(Number($spell_input.val())-1);
        }
    })

});