import telepot
import tkinter as tk
import RPi.GPIO as gp
import time
from telepot.loop import MessageLoop

#botfather
#userinfobot

token='7398022570:AAGwuzze6VLXr51E42YJCHhBD-zalogs'
bot=telepot.Bot(token)
chat_id='1717886'
gp.setmode(gp.BOARD)
led = 7
gp.setup(led,gp.OUT)

def On_Click():
    msg="LED IS ON"
    gp.output(led,True)
    time.sleep(2)
    bot.sendMessage(chat_id,msg)
    url=f"https://api.telegram.org/bot7398022570:AAGwuzze6VLXr51E42YJCHhBD-zalogs/sendMessage"


def Off_Click():
    msg="LED IS OFF"
    gp.output(led,False)
    time.sleep(2)
    bot.sendMessage(chat_id,msg)
    url=f"https://api.telegram.org/bot7398022570:AAGwuzze6VLXr51E42YJCHhBD-zalogs/sendMessage"


root=tk.Tk()
OnButton=tk.Button(root,text="On",width=10,height 2,command=On_Click)
OfButton-tk.Button(root,text="Off",width=10,height=2,command=Off_Click)
OnButton.pack(pady=10)
OfButton.pack(pady=10)
root.mainloop()
gp.cleanup(True)
gp.cleanup()
