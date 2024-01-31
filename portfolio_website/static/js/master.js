$(document).ready(function(){
  $(".nav-link, .navbar-brand").on("click",function(){

    $(".nav-link").removeClass("current");
    $(".navbar-brand").removeClass("current");
    $(this).addClass("current");
  });
});
