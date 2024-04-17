import mysql.connector
import tkinter as tk
from tkinter import ttk

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Surya@630',
    database='taskmanager'
)

def add_task(task_name, description, category, due_date, priority):
    cursor = db.cursor()
    sql = "INSERT INTO tasks (task_name, description, category, due_date, priority) VALUES (%s, %s, %s, %s, %s)"
    val = (task_name, description, category, due_date, priority)
    cursor.execute(sql, val)
    db.commit()
    status_label.config(text="Hey Surya your task added successfully!")

def view_tasks():
    cursor = db.cursor()
    sql = "SELECT * FROM tasks"
    cursor.execute(sql)
    tasks = cursor.fetchall()
    task_text = ""
    if tasks:
        for task in tasks:
            task_text += f"Task ID: {task[0]}, Task Name: {task[1]}, Description: {task[2]}, Category: {task[3]}, Due Date: {task[4]}, Priority: {task[5]}\n"
    else:
        task_text = "No Tasks in the DataBase"
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, task_text)

def mark_completed(task_id):
    cursor = db.cursor()
    sql = "UPDATE tasks SET is_completed = 1 WHERE id = %s"
    val = (task_id,)
    cursor.execute(sql, val)
    db.commit()
    status_label.config(text="Hey Surya this task is completed Yayy!")

def update_task(task_id, task_name, description, category, due_date, priority):
    cursor = db.cursor()
    sql = "UPDATE tasks SET task_name = %s, description = %s, category = %s, due_date = %s, priority = %s WHERE id = %s"
    val = (task_name, description, category, due_date, priority, task_id)
    cursor.execute(sql, val)
    db.commit()
    status_label.config(text="Hey Surya task details are updated for this one!")

def delete_task(task_id):
    cursor = db.cursor()
    sql = "DELETE FROM tasks WHERE id = %s"
    val = (task_id,)
    cursor.execute(sql, val)
    db.commit()
    status_label.config(text=" Hey Surya task is deleted!")

def handle_add_task():
    task_name = task_name_entry.get()
    description = description_entry.get()
    category = category_combobox.get()
    due_date = due_date_entry.get()
    priority = priority_combobox.get()
    add_task(task_name, description, category, due_date, priority)

def handle_view_tasks():
    view_tasks()

def handle_mark_completed():
    task_id = int(task_id_entry.get())
    mark_completed(task_id)

def handle_update_task():
    task_id = int(task_id_entry.get())
    task_name = task_name_entry.get()
    description = description_entry.get()
    category = category_combobox.get()
    due_date = due_date_entry.get()
    priority = priority_combobox.get()
    update_task(task_id, task_name, description, category, due_date, priority)

def handle_delete_task():
    task_id = int(task_id_entry.get())
    delete_task(task_id)

root = tk.Tk()
root.title("Task Management System")

# Labels
task_name_label = tk.Label(root, text="Task Name:")
task_name_label.grid(row=0, column=0)

description_label = tk.Label(root, text="Description:")
description_label.grid(row=1, column=0)

category_label = tk.Label(root, text="Category:")
category_label.grid(row=2, column=0)

due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
due_date_label.grid(row=3, column=0)

priority_label = tk.Label(root, text="Priority:")
priority_label.grid(row=4, column=0)

task_id_label = tk.Label(root, text="Task ID:")
task_id_label.grid(row=5, column=0)

# Entries
task_name_entry = tk.Entry(root)
task_name_entry.grid(row=0, column=1)

description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1)

category_combobox = ttk.Combobox(root, values=["Work", "Personal", "Study", "Other"])
category_combobox.grid(row=2, column=1)

due_date_entry = tk.Entry(root)
due_date_entry.grid(row=3, column=1)

priority_combobox = ttk.Combobox(root, values=["High", "Medium", "Low"])
priority_combobox.grid(row=4, column=1)

task_id_entry = tk.Entry(root)
task_id_entry.grid(row=5, column=1)

# Buttons
add_button = tk.Button(root, text="Add Task", command=handle_add_task)
add_button.grid(row=6, column=0, columnspan=2, pady=5)

view_button = tk.Button(root, text="View Tasks", command=handle_view_tasks)
view_button.grid(row=7, column=0, columnspan=2, pady=5)

mark_completed_button = tk.Button(root, text="Mark Completed", command=handle_mark_completed)
mark_completed_button.grid(row=8, column=0, columnspan=2, pady=5)

update_button = tk.Button(root, text="Update Task", command=handle_update_task)
update_button.grid(row=9, column=0, columnspan=2, pady=5)

delete_button = tk.Button(root, text="Delete Task", command=handle_delete_task)
delete_button.grid(row=10, column=0, columnspan=2, pady=5)

# Output Text
output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=11, column=0, columnspan=2)

status_label = tk.Label(root, text="")
status_label.grid(row=12, column=0, columnspan=2)

root.mainloop()

