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
      $scope.si = false;
      $scope.codigo = ""
      $scope.cedula = ""
      // {
      // "value":"hcolmenares",
      //     "criteria":"username",
      // }
      $scope.valor = "";
      $scope.cargar = false;
      $scope.aux2 = false
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

          if ($scope.codigo.length > 0) {
            console.log("entre")
            $scope.buscarCo($scope.codigo)

          } else if ($scope.cedula.length > 0) {
            $scope.buscar($scope.cedula)
          }


        }
      }

      $scope.enviar = function(feo) {


        var data = {};
        data.feo = feo
        data.cedula = $scope.data.cedula




        request.post(ip + '/wango/entro', data, {
            'Content-Type': 'application/x-www-form-urlencoded'
          })
          .then(function(res) {
            if (res.data.error != 0) {

              $scope.auxerror = true
              $scope.error = res.data.error
            } else {
              $scope.aux2 = true
              $scope.auxerror = false
              $scope.si = true;
              $scope.auxerror = true
              $scope.error = "Ok"
            }

          }, function(errorMsg) {
            $scope.auxerror = true
            $scope.error = "Error de conexión"


          });

      }


      $scope.buscar = function(cedula) {
        $scope.aux2 = false
        $scope.si = false

        var data = {}

        data.cedula = cedula
        request.post(ip + '/wango/buscarC', data, {
            'Content-Type': 'application/x-www-form-urlencoded'
          })
          .then(function(res) {

            if (res.data.error != 0) {

              $scope.auxerror = true
              $scope.error = res.data.error
            } else {
              $scope.aux2 = false
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

      $scope.buscarCo = function(codigo) {
        $scope.aux2 = true
        $scope.si = false

        var data = {}

        data.codigo = "'" + codigo + "'"
        request.post(ip + '/wango/buscarCodigo', data, {
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
