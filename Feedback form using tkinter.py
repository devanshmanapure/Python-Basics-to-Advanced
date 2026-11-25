#Feedback form using tkinter
import tkinter as tk
root = tk.Tk() #create the main application window

root.title("Student Feedback form")
root.geometry("400x300") #set the window size
#create a heading label
heading = tk.Label(root, text="Student Feedback Form", font=("Arial", 16, "bold"),fg="cyan")
heading.pack(pady=20)
root.mainloop() #start the main event loop