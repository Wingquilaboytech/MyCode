import sys #to import system files
from tkinter import *   #whole module is imported
import time #importing local time
#Used to display time on the label
def DClock():
    curr_time= time.strftime("%H:%M:%S")
    clock.config(text=curr_time)
    clock.after(100,DClock)
#making window
window=Tk()
window.title('Digital Clock') #adding title to the window
#giving name to our digital clock and styling it
message= Label(window,background="red", font=("calibri",100,"italic"),  text="Time", fg="Blue")
message.grid(row=0,column=0)
clock= Label(window, font=("times",150,"bold"),fg="Orange")
clock.grid(row=1,column=0)
DClock()
mainloop() #loop is closed