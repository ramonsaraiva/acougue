'use strict';

var controllers = angular.module('controllers', []);

controllers.controller('main_controller', ['$scope', '$http', function($scope, $http) {
	$scope.configuration = {}

	$scope.default_config = function()
	{
		$scope.configuration = {}
		$scope.configuration.cashiers = 1;
		$scope.configuration.meats = 2;
		$scope.configuration.grocery_area = 6;
		$scope.configuration.client_lambda = 2.7;
		$scope.configuration.truck_lambda = 1;
	};

	$scope.simulate = function()
	{
		$http.post('/api/simulation/', $scope.configuration).
			success(function(data) {
				alert('posted');
			}).
			error(function(e) {
				alert('error in post');
			});
	};

	$scope.default_config();
}]);
