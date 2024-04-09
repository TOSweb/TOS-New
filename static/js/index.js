function toggleFunction() {
    console.log('hh')
    var x = document.getElementById("topnav");
    x.classList.toggle("expanded");
}

function checkOrientation() {
    var x = document.getElementById("topnav");
    if (window.matchMedia("(orientation: landscape)").matches) { // Change the class name to "landscape" when in landscape orientation

        if (x.className === "nav-container responsive") {
            x.className = "nav-container"
        }


    } else {}
}

checkOrientation();

// Listen for the window resize event to detect orientation changes
window.addEventListener('resize', checkOrientation);



function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

document.addEventListener("DOMContentLoaded", function() {
    // Get all the tablinks in the document
    var tablinks = document.getElementsByClassName("libtablinks");
  
    // Function to hide all content and remove "active" class from all tabs
    function hideAllContentAndRemoveActiveClass() {
      var content = document.getElementsByClassName("libtabcontent");
      for (let i = 0; i < content.length; i++) {
        content[i].style.display = "none";
      }
      for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
      }
    }
  
    // Function to show content of the clicked tab
    function showContent(index) {
      document.getElementsByClassName("libtabcontent")[index].style.display = "block";
      tablinks[index].classList.add("active");
    }
  
    // Attach click event to each tab
    for (let i = 0; i < tablinks.length; i++) {
      tablinks[i].addEventListener("click", function() {
        hideAllContentAndRemoveActiveClass();
        showContent(i);
      });
    }
  
    // Initially hide all content except the first one
    hideAllContentAndRemoveActiveClass();
    // Then show the first tab content by default
    if (tablinks.length > 0) showContent(0);
  });


  

  
