import time
import configparser

def printgreting(username, folder):
    print('=======================================================')
    print('%s in %s [%s]' % (username, folder, time.strftime("%X")))

def getproperties(key):
    config = configparser.ConfigParser()
    config.read('config/properties.ini')
    return config['DEFAULT'][key]
