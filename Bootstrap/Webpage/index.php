<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Level Mobility</title>

    <!-- Bootstrap Core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">
    <link href="vendor/simple-line-icons/css/simple-line-icons.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/stylish-portfolio.min.css" rel="stylesheet">

    <!--AJAX -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

  </head>

  <body id="page-top">
      <!-- Navigation -->
      <a class="menu-toggle rounded" href="#">
          <i class="fas fa-bars"></i>
      </a>
      <nav id="sidebar-wrapper">
          <ul class="sidebar-nav">
              <li class="sidebar-brand">
                  <a class="js-scroll-trigger" href="#page-top">Start Bootstrap</a>
              </li>
              <li class="sidebar-nav-item">
                  <a class="js-scroll-trigger" href="#page-top">Home</a>
              </li>
              <li class="sidebar-nav-item">
                  <a class="js-scroll-trigger" href="#about">About</a>
              </li>
              <li class="sidebar-nav-item">
                  <a class="js-scroll-trigger" href="#services">Services</a>
              </li>
              <li class="sidebar-nav-item">
                  <a class="js-scroll-trigger" href="#portfolio">Portfolio</a>
              </li>
              <li class="sidebar-nav-item">
                  <a class="js-scroll-trigger" href="#contact">Contact</a>
              </li>
          </ul>
      </nav>
      <!-- Header -->
      <header class="masthead d-flex">
          <div class="container text-center my-auto">
              <h1 class="mb-5">Level Headed Mobility</h1>
              <h3 class="mb-5">
                  <em>A Saftey Driven Solution to Avoiding Recklessness</em>
              </h3>
              <a class="btn btn-primary btn-xl js-scroll-trigger" href="#services">Learn More</a>
          </div>
          <div class="overlay"></div>
      </header>
      <!-- About
        <section class="content-section bg-light" id="about">
          <div class="container text-center">
            <div class="row">
              <div class="col-lg-10 mx-auto">
                <h2>Stylish Portfolio is the perfect theme for your next project!</h2>
                <p class="lead mb-5">This theme features a flexible, UX friendly sidebar menu and stock photos from our friends at
                  <a href="https://unsplash.com/">Unsplash</a>!</p>
                <a class="btn btn-dark btn-xl js-scroll-trigger" href="#services">What We Offer</a>
              </div>
            </div>
          </div>
        </section>
       -->
      <!-- Services -->
      <section class="content-section bg-primary text-white text-center" id="services">
          <div class="container">
              <div class="content-section-heading">
                  <h3 class="text-secondary mb-0">Services</h3>
                  <h2 class="mb-5">What We Offer</h2>
              </div>
              <div class="row">
                  <div class="col-lg-3 col-md-6 mb-5 mb-lg-0">
                      <span class="service-icon rounded-circle mx-auto mb-3">
                          <i class="icon-shield"></i>
                      </span>
                      <h4>
                          <strong>Safe</strong>
                      </h4>
                      <p class="text-faded mb-0">Be aware of dangerous drivers!</p>
                  </div>
                  <div class="col-lg-3 col-md-6 mb-5 mb-lg-0">
                      <span class="service-icon rounded-circle mx-auto mb-3">
                          <i class="icon-refresh"></i>
                      </span>
                      <h4>
                          <strong>Recent</strong>
                      </h4>
                      <p class="text-faded mb-0">Real-time updates around you.</p>
                  </div>
                  <div class="col-lg-3 col-md-6 mb-5 mb-md-0">
                      <span class="service-icon rounded-circle mx-auto mb-3">
                          <i class="icon-like"></i>
                      </span>
                      <h4>
                          <strong>Simple</strong>
                      </h4>
                      <p class="text-faded mb-0">
                          Easy to use, just 1 click!
                      </p>
                  </div>
                  <div class="col-lg-3 col-md-6">
                      <span class="service-icon rounded-circle mx-auto mb-3">
                          <i class="icon-speedometer"></i>
                      </span>
                      <h4>
                          <strong>Mobility</strong>
                      </h4>
                      <p class="text-faded mb-0">Get where you need to be</p>
                  </div>
              </div>
              <a  style="margin-top: 5vh;" class="btn btn-xl btn-light mr-4" href="#portfolio">Check it out</a>
          </div>
      </section>
      <!-- Callout -->
     <!--  <section class="callout">
          <div class="container text-center">
              <h2 class="mx-auto mb-5">
                  Welcome to
                  <em>your</em>
                  next website!
              </h2>
              <a class="btn btn-primary btn-xl" href="https://startbootstrap.com/template-overviews/stylish-portfolio/">Download Now!</a>
          </div>
      </section> -->
      <!-- Portfolio -->
      <section class="content-section" id="portfolio">
          <div class="container">
              <div class="content-section-heading text-center">
                  <h3 class="text-secondary mb-0">Demo using real-time data</h3>
                  <h2 class="mb-5">Try It Out</h2>
              </div>
              <button class="btn btn-primary btn-xl js-scroll-trigger" style="width: 20%; margin-left: 40%;" type="button" onClick="document.location.href='UI_backend.php'">Start Demo</button>

             <!--  <script type="text/javascript"charset="utf-8">
    
                function loadDoc() {
                    var xhttp = new XMLHttpRequest();
                    xhttp.onreadystatechange = function() {
                      /*  Holds the status of the XMLHttpRequest.
                    0: request not initialized 
                    1: server connection established
                    2: request received 
                    3: processing request 
                    4: request finished and response is ready
                    */
                      if (this.readyState == 4) {
                        if (this.status == 200) {
                          document.getElementById("demo").innerHTML = this.responseText;
                        }
                        else {
                          alert(this.status + " error");
                        }
                      }
                    };
                    xhttp.open("GET", "gettabledata.php?q=", true);
                    xhttp.send();
                }

                // var refreshId = setInterval(function() {
                //   loadDoc();
                //       }, 2000);
              </script> -->

              <!-- <button style="margin-left:auto; margin-right: auto;" type="button">Click Me!</button> -->
              <!-- <div class="row no-gutters">
                  <div class="col-lg-6">
                      <a class="portfolio-item" href="#">
                          <span class="caption">
                              <span class="caption-content">
                                  <h2>Stationary</h2>
                                  <p class="mb-0">A yellow pencil with envelopes on a clean, blue backdrop!</p>
                              </span>
                          </span>
                          <img class="img-fluid" src="img/portfolio-1.jpg" alt="">
                      </a>
                  </div>
                  <div class="col-lg-6">
                      <a class="portfolio-item" href="#">
                          <span class="caption">
                              <span class="caption-content">
                                  <h2>Ice Cream</h2>
                                  <p class="mb-0">A dark blue background with a colored pencil, a clip, and a tiny ice cream cone!</p>
                              </span>
                          </span>
                          <img class="img-fluid" src="img/portfolio-2.jpg" alt="">
                      </a>
                  </div>
                  <div class="col-lg-6">
                      <a class="portfolio-item" href="#">
                          <span class="caption">
                              <span class="caption-content">
                                  <h2>Strawberries</h2>
                                  <p class="mb-0">Strawberries are such a tasty snack, especially with a little sugar on top!</p>
                              </span>
                          </span>
                          <img class="img-fluid" src="img/portfolio-3.jpg" alt="">
                      </a>
                  </div>
                  <div class="col-lg-6">
                      <a class="portfolio-item" href="#">
                          <span class="caption">
                              <span class="caption-content">
                                  <h2>Workspace</h2>
                                  <p class="mb-0">A yellow workspace with some scissors, pencils, and other objects.</p>
                              </span>
                          </span>
                          <img class="img-fluid" src="img/portfolio-4.jpg" alt="">
                      </a>
                  </div>
              </div> -->
          </div>
      </section>
      <!-- Call to Action -->
    <!--   <section class="content-section bg-primary text-white">
          <div class="container text-center">
              <h2 class="mb-4">The buttons below are impossible to resist...</h2>
              <a href="#" class="btn btn-xl btn-light mr-4">Click Me!</a>
              <a href="#" class="btn btn-xl btn-dark">Look at Me!</a>
          </div> -->
      </section>
      <!-- Map -->
      <section id="contact" class="map">
          <iframe width="100%" height="100%" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=+Spark+Headquarters,+Ann+Arbor,+MI&amp;aq=0&amp;oq=twitter&amp;sll=28.659344,-81.187888&amp;sspn=0.128789,0.264187&amp;ie=UTF8&amp;hq=Twitter,+Inc.,+Market+Street,+San+Francisco,+CA&amp;t=m&amp;z=15&amp;iwloc=A&amp;output=embed"></iframe>
          <br />
          <small>
              <a href="https://maps.google.com/maps?f=q&amp;source=embed&amp;hl=en&amp;geocode=&amp;q=Twitter,+Inc.,+Market+Street,+San+Francisco,+CA&amp;aq=0&amp;oq=twitter&amp;sll=28.659344,-81.187888&amp;sspn=0.128789,0.264187&amp;ie=UTF8&amp;hq=Twitter,+Inc.,+Market+Street,+San+Francisco,+CA&amp;t=m&amp;z=15&amp;iwloc=A"></a>
          </small>
      </section>
      <!-- Footer -->
      <footer class="footer text-center">
          <div class="container">
              
              <p class="text-muted small mb-0">Copyright &copy; Level Headed Mobility
                <br>Louis Gouirand, Utsav Lathia & Adam Schreck</p>
          </div>
      </footer>
      <!-- Scroll to Top Button-->
      <a class="scroll-to-top rounded js-scroll-trigger" href="#page-top">
          <i class="fas fa-angle-up"></i>
      </a>
      <!-- Bootstrap core JavaScript -->
      <script src="vendor/jquery/jquery.min.js"></script>
      <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
      <!-- Plugin JavaScript -->
      <script src="vendor/jquery-easing/jquery.easing.min.js"></script>
      <!-- Custom scripts for this template -->
      <script src="js/stylish-portfolio.min.js"></script>
  </body>

</html>
