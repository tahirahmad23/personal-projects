$(document).ready(function(){
  // On document load, check window width and toggle caption visibility
  checkWidth();

  // On window resize, check and toggle caption visibility
  $(window).resize(function(){
    checkWidth();
  });

  // Function to toggle caption visibility based on window width
  function checkWidth(){
    if($(window).width() < 576){
      $('.carousel-caption').css('display', 'block');
    } else {
      $('.carousel-caption').css('display', '');
    }
  }
});
