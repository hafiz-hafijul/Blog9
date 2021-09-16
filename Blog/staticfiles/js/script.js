(function($) {

    "use strict";

    $('.nav li.dropdown').hover(function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeIn(500);
    }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeOut(500);
    });

    //Submenu Dropdown Toggle
    if ($('.nav li.dropdown .dropdown-menu').length) {
        //Dropdown Button
        $('.nav li.dropdown .dropdown-menu.dropdown-2').on('click', function() {
            $(this).prev('ul').slideToggle(500);
        });

        //Disable dropdown parent link
        $('.nav li.dropdown .dropdown-menu.dropdown-2 > a').on('click', function(e) {
            e.preventDefault();
        });
    }



    //Submenu Dropdown Toggle
    if ($('.header-menu li.dropdown ul').length) {
        $('.header-menu li.dropdown').append('<div class="dropdown-btn"><span class="fa fa-angle-down"></span></div>');

        //Dropdown Button
        $('.header-menu li.dropdown .dropdown-btn').on('click', function() {
            $(this).prev('ul').slideToggle(500);
        });

        //Disable dropdown parent link
        $('.header-menu .navigation li.dropdown > a,.hidden-bar .side-menu li.dropdown > a').on('click', function(e) {
            e.preventDefault();
        });
    }



    /*
     * ----------------------------------------------------------------------------------------
     *  PRELOADER JS
     * ----------------------------------------------------------------------------------------
     */

    function handlePreloader() {
        if ($('.preloader').length) {
            $('.preloader').delay(200).fadeOut(500);
        }
    }

    var prealoaderOption = $(window);
    prealoaderOption.on("load", function() {
        var preloader = jQuery('.spinner');
        var preloaderArea = jQuery('.preloader-area');
        preloader.fadeOut();
        preloaderArea.delay(350).fadeOut('slow');
    });


    //Custom Seclect Box
    if ($('.custom-select-box').length) {
        $('.custom-select-box').selectmenu().selectmenu('menuWidget').addClass('overflow');
    }


    //Sponsors Carousel
    if ($('.sponsors-carousel').length) {
        $('.sponsors-carousel').owlCarousel({
            loop: true,
            margin: 30,
            nav: false,
            smartSpeed: 700,
            autoplay: 4000,
            navText: ['<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>'],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                800: {
                    items: 3
                },
                1200: {
                    items: 5
                }
            }
        });
    }

    //Sponsors Carousel
    if ($('.sub-post').length) {
        $('.sub-post').owlCarousel({
            loop: true,
            margin: 30,
            nav: false,
            smartSpeed: 700,
            autoplay: 4000,
            navText: ['<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>'],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                800: {
                    items: 3
                },
                1200: {
                    items: 4
                }
            }
        });
    }






    /* ==========================================================================
       When document is loading, do
       ========================================================================== */

    $(window).on('load', function() {
        handlePreloader();
    });


    /* ==========================================================================
              pagination
              ========================================================================== */


    $(function() {
        var obj = $('#pagination').twbsPagination({
            totalPages: 10,
            visiblePages: 3,
            onPageClick: function(event, page) {
                console.info(page);
            }
        });
    });



    $(document).ready(function() {
        function buttonUp() {
            var valux = $('.ExpInput').val();
            valux = $.trim(valux).length;
            if (valux !== 0) {
                $('.Expbtn').css('z-index', '99');
            } else {
                $('.ExpInput').val('');
                $('.Expbtn').css('z-index', '-999');
            }
        }
    });

    $(document).ready(function() {
        var submitIcon = $('.ExpIcon');
        var submitInput = $('.ExpInput');
        var searchBox = $('.Exp-serach');
        var isOpen = false;

        $(document).mouseup(function() {
            if (isOpen == true) {
                submitInput.val('');
                $('.Expbtn').css('z-index', '-999');
                submitIcon.click();
            }
        });

        submitIcon.mouseup(function() {
            return false;
        });

        searchBox.mouseup(function() {
            return false;
        });

        submitIcon.click(function() {
            if (isOpen == false) {
                searchBox.addClass('Exp-serach-open');
                isOpen = true;
            } else {
                searchBox.removeClass('Exp-serach-open');
                isOpen = false;
            }
        });

    });


    function callback(event) {
        // Provided by the core
        var element = event.target; // DOM element, in this example .owl-carousel
        var name = event.type; // Name of the event, in this example dragged
        var namespace = event.namespace; // Namespace of the event, in this example owl.carousel
        var items = event.item.count; // Number of items
        var item = event.item.index; // Position of the current item
        // Provided by the navigation plugin
        var pages = event.page.count; // Number of pages
        var page = event.page.index; // Position of the current page
        var size = event.page.size; // Number of items per page
    }
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 0,
        dots: false,
        responsive: {
            0: {
                items: 2
            },
            600: {
                items: 3
            },
            1000: {
                items: 6
            }
        }
    })

    $('.sub-post').owlCarousel({
        loop: true,
        margin: 0,
        dots: false,
        nav: true,
        responsive: {
            0: {
                items: 2
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    })

    /*
    =======================================
      venobox video and image pop-up 
    =======================================
    */

    $(document).ready(function() {
        $('.venobox').venobox();
    });


    $("#firstlink").venobox().trigger('click');


    $('.venobox_custom').venobox({
        framewidth: '500px', // default: ''
        frameheight: '400px', // default: ''
        border: '5px', // default: '0'
        bgcolor: '#5dff5e', // default: '#fff'
        titleattr: 'data-title', // default: 'title'
        numeratio: true, // default: false
        infinigall: true // default: false
    });


    /*------------------------------------------------------------------
     Validate
     -------------------------------------------------------------------*/

    $("#submit").on("click", function() {
        var errors = "";

        var contact_name = document.getElementById("contact_name");
        var contact_email_address = document.getElementById("contact_email");

        if (contact_name.value == "") {
            errors += 'Please provide your name.';
        } else if (contact_email_address.value == "") {
            errors += 'Please provide an email address.';
        } else if (contact_email_address.value == "") {
            errors += 'Please provide a valid email address.';
        }


        if (errors) {
            document.getElementById("error").style.display = "block";
            document.getElementById("error").innerHTML = errors;
            return false;
        } else {

            $.ajax({
                type: "POST",
                url: 'process.php',
                data: $("#contact_form").serialize(),
                success: function(msg) {
                    if (msg == 'success') {
                        document.getElementById("error").style.display = "none";
                        document.getElementById("contact_name").value = "";
                        document.getElementById("contact_email").value = "";
                        document.getElementById("message").value = "";
                        $("#contact_form").hide();
                        document.getElementById("success").style.display = "block";
                        document.getElementById("success").innerHTML = "Thank You! We'll contact you shortly.";
                    } else {
                        document.getElementById("error").style.display = "block";
                        document.getElementById("error").innerHTML = "Oops! Something went wrong while prceeding.";
                    }
                }

            });

        }
    });

})(window.jQuery);