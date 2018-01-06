$(function(){
    $("#register").click(function(){
        $.ajax({
            type: 'POST',
            url: '/create_user',
            data: JSON.stringify({"user_name":$("#user_name").val(),
                                  "email":$("#email").val(),
                                  "password":$("#password").val()
                                }),
            contentType: 'application/json',
            success: function(response){
                console.log(response)
                var color;
                if(response[0] == 1){
                    color = "green";
                    $("#user_name").val("");
                    $("#email").val("");
                    $("#password").val("");
                }else{
                    color = "red";
                }
                Materialize.toast(response[1], 5000, color + ' rounded')
            },
            error: function(response){
                console.log("application error")
            }
        })
    })
});
$(document).ready(function(){
    // the "href" attribute of the modal trigger must specify the modal ID that wants to be triggered
    $('.modal').modal();
});