$(document).ready ( function(){

    // clicking starting test button
    $("#start_test").click(function() {
        var url = $("#form_number").attr("data-form-url");

        $.ajax({
            url: url,
            data: {
            },
            success: function(data){
                $("#quiz_form").html(data);
                $('#start_test').hide();
                $('#id_explain').hide();
            }
        });
    });

    function atLeastOneRadio() {
        return ($('#submit_form input[type=radio]:checked').size > 0);
    }

    $(document).on('click', '#next_question', function() {
        if (atLeastOneRadio() == true) {
            $('#error').hide();
            $('#next_question').removeClass('disabled');
        }
        else { 
            $('#next_question').addClass('disabled');
            $('#error').show();
        }
    });

    // function to get cookie - need to send crsftoken
    function getCookie(name) {

        var matches = document.cookie.match(new RegExp(
          "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
        ))
        return matches ? decodeURIComponent(matches[1]) : undefined
    };

    // function to post send answer on any question
    $(document).on('submit', '#submit_form', function(e) {
        e.preventDefault();

        $('#error').html('');

        var url = $("#submit_form").attr("data-form-url");

        $.ajax({
            url : url,
            type : "POST",
            data : {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                answer: $("#submit_form input[type='radio']:checked").val()
            },
            success : function(data) {
                $('#quiz_form').html(data);
            }
        });
        return false;
    });

    // submiting client form
    $(document).on('submit', '#submit_user_form', function(e) {
        e.preventDefault();

        var url = $("#submit_user_form").attr("data-form-url");

        $.ajax({
            url : url,
            type : "POST",
            data : {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                surname: $("#id_Surname_cl").val(),
                name: $('#id_Name_cl').val(),
                secondName: $('#id_Po_batk_cl').val(),
                passportSerial: $('#id_Seria_passport').val(),
                passportNumber: $('#id_Nomer_passport').val()
            },
            success : function(data) {
                $('#quiz_form').html(data);
            }
        });
        return false;
    });
});