'use strict';

var controllers = angular.module('controllers', []);

controllers.controller('main_controller', ['$scope', '$http', function($scope, $http) {
	$scope.configuration = {}
	$scope.result = false;
	$scope.data = {}
	$scope.charts = {}
	$scope.charts.incoming_outgoing = {}

	$scope.default_config = function()
	{
		$scope.configuration = {}
		$scope.configuration.cashiers = 1;
		$scope.configuration.meats = 2;
		$scope.configuration.grocery_area = 6;
		$scope.configuration.client_lambda = 2.7;
		$scope.configuration.truck_quantity = 3;
	};

	$scope.charts.incoming_outgoing.options = {
		series: {
			lines: { show: true },
			points: { show: true }
		},
		grid: {
			labelMargin: 10,
			hoverable: true,
			tooltip: true
		}
	}

	$scope.simulate = function()
	{
		$http.post('/api/simulation/', $scope.configuration).
			success(function(data) {
				$scope.result = true;

				$scope.data.client_incoming = data.client_incoming;
				$scope.data.client_outgoing = data.client_outgoing;
				$scope.data.clients = data.clients;
				$scope.data.trucks = data.trucks;

				$scope.charts.incoming_outgoing.data = [
					{'label': 'Client incoming', data: $scope.data.client_incoming},
					{'label': 'Client outgoing', data: $scope.data.client_outgoing}
				]
			}).
			error(function(e) {
				alert('error in post');
			});
	};

	$scope.default_config();
}]);
