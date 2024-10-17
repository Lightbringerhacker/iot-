'''sudo apt-get update
sudo apt-get upgrade
sudo raspi-config
lsmod | grep spi
sudo apt-get install python3-dev python3-pip
sudo pip3 install spidev
sudo pip3 install mfrc522
pwd
mkdir rfiddemo
cd rfiddemo/
pwd
sudo nano write.py
sudo pyhton3 write.py
pwd
sudo nano read.py
sudo python3 read.py'''

#below is write.py code 
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522

#welcome message
print("Looking for cards")
print("Press Ctrl+c to STOP")

try:
    text=input('enter new data')
    print("now place your tag to write.....")
    reader.write(text)
    print("Data Written Successfully")
finally:
    GPIO.cleanup()

#below is read.py code
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522

#welcome message
print("Looking for cards")
print("Press Ctrl+c to STOP")

try:
    id, text = reader.read()
    print(id)
    print(text)

finally:
    GPIO.cleanup()



#connection
'''
sda = 24
sck = 23
mosi = 19
miso = 21
gnd = 6
rst = 22
3.3v = 1
