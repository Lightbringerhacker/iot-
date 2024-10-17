import tkinter as tk
import RPi.GPIO as gp

gp.setwarnings(False)
gp.setmode(gp.BOARD)
led=7
fan=8
ac=10
gp.setup(led,gp.OUT)
gp.setup(fan,gp.OUT)
gp.setup(ac,gp.OUT)

def ON_Bulb(): 
 print(var1.get())	
 if var1.get():
	 gp.output(led, False)
	 
	 
 
 else:
		gp.output(led,True)
		 
def ON_FAN(): 
 print(var2.get())	
 if var2.get():
	 gp.output(fan, False)
	 
	 
 
 else:
		gp.output(fan,True)
		  
def ON_AC(): 
 print(var3.get())	
 if var3.get():
	 gp.output(ac, False)
	 
	 
 
 else:
		gp.output(ac,True)
 

root=tk.Tk()
var1=tk.BooleanVar()
var2=tk.BooleanVar()
var3=tk.BooleanVar()
togglebulb=tk.Checkbutton(root,text="Toggle for LED", variable=var1, command=ON_Bulb)
toggleFan=tk.Checkbutton(root,text="Toggle for Fan", variable=var2, command=ON_FAN)
toggleAC=tk.Checkbutton(root,text="Toggle for AC", variable=var3, command=ON_AC)

togglebulb.pack(pady=10)
toggleFan.pack(pady=30)
toggleAC.pack(pady=0)

root.mainloop()
gp.cleanup()
