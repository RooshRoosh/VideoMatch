/**
 * Created with PyCharm.
 * User: dns
 * Date: 31.03.15
 * Time: 23:57
 * To change this template use File | Settings | File Templates.
 */


var myApp = angular.module('myApp', []);

myApp.constant('YT_event', {
    STOP:            0,
    PLAY:            1,
    PAUSE:           2
});

myApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{${');
  $interpolateProvider.endSymbol('}$}');
});



myApp.directive('youtube', function($window){
    return {
        'restrict': 'E',
        'template': "<div></div>",
        'scope':{
            'height':'@',
            'width':"@",
            'videoid':"@"
        },
        'link': function(scope, $element, $attrs){
            console.log(scope);
            var tag = document.createElement('script');
            tag.src = "https://www.youtube.com/iframe_api";
            var firstScriptTag = document.getElementsByTagName('script')[0];
            firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
            var player;


            $window.onYouTubeIframeAPIReady = function() {
                player = new YT.Player($element.children()[0], {
                  playerVars: {
                    autoplay: 1,
                    html5: 1,
                    theme: "light",
                    modesbranding: 0,
                    color: "white",
                    iv_load_policy: 3,
                    showinfo: 1,
                    controls: 1
                  },
                  height: scope.height,
                  width: scope.width,
                  videoId: scope.videoid
                });
            };

//            scope.$on(0, function () {
//                console.log('stop');
//                player.seekTo(0);
//                player.stopVideo();
//
//            });
//
//            scope.$on(1, function () {
//                console.log('play');
//                player.playVideo();
//            });
//
//            scope.$on(2, function () {
//                console.log('pause');
//                player.pauseVideo();
//            });


            scope.$watch('videoid', function(newValue, oldValue) {
              if (newValue == oldValue) {
                return;
              }
              player.cueVideoById($scope.videoid);
              scope.newVideoLoad = true;

            });


        }
    }
});



myApp.controller('videoLabeling',['$scope','$http','$q',
    function($scope, $http, $q){

        $scope.videoTitle = '';

        $scope.originalQuestion = 'Как стараться?';
        $scope.translatedQuestion = 'How to try hard?';
        $scope.youtubeUrl = 'http://www.youtube.com/watch?v=7Ds30KqLaHs';
        $scope.videoid = '7Ds30KqLaHs';
        $scope.player = null;
        $scope.newVideoLoad = true;

        $scope.playerInit = function(){
            // Подгружаем первое видео
        };
        $scope.enableControl = function(){
            $scope.newVideoLoad = false;
        };
        $scope.yesButtonClick = function(){
          console.log('yes we can');
        };

        $scope.noButtonClick = function (){
            console.log("yes we can't");
        };

        $scope.sendAnswer = function(answer){
            var url = '',
                deferred = $q.defer();

            $http.post(url, data)
                .success(
                    function(data){
                        $scope.loadVideo(data.youtubeUrl);
                        $scope.videoTitle = data.videoTitle;
//                        $scope
                        deferred.resolve();
                    }
                )
                .error(
                    function(data){
                        deferred.reject();
                    }
                )
            return deferred.promise;
        };
        $scope.loadVideo = function(newVideo){

        }
    }]
);