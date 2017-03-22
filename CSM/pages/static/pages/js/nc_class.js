$(document).ready(function(){

    var $class = $('#id_klass');

    var $cleric = $('#cleric');
    var $sorcerer = $('#sorcerer');
    var $warlock = $('#warlock');

    $cleric.hide();
    $sorcerer.hide();
    $warlock.hide();


    $class.on('change', function(){

        $cleric.hide();
        $sorcerer.hide();
        $warlock.hide();
        $('#prestige_features').empty();
        $('#prestige_name').empty();

        var $class_query = $('#id_klass option:selected').text().toLowerCase();

        if ($class_query === 'cleric'){
            $cleric.toggle('display');
        } else if ($class_query === 'sorcerer') {
            $sorcerer.toggle('display');
        } else if ($class_query === 'warlock') {
            $warlock.toggle('display');
        }
        if ($(this).val() !== '') {
            $('#class_features').empty();

            $.get('/api/v1/rules/classes/' + $class_query, function (data) {
                $('#class_name').text(data.name);

                for (var i = 0; i < data.features.length; i++) {
                    var $feature = $('<li>', {text: data.features[i].name});
                    $('#class_features').append($feature);
                }
            });
        }
    });

    $cleric.on('change', function(){

        var $prestige_query = $('#id_cleric_prestige option:selected').text().toLowerCase();
        var re = /\s/
        $prestige_query = $prestige_query.replace(re, '-');

        if ($prestige_query !== '') {
            $('#prestige_features').empty();

            $.get('/api/v1/rules/prestige_classes/' + $prestige_query, function (data) {
                $('#prestige_name').text(data.name);

                for (var i = 0; i < data.features.length; i++) {
                    var $feature = $('<li>', {text: data.features[i].name});
                    $('#prestige_features').append($feature);
                }
            });
        }
    });

    $sorcerer.on('change', function(){

        var $prestige_query = $('#id_sorcerer_prestige option:selected').text().toLowerCase();
        var re = /\s/
        $prestige_query = $prestige_query.replace(re, '-');

        if ($prestige_query !== '') {
            $('#prestige_features').empty();

            $.get('/api/v1/rules/prestige_classes/' + $prestige_query, function (data) {
                $('#prestige_name').text(data.name);

                for (var i = 0; i < data.features.length; i++) {
                    var $feature = $('<li>', {text: data.features[i].name});
                    $('#prestige_features').append($feature);
                }
            });
        }
    });

    $warlock.on('change', function(){

        var $prestige_query = $('#id_warlock_prestige option:selected').text().toLowerCase();
        var re = /\s/
        $prestige_query = $prestige_query.replace(re, '-');

        if ($prestige_query !== '') {
            $('#prestige_features').empty();

            $.get('/api/v1/rules/prestige_classes/' + $prestige_query, function (data) {
                $('#prestige_name').text(data.name);

                for (var i = 0; i < data.features.length; i++) {
                    var $feature = $('<li>', {text: data.features[i].name});
                    $('#prestige_features').append($feature);
                }
            });
        }
    });





});