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
  $(function() {
    // run the currently selected effect
    function runEffect() {
      if ($(".main").css("left") == "240px") {
        $(".main").animate({
          "left": "-=220px"
        }, 1000);

        $(".sidebar").animate({
          "left": "-=245px"
        }, 1000);

        $(".button-2").css("display", "inline-block");
      }
      else if($(".main").css("left") == "20px") {
        $(".main").animate({
          "left": "+=220px"
        }, 1000);

        $(".sidebar").animate({
          "left": "+=245px"
        }, 1000);

        $(".button-2").css("display", "none");
      }
    }

    // set effect from select menu value
    $( ".sidebar-button" ).click(function() {
      runEffect();
    });
    $( ".button-2" ).click(function() {
      runEffect();
    });
  });
  
  if ($(window).width() < 650) {
    $(".main").css("left", "0");
    $(".sidebar").css("display", "none");
    $(".button-2").css("display", "inline-block");
  }

})






