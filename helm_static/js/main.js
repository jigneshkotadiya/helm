$(document).ready(function(){

    window.setTimeout(function() {
        $(".alert").fadeTo(500, 0).slideUp(500, function(){
            $(this).remove(); 
        });
    }, 2000);

    // $(".alert").delay(200).addClass("in").fadeOut(3500);

});

