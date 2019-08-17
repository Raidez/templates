from tkinter import *

text_font = ("Times New Roman", 16)

class TodoList(Frame):
	def __init__(self, master, tasks=[], **kwargs):
		Frame.__init__(self, master, kwargs)
		self.tasks = tasks
		self.event_add('<<AddTask>>', '<Button-1>', '<Return>')
		self.event_add('<<DelTask>>', '<Button-1>')
		self.generate()
	
	def add_task(self, task):
		if len(task) > 0:
			self.tasks.append(task)
			self.generate()
	
	def del_task(self, index):
		del self.tasks[index]
		self.generate()
	
	def generate(self):
		for widget in self.winfo_children():
			widget.destroy()
		
		# génération de la liste des tâches
		for index, task in enumerate(self.tasks):
			TodoItem(self, index, f"• {task}").pack(side=TOP, fill=X, expand=1)
		
		# génération du formulaire
		taskname = StringVar()
		task_form = Entry(self, textvariable=taskname)
		task_form.pack(side=LEFT)
		task_form.bind('<<AddTask>>', lambda e: self.add_task(taskname.get()))

		button = Button(self, text="Add task")
		button.pack(side=LEFT)
		button.bind('<<AddTask>>', lambda e: self.add_task(taskname.get()))

class TodoItem(Frame):
	def __init__(self, master, index, label, **kwargs):
		Frame.__init__(self, master, kwargs)

		# texte à puce
		default_style_label = {
			'text': label,
			'anchor': W,
			'font': text_font
		}
		self.label = Label(self, {**default_style_label, **kwargs})
		self.label.pack(side=LEFT)

		# button de suppresion
		default_style_button = {
			'text': "×",
			'foreground': "Red",
			'anchor': W,
			'font': text_font + ("bold", ),
			'borderwidth': 0,
			'cursor': "hand2"
		}
		self.button = Button(self, {**default_style_button, **kwargs})
		self.button.pack(side=LEFT)

		# gestion de l'apparition du bouton
		self.button_pack_info = self.button.pack_info()
		self.button.pack_forget()
		self.bind('<Enter>', lambda e: self.toggle_button(True))
		self.bind('<Leave>', lambda e: self.toggle_button(False))

		# suppression de la tâche
		self.button.bind('<<DelTask>>', lambda e: self.master.del_task(index))
	
	def toggle_button(self, is_show):
		if is_show:
			self.button.pack(self.button_pack_info)
		else:
			self.button.pack_forget()
