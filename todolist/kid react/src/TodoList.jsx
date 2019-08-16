import React, { Component } from "react";
import "./TodoList.css";

class TodoList extends Component {
	constructor() {
		super();
		this.state = { tasks: ["Create app with React", "Make it easy", "Commit on GitHub"] };

		this.addTask = this.addTask.bind(this);
		this.delTask = this.delTask.bind(this);
	}

	addTask(event) {
		event.preventDefault();
		let task = event.target['task'];
		let tasks = this.state.tasks;
		let taskname = task.value;
		if (!taskname) return;
		tasks.push(taskname);
		task.value = "";
		this.setState({ tasks: tasks });
	}

	delTask(event) {
		let taskid = event.target.value;
		let tasks = this.state.tasks;
		tasks.splice(taskid, 1);
		this.setState({ tasks: tasks });
	}

	render() {
		return(
			<div>
				<ul>
					{ this.state.tasks.map((task, id) => (
						<li key={id}>
							{ task }
							<button onClick={this.delTask} value={id}>&times;</button>
						</li>
					)) }
				</ul>

				<form onSubmit={this.addTask}>
					<input type="text" name="task" placeholder="Other task..." autoFocus />
					<input type="submit" value="Add task" />
				</form>
			</div>
		);
	}
}

export default TodoList;