$(window).scroll(function() {
    var scroll = $(window).scrollTop();

    if (scroll >= $(window).height()) {
        $("header").css({
            'background': 'rgba(255,255,255,.2)',
        });
        $('nav a').addClass('scrolling');
    }
    else {
        $("header").css({
            'background': 'rgba(0,0,0,.6)',
        });
        $("nav a").removeClass("scrolling");
    }
});

$(document).ready(function() {
    var img_url = [
        'data:image/jpeg;base64,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',
        'data:image/jpeg;base64,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',
        'data:image/jpeg;base64,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',
        'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTk_idx9nWJ2ip_s_wdiOdYqAcB2gFxuCpyak5HWBKU2psvnteS'
    ]

    $('.slides img').attr('src', img_url[0]);

    for (var i in img_url) {
        $('.clickable').append('<img src="' + img_url[i] + '" data-num="' + i + '">');
    }

    function loop(index = 1) {
        $('.controls').off('click').on('click', function(event) {
            if ($(this).attr('id') == 'prev') {
                var current = $('.slides img').attr('data-num');
                if(current == 0){
                    index = img_url.length - 1;
                } else {
                    index =  +current - 1;
                }
            }
            else if ($(this).attr('id') == 'next') {
                var current = $('.slides img').attr('data-num');
                if (current == img_url.length - 1){
                    index = 0;
                } else {
                    index = +current + 1;
                }
            }
            $('.slides img').attr({
                'src': img_url[index],
                'data-num': index,
            });
        });
        $('.clickable img').click(function() {
            index = $(this).attr('data-num');
            $('.slides img').attr({
                'src': img_url[index],
                'data-num': index,
            });
        });

        function anim() {
            $('.slides img').attr({
                'src': img_url[index],
                'data-num': index,
            });
            index++;
            if (index > img_url.length - 1) {
                index = 0;
            }
            loop(index);
        }
        setTimeout(anim, 3000);
    }
    loop();
});