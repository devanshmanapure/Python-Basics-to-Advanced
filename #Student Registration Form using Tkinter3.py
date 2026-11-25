#Student Registration Form using Tkinter 3
import tkinter as tk
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x300")
tk.Label(text = "Student Registration Form", font = ("Calibri", 18)).pack(pady = 15)
tk.Label(text = "Name: ", font = ("Calibri", 18)).pack()
name_entry = tk.Entry(root, width = 30)
name_entry.pack(pady = 5)
training_mode = tk.StringVar(value = "Online")
tk.Label(text = "Training Mode: ").pack(pady = 10)
tk.Radiobutton(root, text = "Online", variable = training_mode, value = "Online").pack()
tk.Radiobutton(root, text = "Classroom", variable = training_mode, value = "Classroom").pack()

def submit():
    name = name_entry.get()
    mode = training_mode.get()
    result_label.config(text = "Welcome: " + name)
tk.Button(text = "Submit", command = submit).pack(pady = 10)
result_label = tk.Label(root, text = "", font = ("Calibri", 14))
result_label.pack(pady = 10)
root.mainloop()