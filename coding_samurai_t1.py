from tkinter import *
from tkinter import messagebox
import os

tasks = []

#function to add tasks
def add_task():
    title = title_entry.get()
    description = des_entry.get()
    
    if title and description:
        tasks.append({"title": title, "description": description, "completed": False})
        refresh()
        save_file()
        title_entry.delete(0, END)
        des_entry.delete(0, END)
    else:
        messagebox.showerror("Message", "Fill the fields")

#function to refresh taskbox at running time
def refresh():
    task_box.delete(0, END)
    for task in tasks:
        task_box.insert(END, f"{task['title']} - {task['description']} - {'Completed' if task['completed'] else 'Pending'}")

#function to write data in txt file
def save_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['title']},{task['description']},{task['completed']}\n")

#function for completed tasks
def completed():
    selected_task = task_box.curselection()
    if selected_task:
        index = selected_task[0]
        tasks[index]["completed"] = True
        refresh()
        save_file()

#function to delete a task
def delete():
    selected_task = task_box.curselection()
    if selected_task:
        index = selected_task[0]
        del tasks[index]
        refresh()
        save_file()

#function to load data from txt file when the program starts            
def load():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                title, description, completed = line.strip().split(',')
                tasks.append({"title": title, "description": description, "completed": completed == 'True'})
    refresh()

window = Tk()
window.title("To do Application")

#A frame where all widgets are placed
main_frame = Frame(window, bg="#8f918d", width=520, height=420)


#all the labels, buttons and entries
heading = Label(main_frame,
                text="Todo List",
                font=("Helvetica", 26, "bold"),
                bg="#8f918d")

title_label = Label(main_frame, 
                    text="Task title",
                    bg="#8f918d",
                    foreground="#000000",
                    font=("Helvectia",10,"bold"))

title_entry = Entry(main_frame, width=45,relief=SOLID)


des_label = Label(main_frame,
                  text="Task Description",
                  bg="#8f918d",
                  foreground="#000000",
                  font=("Helvectia",10,"bold"))

des_entry = Entry(main_frame, width=45,relief=SOLID)

add_button = Button(main_frame,
                    text="Add task",
                    command=add_task,
                    bg="#5e2cdb",
                    relief=RIDGE)

task_box = Listbox(main_frame,
                   width=82, 
                   height=13)

completed_button = Button(main_frame, 
                          text="Completed",
                          bg="green",
                          activebackground="green",
                          relief=RIDGE,
                          command=completed)

delete_button = Button(main_frame, 
                       text="Delete",
                       bg="red", 
                       relief=RIDGE,
                       activebackground="red",
                       command=delete,
                       padx=12)

#placing all the widgets using grid geometry
main_frame.grid(row=0, column=0)
main_frame.grid_propagate(False)
heading.grid(row=0, column=0, columnspan=3, padx=(10), pady=(10, 0))
title_label.grid(row=1, column=0, sticky="w", pady=(20, 5), padx=(10, 20))
title_entry.grid(row=1, column=1, sticky="w", pady=(20, 5))
des_label.grid(row=2, column=0, padx=(10, 20))
des_entry.grid(row=2, column=1, sticky="w")
add_button.grid(row=1, column=2, pady=(20, 5), padx=34, rowspan=2)
task_box.grid(row=3, column=0, padx=10, pady=20, columnspan=3, sticky="w")
completed_button.grid(row=5, column=0, pady=(0, 10), padx=(10, 15), sticky="s",columnspan=2)
delete_button.grid(row=5, column=1, pady=(0, 10), padx=(75, 10), sticky="s")

load()

window.mainloop()
