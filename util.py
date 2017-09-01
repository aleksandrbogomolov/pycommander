"""Collect util methods"""
import configparser
import time

def printgreting(username, folder):
    """Print gretings string"""
    print '======================================================='
    print '%s in %s [%s]' % (username, folder, time.strftime("%X"))

def getproperties(key):
    """Getting properties from properties.ini file"""
    config = configparser.ConfigParser()
    config.read('config/properties.ini')
    return config['DEFAULT'][key]
