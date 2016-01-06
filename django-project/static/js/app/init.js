(function($) {
  $(function() {

    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $('.post-body img').each(function() {
      var $ths = $(this);
      if ($ths.css('float') === 'left') {
        $ths.addClass('fleft-padding');
      } else if ($ths.css('float') === 'right') {
        $ths.addClass('fright-padding');
      }
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space
