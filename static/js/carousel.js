document.addEventListener('DOMContentLoaded', function () {
  let index = 0; // Current index of the visible item
  const items = document.querySelectorAll('.carousel-item');
  const totalItems = items.length;

  document.querySelector('.prev').addEventListener('click', function() {
    if (index > 0) {
      index--;
    } else {
      index = totalItems - 1;
    }
    updateCarousel();
  });

  document.querySelector('.next').addEventListener('click', function() {
    if (index < totalItems - 1) {
      index++;
    } else {
      index = 0;
    }
    updateCarousel();
  });

  function updateCarousel() {
    const offset = -index * 100; // Assuming each item is 100% of the container width
    document.querySelector('.carousel-items').style.transform = `translateX(${offset}%)`;
  }
});