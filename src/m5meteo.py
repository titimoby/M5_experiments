import ujson
from m5stack import *
from m5ui import *
import wifiCfg
import urequests

lcd.clear()

fichier = open('config.json')
config = ujson.load(fichier)
if not wifiCfg.is_connected():
    lcd.println('connection au wifi')
    wifiCfg.doConnect(config['ssid'], config['passwd'])
# req = urequests.get('http://api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={your api key}')
req = urequests.get('http://api.openweathermap.org/data/2.5/weather?q=Lyon&appid=' + config['openweathermapApiKey'] + '&units=metric')
meteo = req.json()

lcd.clear()
lcd.font(lcd.FONT_DejaVu40)
lcd.text(10,10,"meteo")
lcd.text(20, 45, meteo['weather'][0]['description'])
lcd.text(50, 120, "temperature")
lcd.text(80, 155, str(meteo['main']['temp']))

fichier.close()
