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

var app = angular.module('mainApp', []);

app.controller('activityTutorialCtrl',
  ['$scope', function($scope) {
    function bounce() {
      $.get('/bounce');
      $.get('/ping', function(data) {
        $('.badge').html(data);
      });
    }

    $scope.clicks = 0;
    console.log('I <3 Huahua'); // Remove me when I am done.

    $scope.triggerStepCount = function() {
      console.log('I <3 Huahua'); // Remove me when I am done.
      $scope.clicks++;
      if ($scope.clicks === 1) {
        $('.add-journal-sign').css('z-index', '3');
      } else if ($scope.clicks === 2) {
        $('.add-journal-sign').css('z-index', '0');
        $('.activity-box').css('z-index', '3');
      } else if ($scope.clicks === 3) {
        $('.activity-box').css('z-index', '0');
        $('.dropdown-toggle').css('z-index', '3');
      } else if ($scope.clicks === 4) {
        $('.dropdown-toggle').css('z-index', '0');
        $('.overlay').remove();
        $scope.clicks = 0; 
      }
    };

    $scope.triggerBackCount = function() {
      $scope.clicks--;
    };

    $scope.skip = function() {
      $scope.clicks = 0;
    };

  }
]);
