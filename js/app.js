$(window).scroll(function () {
    var scroll = $(window).scrollTop();

    if (scroll >= 50) {
        $("header").css({
            'background': '#fff',
        });
        $('nav a').addClass('scrolling');
    } else {
        $("header").css({
            'background': '#000',
        });
        $("nav a").removeClass("scrolling");
    }
});
$(document).ready(function(){
    var img_url = 'https://udemy-images.udemy.com/course/750x422/391546_3a97_3.jpg'
  $('.slides').css({
    'background-image': 'url("'+img_url+'")',
  });
});