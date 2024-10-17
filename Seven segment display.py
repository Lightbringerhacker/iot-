import RP1.GPIO as gp
import time
from tm1637 import TM1637

gp.setwarnings(False)

#Define the GPIO pins for CLK and 010
clk = 17 #Clock pin
dio = 4 #Data pin

#Create a TM1637 object
display = TM1637(clk, dio)

#Function to display the time
def display_time():
    current_time = time.strftime("%H%M") #Get hours and minutes in HHMM
    display.number(int(current_time))
    time.sleep(1) #Update every second
    print("Displayang....")
    print(current_time)

try:
    for i in range(50):
        display_time()
except KeyboardInterrupt:
    print("Exiting...")
finally:
    display.clear() #Clear the display before exiting
    gp.cleanup()
