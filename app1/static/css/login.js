$(document).ready(function () {
    $(".login").animate({
        width:"300px",
        top:"50%"
    },2000)
    $(".login").animate({
        height:"60%"
    },2000 , function(){

        $("h1").animate({
            opacity:"1",
        },function(){
            $("input").animate({
            opacity:"1",
            } , ()=>{
                $("button").animate({
                    opacity:"1"
                },()=>{
                    $(".forgrt").animate({
                        opacity:"1"
                    })
                })
            })
        })
    })

   


});

