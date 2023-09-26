import tkinter as tk
import datetime
from time import *
import winsound

set_alarm_timer = 0

def update():
    time_string = strftime("%I:%M:%S %p")
    timeLabel.config(text=time_string)

    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%d/%m/%Y")

    if (now == set_alarm_timer):
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC) 
    
    timeLabel.after(1000, update) #recursion for continuous update

def alarm(set_alarm_timer):
    while False:
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
    alarm_hour = Hour.get()
    alarm_min = Minute.get()

    alarm_hour.zfill(2)
    alarm_min.zfill(2)
    #No need for conversion if we use 24 hour clock
    
    set_alarm_timer = f"{alarm_hour}:{alarm_min}:00"
    alarm(set_alarm_timer)


clock = tk.Tk()
clock.resizable(width=False, height=False)
clock.geometry('385x130')

timeLabel = tk.Label(clock, font=("Arial",50),fg="#FF0000",bg="black")
timeLabel.place(x=0,y=0,width=385, height=80)
timeLabel["anchor"] = "center"

Instructions = tk.Label(clock, font=("Arial",10),fg="#FF0000",bg="black", text="Enter time in 24hr format")
Instructions.place(x=0, y = 110, width =385)
Instructions["anchor"] = "center"


# The Variables we require to set the alarm (initialization):
hour = tk.StringVar()
min = tk.StringVar()

# Time required to set the alarm clock:
Hour = tk.Entry(clock, fg="black", bg="#54B646",font=("Arial",15))
Hour.place(x=0,y=80,width=120,height=30)
Minute = tk.Entry(clock, fg="black", bg="#54B646",font=("Arial",15))
Minute.place(x=120,y=80,width=120,height=30)


# To take the time input by user:
SetAlarm = tk.Button(clock, text="Set Alarm")
SetAlarm.place(x=240,y=80, width=147,height=30)
SetAlarm["command"] = actual_time()

update()
clock.mainloop()