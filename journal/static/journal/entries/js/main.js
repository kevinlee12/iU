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

// Credit below goes to:
// http://stackoverflow.com/questions/17147821/how-to-make-a-whole-row-in-a-table-clickable-as-a-link
// $(document).ready(function() {
jQuery(window).on('load', function() {

  $('.grid').masonry({
    itemSelector: '.grid-item',
    columnWidth: 29
  });

  $('.grid').find('.grid-item').find('.overlay').hide();

  $('.entry-list').hover(
    function() {
      $(this).find('.overlay').fadeIn();
    },
    function() {
      $(this).find('.overlay').fadeOut();
    }
  );
});

