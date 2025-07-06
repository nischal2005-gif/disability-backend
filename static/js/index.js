  // JavaScript for toggling the Header Navigation Links
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');
  const body = document.body

  hamburger.addEventListener('click', () => {
      navLinks.classList.toggle('active');
      body.classList.toggle('body-collapse')
  });

  // Hide the nav menu if clicking anywhere outside the nav and hamburger
  document.addEventListener('click', (e) => {
      if (!navLinks.contains(e.target) && !hamburger.contains(e.target)) {
        navLinks.classList.remove('active');
        body.classList.remove('body-collapse')
      }
  });

// if(window.innerWidth>768){
//     body.classList.remove('body-collapse')
//     navLinks.classList.remove('active');
// }

window.addEventListener('resize', () => {
  if (window.innerWidth > 768) {
    body.classList.remove('body-collapse');
    navLinks.classList.remove('active');
  }
});