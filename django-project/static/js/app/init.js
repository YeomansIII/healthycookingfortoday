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

    window.getUrlParameter = function getUrlParameter(sParam) {
      var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

      for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
          return sParameterName[1] === undefined ? true : sParameterName[1];
        }
      }
    };

    $('.modal-trigger').leanModal();

  }); // end of document ready
})(jQuery); // end of jQuery name space
