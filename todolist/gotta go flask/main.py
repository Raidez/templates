from flask import Flask, request, render_template, redirect
app = Flask(__name__)
tasks = list()
_tasks = ["Make app with Flask", "It's more easily than Django"]
once = True

@app.route('/')
def hello_world():
	global once, tasks, _tasks
	if once:
		once = False
		tasks = _tasks.copy()
	return render_template('index.html', tasks=tasks)

@app.route('/addTask', methods=['POST'])
def addTaskPost():
	task = request.form['task']
	if len(task) > 0:
		return addTask(task)
	return redirect('/')

@app.route('/addTask/<string:task>')
def addTask(task):
	global tasks
	tasks.append(task)
	return redirect('/')

@app.route('/delTask/<int:index>')
def delTask(index):
	global tasks
	del tasks[index]
	return redirect('/')

@app.route('/reset')
def reset():
	global tasks, _tasks
	tasks = _tasks.copy()
	return redirect('/')

@app.errorhandler(404)
def pageNotFound(e):
	return redirect('/')

app.run(port=8080, debug=True)
