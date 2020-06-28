import ujson

config = {}
with open('/flash/wifi_config.json') as fichier:
    config = ujson.load(fichier)

print(config)
