$(document).ready(function() {
    $(".background").css("height", $(window).height() + "px");
    fadeInHeader();
    $("#panel1").css("height", $(window).height() + "px");
    linkSmoothScroll();
});


function fadeInHeader() {
    $("#overlay").css("display", "none");
    $("#main-title").css("display","none");
    $("#small").css("display", "none");
    $("#big").css("display", "none");
    $("#greeter").css("display", "none");
    $("header").css("display", "none");
    setTimeout(function() {
        $("#overlay").fadeIn(300);
    }, 700);
    setTimeout(function() {
        $("#main-title").fadeIn(300);
        $("#big").fadeIn(2000);
        $("#small").fadeIn(2000);
        $("#greeter").fadeIn(2000);
        $("header").fadeIn(2000);
    }, 2000);
    setTimeout(function() {
      $('#bouncing-arrow').show(500);
  }, 3500);
}

function linkSmoothScroll() {
    $("a[href^='#']").click(function(event) {
        event.preventDefault();
        $('html, body').animate({
          scrollTop: $($.attr(this, 'href')).offset().top
        }, 1000);
    });
}

// Credit for the function below comes from:
// http://www.webdesignerdepot.com/2014/05/how-to-create-an-animated-sticky-header-with-css3-and-jquery/
$(window).scroll(function() {
    if ($(this).scrollTop() > 1){
        $('header').addClass("sticky");
        $('#logo').addClass("sticky");
    }
    else {
        $('header').removeClass("sticky");
        $('#logo').removeClass("sticky");
    }
});