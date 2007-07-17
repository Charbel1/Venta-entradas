'use strict';

angular.module('app.lostpwd', ['ngRoute', 'LocalStorageModule'])

  .config(['$routeProvider', function($routeProvider) {


    $routeProvider.when('/lostpwd/', {
      templateUrl: 'components/lostpwd/lostpwd.html',
      controller: 'lostpwdContrl'

    });


  }])


  .controller('lostpwdContrl', ['$scope', '$rootScope', '$routeParams', '$location', '$interval', '$http', '$q', 'ip', 'request',
    function($scope, $rootScope, $routeParams, $location, $interval, $http, $q, ip, request) {



      // {
      // "value":"hcolmenares",
      //     "criteria":"username",
      // }
      $scope.valor="";
      $scope.cargar = false;
      $scope.error = false;


      $scope.enter = function(event) {
        console.log(event.keyCode)
        if (event.keyCode === 13 && !$scope.cargar && $scope.valor.length>0   ) {
          $scope.enviar()
        }
        else if ( $scope.valor.length ==0) {
          request.error(9999);
          $scope.error = true;

        }
      }

      $scope.enviar = function() {

        var data = {};
        data.value = $scope.valor;


        if ($scope.valor.indexOf('@') != -1) {
          data.criteria = "email"
        } else {
          data.criteria = "username"
        }

        console.log(data)
          $scope.cargar = true;
        request.post(ip + '/auth/restart-pwd/get-token', data, {
            'Content-Type': 'application/x-www-form-urlencoded'
          })
          .then(function(res) {


            console.log("envie correo")
            console.log(res)
            $location.path("/main")



          }, function(errorMsg) {
            $scope.cargar = false;
            console.log(errorMsg)
            if (errorMsg.data != null) {

              request.error(errorMsg.data.error);
            } else {
              request.error(-1);
            }
            $scope.error = true;


          });

      }


      $scope.limpiar = function() {
        $scope.valor = "";

      }

      $scope.cancelar = function() {
        $location.path("/main")

      }

    }
  ]);
