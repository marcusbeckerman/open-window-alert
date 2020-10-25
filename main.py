import serial
from urllib.request import urlopen
import json
from win10toast import ToastNotifier
from time import sleep

n = ToastNotifier()

# Weather
open_weather_map_key = 'Get an API key at openweathermap.org'
city = 'San Marcos'
state = 'ca'
country = 'US'
units = 'imperial' # imperial or metric
maxtemp = 75 # This is default for imperial units

# Serial
serialport = 'COM3'
baudrate = 9600

url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&APPID={open_weather_map_key}&units={units}'


while True:
    response = urlopen(url)
    outsidetemp = json.loads(response.read().decode())['main']['temp']

    roomtemp = float(str(serial.Serial(port=serialport, baudrate=baudrate).readline())[2:-5])

    if roomtemp > outsidetemp and roomtemp > maxtemp:
        n.show_toast(title='Open a window!', msg=f'Your room is {roomtemp}°, while outside temp is only {outsidetemp}°. Open a window and cool off!', threaded=True, duration=600)
        while n.notification_active():
            sleep(0.1)
    sleep(5)


