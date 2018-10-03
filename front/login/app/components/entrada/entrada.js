'use strict';

angular.module('app.entrada', ['ngRoute', 'LocalStorageModule'])

  .config(['$routeProvider', function($routeProvider) {


    $routeProvider.when('/entrada/', {
      templateUrl: 'components/entrada/entrada.html',
      controller: 'entradaContrl'

    });


  }])


  .controller('entradaContrl', ['$scope', '$rootScope', '$routeParams', '$location', '$interval', '$http', '$q', 'ip', 'request',
    function($scope, $rootScope, $routeParams, $location, $interval, $http, $q, ip, request) {

      $scope.data = {}
      $scope.si = true;
      $scope.entrada = ""
      $scope.cedula = ""
      // {
      // "value":"hcolmenares",
      //     "criteria":"username",
      // }
      $scope.valor = "";
      $scope.cargar = false;
      $scope.error = false;

      $scope.cambio = function(valor) {
        if (valor == 'codigo') {
          $scope.aux2 = true

        } else {
          $scope.aux2 = false
        }
        $scope.limpiar()

      }

      $scope.otro = function()

      {
        $scope.si = false
        $scope.data = {}

      }

      $scope.enter = function(event) {

        if (event.keyCode === 13) {

          if ($scope.entrada.length > 0) {
            alert("")

          } else if ($scope.cedula.length > 0) {
            $scope.buscar()
          }


        }
      }

      $scope.enviar = function(feo) {


        var data = {};
        data.feo = feo


        if ($scope.aux2 == true) {
          data.criteria = 'codigo'
          data.valor = $scope.codigo
        } else {
          data.valor = $scope.cedula
          data.criteria = "cedula"
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


      $scope.buscar = function(cedula) {
        $scope.aux2 = false
        $scope.si = false

        var data = {}

        data.cedula = "123"
        request.post(ip + '/wango/buscarC', data, {
            'Content-Type': 'application/x-www-form-urlencoded'
          })
          .then(function(res) {

            if (res.data.error != 0) {

              $scope.auxerror = true
              $scope.error = res.data.error
            } else {
              $scope.aux2 = true
              $scope.auxerror = false
              console.log(res.data.data)
              $scope.data = res.data.data
              $scope.si = true;
            }

          }, function(errorMsg) {
            $scope.auxerror = true
            $scope.error = "Error de conexión"

          });


      }



      $scope.limpiar = function() {
        $scope.valor = "";
        $scope.cedula = "";
        $scope.codigo = "";

        $scope.si = false
        $scope.auxerror = false
        $scope.error = "";

      }

      $scope.cancelar = function() {
        $location.path("/main")

      }

    }
  ]);
