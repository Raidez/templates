let todolist = new Vue({
	el: '#todolist',
	data: {
		tasks: ["Make app with Vue.js", "Be happy of lightweight"]
	},
	methods: {
		addTask: function(event) {
			event.preventDefault();
			let task = new FormData(event.target).get('task');
			if (!task) return;
			this.tasks.push(task);
			event.target['task'].value = "";
		},
		delTask: function(taskid) { this.tasks.splice(taskid, 1) }
	}
});
