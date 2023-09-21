import tkinter as tk
from tkinter import messagebox
import datetime
import time
import winsound

def set_alarm():
    alarm_time = entry_alarm_time.get()
    try:
        alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format.")
        return

    current_time = datetime.datetime.now()
    while current_time < alarm_time:
        current_time = datetime.datetime.now()
        time.sleep(1)

    winsound.Beep(500, 1000)  # Beep sound when the alarm goes off
    messagebox.showinfo("Alarm", "Time to wake up!")

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create and place GUI elements
label_instructions = tk.Label(root, text="Enter alarm time (HH:MM):")
label_instructions.pack()

entry_alarm_time = tk.Entry(root)
entry_alarm_time.pack()

button_set_alarm = tk.Button(root, text="Set Alarm", command=set_alarm)
button_set_alarm.pack()

root.mainloop()
