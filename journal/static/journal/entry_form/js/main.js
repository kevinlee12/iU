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

function required_append(url) {
  var item = url.split('#')[1];
  $('textarea').prop('required', false);
  $('[name=image_entry]').prop('required', false);
  $('[name=link_entry]').prop('required', false);
  if (item === 'text') {
    $('textarea').prop('required', true);
  } else if (item === 'image') {
    $('[name=image_entry]').prop('required', true);
  } else if (item === 'link') {
    $('[name=link_entry]').prop('required', true);
  }
}

$(document).ready(function() {

  $('form').find('iframe').contents().find('body')
  .find('.note-editor').find('.note-dialog')
  .find('.note-image-dialog').find('.modal-dialog')
  .find('.modal-content').find('.modal-body')
  .find('.form-group:first').find('label')
  .append('<small> Maximum image dimensions: 1024x1024 pixel </small>');

  var url = document.location.hash;
  $('.nav-tabs a[href=#' + url.split('#')[1] + ']').tab('show');
  required_append(url);

  $('.nav-tabs a').on('shown.bs.tab', function(e) {
    window.location.hash = e.target.hash;
    required_append(window.location.hash);
  });
  $('#myModal').on('shown.bs.modal', function() {
    $('#myInput').focus();
  });

  $('form').find('iframe').load(function() {
    $(this).contents().find('body')
    .find('.note-editor').find('.note-dialog')
    .find('.note-image-dialog').find('.modal-dialog')
    .find('.modal-content').find('.modal-body')
    .find('.form-group:first').find('label')
    .append('<small> <br>Maximum image dimensions: 1024x1024 pixel </small>');
  });



  // Summernote Image Mods
  // $('form').find('iframe').load(function(){
  //   $(this).find('#summernote').summernote({
  //     onImageUpload: function(files, editor, welEditable) {
  //       console.log(files, editor, welEditable);
  //     }
  //   });
  // });

});
