#sudo raspi-config
#sudo apt-get update
#sudo apt-get upgrade
#sudo apt-get install build-essential python-dev python-smbus git
#git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
#sudo python setup.py install
#sudo apt-get install python-matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Adafruit_ADS1x15
# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
val = [ ]
# Start continuous ADC conversions on channel 0 using the previous gain value.
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')
fig, ax = plt.subplots()
ax.set_ylim(-5000,5000)
ax.set_title('Oscilloscope')
ax.grid(True)
ax.set_ylabel('ADC outputs')
line, = ax.plot([], 'ro-', label='Channel 0')
ax.legend(loc='lower right')
def update(cnt):
 # Read the last ADC conversion value and print it out.
 value = adc.get_last_result()
 print('Channel 0: {0}'.format(value))
 # Set new data to line
 line.set_data(list(range(len(val))), val)
 ax.relim()
 ax.autoscale_view()
 #Store values for later
 val.append(int(value))
 if(cnt>50):
 val.pop(0)
ani = FuncAnimation(fig, update, interval=500)
plt.show()



#connection
'''vdd = pin 17 (3.3v)
gnd = pin 9 (GND)
scl = pin 5 (GPIO3)
sda = pin 3 (GPIO2)





