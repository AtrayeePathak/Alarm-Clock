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
clock.title("The Alarm Clock")
clock.geometry("400x250")

time_format = Label(clock, text="Enter time in 12-hour format:", fg="red", bg="black", font="Arial")
time_format.place(x=60, y=150)

addTime = Label(clock, text="Hour  Min   Sec", font=60)
addTime.place(x=110)

setYourAlarm = Label(clock, text="When to wake you up", fg="blue", relief="solid", font=("Helvetica", 7, "bold"))
setYourAlarm.place(x=0, y=29)

# The Variables we require to set the alarm (initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
am_pm_var = StringVar(value="AM")  # Default to AM

# Time required to set the alarm clock:
hourTime = Entry(clock, textvariable=hour, bg="pink", width=15)
hourTime.place(x=110, y=50)
minTime = Entry(clock, textvariable=min, bg="pink", width=15)
minTime.place(x=150, y=50)
secTime = Entry(clock, textvariable=sec, bg="pink", width=15)
secTime.place(x=200, y=50)

# AM/PM dropdown menu
am_pm_dropdown = OptionMenu(clock, am_pm_var, "AM", "PM")
am_pm_dropdown.place(x=280, y=48)

# To take the time input by user:
submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time)
submit.place(x=110, y=100)

clock.mainloop()
