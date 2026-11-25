#Student Registration Form using Tkinter 2
import tkinter as tk
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x300")
tk.Label(text = "Student Registration Form", font = ("Calibri", 18)).pack(pady = 15)
tk.Label(text = "Name: ", font = ("Calibri", 18)).pack()
name_entry = tk.Entry(root, width = 30)
name_entry.pack(pady = 5)

def display_name():
    name = name_entry.get()
    result_label.config(text = "Welcome: " + name)
tk.Button(text = "Submit", command = display_name).pack(pady = 10)
result_label = tk.Label(root, text = "", font = ("Calibri", 14))
result_label.pack(pady = 10)
root.mainloop()
