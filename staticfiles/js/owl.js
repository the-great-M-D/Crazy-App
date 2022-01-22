jQuery(document).ready(function($){

    $(".demo").owlCarousel({
        
        autoplay: 3000,
        
        items: 4,
   
        loop: true,
        dots: false,
        margin: 30,
        responsiveClass: true,
        responsive: {
          0: {
            items: 1
          },
          600: {
            items: 2
          },
          1000: {
            items: 3
          }
        }
      });



      var siteCarousel = function () {
        if ( $('#demo2').length > 0 ) {
          $('#demo2').owlCarousel({
            center: false,
            items: 1,
            loop: true,
            stagePadding: 0,
            margin: 30,
            autoplay: true,
            nav: true,
            navText: ['<span class="icon-arrow_back">', '<span class="icon-arrow_forward">'],
            responsive:{
              600:{
                
                nav: true,
                items: 1
              },
              1000:{
                
                stagePadding: 0,
                nav: true,
                items: 2
              },
              1200:{
                
                stagePadding: 0,
                nav: true,
                items: 2
              }
            }
          });
        }
    
        $('.slide-one-item').owlCarousel({
          center: false,
          items: 1,
          loop: true,
          stagePadding: 0,
          margin: 0,
          smartSpeed: 1000,
          autoplay: true,
          pauseOnHover: false,
          nav: true,
          navText: ['<span class="icon-keyboard_arrow_left">', '<span class="icon-keyboard_arrow_right">']
        });
      };
      siteCarousel();


});