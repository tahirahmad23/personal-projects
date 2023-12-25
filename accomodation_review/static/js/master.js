
swap();

function swap() {
  let slides = document.getElementsByClassName("mySlides");
  let currentslide = document.getElementsByClassName("mySlides active")[0];
  var index = Array.from(slides).indexOf(currentslide)
  currentslide.className = currentslide.className.replace(" active", "");
  if (slides[index+1]=== undefined) {
    slides[0].className += " active"
  }
  else {
    slides[index +1].className += " active"
  }
  setTimeout(swap, 5000);
}
