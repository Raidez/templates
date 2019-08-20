from browser import document, html
from browser.template import Template

# https://brython.info/static_doc/fr/intro.html?lang=fr

tasks = ["Make my app with Brython", "I really loved Python ♥"]

def addTask(ev, elem):
	ev.preventDefault()
	task = document.get(name='task')[0]
	if len(task.value) <= 0: return
	elem.data.tasks.append(task.value)
	task.value = ""

def delTask(ev, elem):
	index = int(ev.target.value)
	del elem.data.tasks[index]

Template('todolist', [addTask, delTask]).render(tasks=tasks)
