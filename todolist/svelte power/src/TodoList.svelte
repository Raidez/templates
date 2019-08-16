<script>
	let tasks = ["Create app with Svelte", "It's more easily than React"];

	function addTask(event) {
		event.preventDefault();
		let task = event.target['task'];
		let taskname = task.value;
		if (!taskname) return;
		tasks = [...tasks, taskname]
		task.value = "";
	}

	function delTask(event) {
		let taskid = event.target.value;
		tasks = tasks.filter((task, id) => id != taskid);
	}
</script>

<style>
	button {
		visibility: hidden;
		color: red;
		border: none;
		background-color: transparent;
		font-weight: bold;
	}

	li:hover button {
		visibility: visible;
		cursor: pointer;
	}
</style>

<ul>
	{#each tasks as task, id}
		<li>
			{task}
			<button on:click={delTask} value={id}>&times;</button>
		</li>
	{/each}
</ul>

<form on:submit={addTask}>
	<input type="text" name="task" placeholder="Other task..." />
	<input type="submit" value="Add task" />
</form>