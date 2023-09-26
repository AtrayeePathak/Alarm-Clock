import tkinter as tk
import datetime
from time import strftime, sleep
import winsound

set_alarm_timer = ""

def update():
    time_string = strftime("%I:%M:%S %p")
    timeLabel.config(text=time_string)

    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%d/%m/%Y")

    if now == set_alarm_timer:
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC) 
    
    timeLabel.after(1000, update)   
    # recursion for continuous update

def alarm(set_alarm_timer):
  while True:
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%d/%m/%Y")
    print("The Set Date is:", date)
    print(now)
    time_string = strftime("%I:%M:%S %p")
    timeLabel.config(text=time_string)
    if now == set_alarm_timer:
      print("Time to Wake up")
      winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
      break
    sleep(1)


def actual_time():
    global set_alarm_timer
    alarm_hour = Hour.get()
    alarm_min = Minute.get()
    am_pm = AM_PM.get()  # Get the selected AM/PM value

    alarm_hour = alarm_hour.zfill(2)
    alarm_min = alarm_min.zfill(2)

    # Convert to 24-hour format
    if am_pm == "PM" and alarm_hour != "12":
        alarm_hour = str(int(alarm_hour) + 12)
    elif am_pm == "AM" and alarm_hour == "12":
        alarm_hour = "00"

    set_alarm_timer = f"{alarm_hour}:{alarm_min}:00"
    alarm(set_alarm_timer)

clock = tk.Tk()
clock.resizable(width=False, height=False)
clock.geometry('385x160')  # Adjust the window height

timeLabel = tk.Label(clock, font=("Arial", 50), fg="#FF0000", bg="black")
timeLabel.place(x=0, y=0, width=385, height=80)
timeLabel["anchor"] = "center"

Instructions = tk.Label(clock, font=("Arial", 10), fg="#FF0000", bg="black", text="Enter time in 12hr format")
Instructions.place(x=0, y=140, width=385)
Instructions["anchor"] = "center"

Hour = tk.StringVar()
Minute = tk.StringVar()
AM_PM = tk.StringVar()

Hour = tk.Entry(clock, fg="black", bg="#54B646", font=("Arial", 15))
Hour.place(x=0, y=80, width=120, height=30)
Minute = tk.Entry(clock, fg="black", bg="#54B646", font=("Arial", 15))
Minute.place(x=120, y=80, width=120, height=30)

# Dropdown menu for AM/PM
am_pm_choices = ["AM", "PM"]
am_pm_menu = tk.OptionMenu(clock, AM_PM, *am_pm_choices)
am_pm_menu.config(font=("Arial", 12))
am_pm_menu.place(x=250, y=80, width=60, height=30)

SetAlarm = tk.Button(clock, text="Set Alarm", command=actual_time)
SetAlarm.place(x=320, y=80, width=65, height=30)

update()
clock.mainloop()
