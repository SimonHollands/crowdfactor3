import pytest
import urllib.request

def test_api():
    urllib.request.urlopen('http://13.57.217.48/model/breakwater').read().decode('ASCII')
