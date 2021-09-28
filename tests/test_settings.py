import sys
import os
from PyQt5 import QtCore

def test_settings():
    settings = QtCore.QSettings('Math-Magik', 'Designer')
    print(settings.fileName())
    settings.setValue('mainWindowWidth', 640)
    settings.setValue('mainWindowHeight', 480)
    keys = settings.allKeys()
    print(keys)
    assert 'mainWindowWidth' in keys
    assert 'mainWindowHeight' in keys

