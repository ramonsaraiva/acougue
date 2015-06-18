'use strict';

var app = angular.module('acougue', [
	'ngRoute',
	'angular-flot',
	'controllers'
]);

app.config(['$routeProvider', function($routeProvider) {
	$routeProvider
		.when('/', {
		});
}]);
