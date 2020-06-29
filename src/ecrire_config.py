import ujson
config = {'ssid':'votre SSID', 'passwd':'votre mot de passe'}
with open('/flash/wifi_config.json', 'w') as fichier:
    ujson.dump(config, fichier)

