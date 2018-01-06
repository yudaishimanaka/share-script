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
                console.log(response)
            },
            error: function(response){
                console.log("application error")
            }
        })
    })
})