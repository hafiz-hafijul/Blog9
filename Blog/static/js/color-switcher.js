(function($) {

    "use strict";


    /*------------------------------------------------------------------
                Switcher
    -------------------------------------------------------------------*/

    $("#default-color").on('click', function() {
        jQuery("#color").attr("href", "css/theme-colors/default-color.css");
        return false;
    });

    $("#red").on('click', function() {
        jQuery("#color").attr("href", "css/theme-colors/red.css");
        return false;
    });

    $("#purple").on('click', function() {
        jQuery("#color").attr("href", "css/theme-colors/purple.css");
        return false;
    });

    $("#green").on('click', function() {
        jQuery("#color").attr("href", "css/theme-colors/green-brown.css");
        return false;
    });

    $("#yellow").on('click', function() {
        jQuery("#color").attr("href", "css/theme-colors/yellow.css");
        return false;
    });

    $(".picker_close").on('click', function() {
        jQuery("#choose_color").toggleClass("position");
    });

    $(".layout_two").on('click', function() {
        jQuery("#boxed").addClass("boxed_size");
    });

    $(".layout_one").on('click', function() {
        jQuery("#boxed").removeClass("boxed_size");
    });

})(window.jQuery);