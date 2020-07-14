import ujson

config = {}
with open('/flash/config.json') as fichier:
    config = ujson.load(fichier)

print(config)
