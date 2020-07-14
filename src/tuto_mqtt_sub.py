import ujson
from m5stack import *
from m5ui import *
import wifiCfg
from m5mqtt import M5mqtt

fichier = open('config.json')
config = ujson.load(fichier)
if not wifiCfg.is_connected():
    lcd.text(10, 10, 'connection au wifi')
    wifiCfg.doConnect(config['ssid'], config['passwd'])

def callback(topic_donnees):
    print((topic_donnees))

m5qtt = M5mqtt("M5stack", "test.mosquitto.org", 1883)
m5qtt.("tuto_topic", callback)

m5qtt.start()

while True:
    pass
