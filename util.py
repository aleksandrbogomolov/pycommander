"""Collect util methods"""
import configparser
import time


def printGreting(username, folder):
    """Print gretings string"""
    delitim = "======================================================="
    print delitim
    print '%s in %s [%s]' % (username, folder, time.strftime("%X"))
    print delitim


def getProperties(key):
    """Getting properties from properties.ini file"""
    config = configparser.ConfigParser()
    config.read('config/properties.ini')
    return config['DEFAULT'][key]
