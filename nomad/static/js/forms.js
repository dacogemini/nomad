function sendData(e) {
    e.preventDefault(); // don not refresh the page

    var form_data = {
        name: $('input[name="name"]').val(),
        ... other field values ...
    }

    $.ajax({
        url: "{% url 'https://mail.google.com/mail/u/0/?pli=1#inbox' %}",
        method: "POST",
        data: form_data,
        success: function(response) {
            // here are the success data in the response
            // you can redirect the user or anything else
            //window.location.replace("{% url 'success-url' %}");
        },
        error: function(response) {
            // here are the errors which you can append to .error-block
            //$('.error-block').html(response);
        }
    })

}
