import tkinter as tk
import datetime
import time
import winsound

def currenttime():
	set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"
	alarm(set_alarm)
def alarm():
	while True:
		alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
		time.sleep(1)
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		if current_time == alarm_time:
			print("hey! it's time to wake up")
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
		

root = tk.Tk()
root.title("alarm clock")
hour = tk.Entry(root, width=4)
hour.pack(side=tk.LEFT)
minute = tk.Entry(root, width=4)
minute.pack(side=tk.LEFT)
second = tk.Entry(root, width=4)
second.pack(side=tk.LEFT)
set_button = tk.Button(root, text="Set Alarm", command=alarm)
set_button.pack()

root.mainloop()