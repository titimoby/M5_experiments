import ujson
config = {
    'ssid':'votre SSID', 
    'passwd':'votre mot de passe'
    'openweathermapApiKey': 'votre api key'
    }
with open('/flash/config.json', 'w') as fichier:
    ujson.dump(config, fichier)

