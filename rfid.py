#Write
import RPi.GPIO as gp
from mfrc522 import SimpleMFRC522

gp.setwarnings(False)
reader = SimpleMFRC522()

try:
    text = input('New data: ')
    print('Place your card to write...')
    reader.write(text)
    print('Written successfully!')
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    gp.cleanup()
    
#Read
import RPi.GPIO as gp
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print('Place your card to read...')
    id, text = reader.read()
    print(f"ID: {id}")
    print(f"Data: {text}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    gp.cleanup()
