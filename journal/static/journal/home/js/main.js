// Copyright 2015 The iU Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the 'License');
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS-IS' BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

$(document).ready(function() {
  $('.background').css('height', $(window).height() + 'px');
  fadeInHeader();
  $('section').css('height', $(window).height() + 'px');
  linkSmoothScroll();

});


function fadeInHeader() {
  $('.overlay').css('display', 'none');
  $('.main-title').css('display','none');
  $('.small').css('display', 'none');
  $('.big').css('display', 'none');
  $('.greeter').css('display', 'none');
  $('header').css('display', 'none');
  setTimeout(function() {
    $('.overlay').fadeIn(300);
  }, 700);
  setTimeout(function() {
    $('.main-title').fadeIn(100);
    $('.big').fadeIn(100);
    $('.small').fadeIn(600);
    $('.greeter').fadeIn(2000);
    $('header').fadeIn(2000);
  }, 2000);
  setTimeout(function() {
    $('.bouncing-arrow').show(100);
  }, 3500);
}

function linkSmoothScroll() {
  $('a[href^='#']').click(function(event) {
    event.preventDefault();
    $('html, body').animate({
      scrollTop: $($.attr(this, 'href')).offset().top
    }, 1000);
  });
}

// Credit for the function below comes from:
// http://www.webdesignerdepot.com/2014/05/how-to-create-an-animated-sticky-header-with-css3-and-jquery/
$(window).scroll(function() {
  if ($(this).scrollTop() > 1) {
    $('.container-fluid').addClass('sticky');
  } else {
    $('.container-fluid').removeClass('sticky');
  }
  
});





