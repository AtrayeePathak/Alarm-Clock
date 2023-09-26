from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer, am_pm):
    while True:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%I:%M:%S %p")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
        time.sleep(1)

def actual_time():
    alarm_hour = hour.get()
    alarm_min = min.get()
    alarm_sec = sec.get()
    am_pm = am_pm_var.get()
    
    # Convert to 24-hour format if needed
    if am_pm == "PM" and alarm_hour != "12":
        alarm_hour = str(int(alarm_hour) + 12)
    elif am_pm == "AM" and alarm_hour == "12":
        alarm_hour = "00"
    
    set_alarm_timer = f"{alarm_hour}:{alarm_min}:{alarm_sec}"
    alarm(set_alarm_timer, am_pm)

clock = Tk()
clock.resizable(width=False, height=False)
clock.geometry('385x130')

Instructions = Label(clock, font=("Arial",10),fg="#FF0000",bg="black", text="Enter time in 24hr format")
Instructions.place(x=0, y = 110, width =385)
Instructions["anchor"] = "center"


# The Variables we require to set the alarm (initialization):
hour = StringVar()
min = StringVar()

# Time required to set the alarm clock:
Hour = Entry(clock, fg="black", bg="#54B646",font=("Arial",15))
Hour.place(x=0,y=80,width=120,height=30)
Minute = Entry(clock, fg="black", bg="#54B646",font=("Arial",15))
Minute.place(x=120,y=80,width=120,height=30)


# To take the time input by user:
SetAlarm = Button(clock, text="Set Alarm")
SetAlarm.place(x=240,y=80, width=147,height=30)
SetAlarm["command"] = actual_time()

clock.mainloop()