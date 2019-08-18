from tkinter import *
from todolist import *

root = Tk()
tasks = ["Create app with Tkinter", "I love Python, it softy"]

Label(root, text="Todolist", font=("Times New Roman", 32, "bold"), anchor=W).pack(side=TOP, fill=X)

ul = TodoList(root, tasks=tasks)
ul.add_task("It's works !")
ul.pack(side=TOP, fill=X)

root.mainloop()
