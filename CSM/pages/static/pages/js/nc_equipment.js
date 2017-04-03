// TODO: Make the js to pull information from each selected element and put it into the panel on the right.

$(document).ready(function() {
    "use strict";

    var $selected_weapons = new Array();
    var $selected_armor = new Array();
    var $selected_items = new Array();
    var $selected_tools = new Array();

    var $query;

    $('#weapons select').on('change', function (){

        $.each($(this).val(), function(){
            if ($selected_weapons.indexOf(this) === -1) {
                $query = $('option[value="' + this + '"]').text().toLowerCase();
            } else {
                $query = '';
            }
        });
        $selected_weapons = $(this).val();

        var re = /\s/
        $query = $query.replace(re, '-');

        $.get('/api/v1/equipment/weapons/' + $query + '/', function(weapon){

            $('#name').html(weapon.name + '<br>' + '<i>' + weapon.weapon_type + ' ' + weapon.melee_or_ranged + '</i>');
            $('#description').text(weapon.description);

            $('#information').empty();

            $('<p>').text('Damage: ' + weapon.damage_dice_number + 'd' + weapon.damage_dice_size).appendTo($('#information'));

            $('<p>').text('Properties: ').appendTo($('#information'));
            $.each(weapon.properties, function(){
                $('<p>').text(this.name + ' - ' + this.description).appendTo($('#information'));
            })


        })
    });

    $('#armor select').on('change', function (){

        $.each($(this).val(), function(){
            if ($selected_armor.indexOf(this) === -1) {
                $query = $('option[value="' + this + '"]').text().toLowerCase();
            } else {
                $query = '';
            }
        });
        $selected_armor = $(this).val();

        var re = /\s/
        $query = $query.replace(re, '-');

        $.get('/api/v1/equipment/armors/' + $query + '/', function(armor){

            $('#name').html(armor.name);
            $('#description').text(armor.description);

            $('#information').empty();

            $('<p>').text('Base AC: ' + armor.base_armor_class).appendTo($('#information'));

            $('<p>').text('Dexterity Bonus: ' + armor.dexterity_modifier).appendTo($('#information'));
            $('<p>').text('Bonus AC: ' + armor.bonus_armor_class).appendTo($('#information'));
            $('<p>').text('Stealth Disadvantage: ' + armor.stealth_disadvantage).appendTo($('#information'));

            if (armor.don_time.indexOf('action') === -1){
                if (armor.don_time > 1) {
                    var $time = 'minutes';
                } else {
                    var $time = 'minute';
                }
            } else {
                var $time = ''
            }


            $('<p>').text('Don Time: ' + armor.don_time + ' ' + $time).appendTo($('#information'));
            $('<p>').text('Doff Time: ' + armor.doff_time + ' ' + $time).appendTo($('#information'));




        })
    });

    $('#items select').on('change', function (){

        $.each($(this).val(), function(){
            if ($selected_items.indexOf(this) === -1) {
                $query = $('option[value="' + this + '"]').text().toLowerCase();
            } else {
                $query = '';
            }
        });
        $selected_items = $(this).val();

        var re = /\s/g;
        $query = $query.replace(re, '-');
        re = /’/g;
        $query = $query.replace(re, "");
        re = /[\(\)]/g;
        $query = $query.replace(re, '')

        $.get('/api/v1/equipment/items/' + $query + '/', function(item){

            $('#name').html(item.name + '<br>' + '<i>' + item.item_type + '</i>');
            $('#description').text(item.description);

            $('#information').empty();
        })
    });

    $('#tools select').on('change', function (){

        $.each($(this).val(), function(){
            if ($selected_tools.indexOf(this) === -1) {
                $query = $('option[value="' + this + '"]').text().toLowerCase();
            } else {
                $query = '';
            }
        });
        $selected_tools = $(this).val();

        var re = /\s/g;
        $query = $query.replace(re, '-');
        re = /’/g;
        $query = $query.replace(re, "");
        re = /[\(\)]/g;
        $query = $query.replace(re, '')


        $.get('/api/v1/equipment/tools/' + $query + '/', function(tool){

            $('#name').html(tool.name + '<br>' + '<i>' + tool.tool_type + '</i>');
            $('#description').text(tool.description);

            $('#information').empty();

            // $('<p>').text('Damage: ' + weapon.damage_dice_number + 'd' + weapon.damage_dice_size).appendTo($('#information'));
            //
            // $('<p>').text('Properties: ').appendTo($('#information'));
            // $.each(weapon.properties, function(){
            //     $('<p>').text(this.name + ' - ' + this.description).appendTo($('#information'));
            // })


        })
    })



});