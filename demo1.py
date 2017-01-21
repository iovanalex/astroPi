import time
import datetime
from sense_hat import SenseHat


sense = SenseHat()
sense.clear()
#sense.show_message("UVT 2017")

while True:
	temp_from_temp=sense.get_temperature()
	temp_from_rh=sense.get_temperature_from_humidity()
	temp_from_press=sense.get_temperature_from_pressure()
	print datetime.datetime.now(), round(temp_from_temp,1), round(temp_from_rh,1),round(temp_from_press,1)
	time.sleep(1)
