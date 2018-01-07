$(function(){
    $("#auth").click(function(){
        $.ajax({
            type: 'POST',
            url: '/auth',
            data: JSON.stringify({"email":$("#email").val(),
                                  "password":$("#password").val()
                                }),
            contentType: 'application/json',
            success: function(response){
                if(response[0] == 1){
                    $("#email").val("");
                    $("#password").val("");
                    window.location = response[1]
                }else{
                    Materialize.toast(response[1], 5000, 'red rounded')
                }
            },
            error: function(response){
                console.log("application error")
            }
        })
    })
})