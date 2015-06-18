'use strict';

var app = angular.module('acougue', [
	'ngRoute',
	'controllers'
]);

app.config(['$routeProvider', function($routeProvider) {
	$routeProvider
		.when('/', {
		});
}]);
