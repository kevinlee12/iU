// Copyright 2015 The iU Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


$(document).ready(function() {
  resizeAction();
  $(window).resize(function () {
    resizeAction();
  });

});

function resizeAction() {
  if ($(window).width() < 768) {
    runEffect();
  }
}

$( ".sidebar-button" ).click(function() {
  runEffect();
});
$( ".button-2" ).click(function() {
  runEffect();
});


function runEffect() {
  console.log("1");
  if ($(".main").css("left") == "240px") {
    $(".main").animate({
      "left": "-=180px"
    }, 1000);

    $(".sidebar").animate({
      "left": "-=245px"
    }, 1000);

    $(".mini-sidebar").fadeIn(1000, function() {
      $(".logo-2").fadeIn(900);
      $(".button-2").fadeIn(900);
      $(".mini-sidebar").css("display", "inherit").fadeIn(1000);
      $(".mini-sidebar-icons").fadeIn(900);
    });
  }
  else if($(".main").css("left") == "60px") {
    $(".main").animate({
      "left": "+=180px"
    }, 1000);

    $(".sidebar").animate({
      "left": "+=245px"
    }, 1000);

    $(".mini-sidebar").fadeOut(30, function() {
      $(".logo-2").fadeOut(30);
      $(".button-2").fadeOut(30);
      $(".mini-sidebar").fadeOut(30);
      $(".mini-sidebar-icons").fadeOut(30);
    });
  }
}
