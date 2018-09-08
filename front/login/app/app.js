'use strict';



// Declare app level module which depends on views, and components
angular.module('app', [
    'ngRoute',
    'btford.socket-io',
    'app.dashboard',
    'app.version',
    'app.lostpwd',

  ])


  .constant('ip', 'http://192.168.1.69:5033')
  .factory('request', ['$http', '$q','$rootScope', function($http, $q,$rootScope) {
    return {
      get: function(url) {
        var defered = $q.defer();
        $http({
          method: "GET",
          url: url
        }).then(function(response) {
          defered.resolve(response);
        }, function(errorMsg) {
          defered.reject(errorMsg);
        });
        return defered.promise;
      },
      post: function(url, data, headers) {
        var defered = $q.defer();

        $http({
          method: "POST",
          url: url,
          data: data,
          headers: headers
        }).then(function(response) {
          defered.resolve(response);
        }, function(errorMsg) {
          defered.reject(errorMsg);
        });
        return defered.promise;
      },
      error: function(caseStr) {
        console.log(caseStr)
        switch (caseStr) {
             case 202:
                $rootScope.errormsg =" Clave y/o Usuario."
                 break;
             case 9999:
                  $rootScope.errormsg ="Rellene Todos Los Campos"
                 break;
                 case -1:
                    $rootScope.errormsg ="Error de Conexión"
                     break;
             default:

         }
      }



    }
  }])


  .config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
    $locationProvider.hashPrefix('!');

    $routeProvider.otherwise({
      redirectTo: '/dashboard'
    });
  }]);
