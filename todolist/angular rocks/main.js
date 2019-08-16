var app = angular.module('app', []);

app.controller('todolist', ($scope) => {
	$scope.tasks = ["Create app with AngularJS", "Maybe it more easier"];
	
	$scope.addTask = (event) => {
		event.preventDefault();
		let task = event.target['task'];
		let taskname = task.value;
		if (!taskname) return;
		$scope.tasks.push(taskname);
		task.value = "";
	}

	$scope.delTask = (taskid) => {
		$scope.tasks.splice(taskid, 1);
	}
});
