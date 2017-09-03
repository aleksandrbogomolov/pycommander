"""Collect util methods"""
import time

import configparser


def print_greetings(username, folder):
    """Print greetings string"""
    delitim = "======================================================="
    print delitim
    print '%s in %s [%s]' % (username, folder, time.strftime("%X"))
    print delitim


def get_properties(key):
    """Getting properties from properties.ini file"""
    config = configparser.ConfigParser()
    config.read('config/properties.ini')
    return config['DEFAULT'][key]
