import pytest
import urllib.request
import requests
from Surf_counter.spot_urls import SpotUrls

def test_first_link():
    spots=['breakwater','topanga']
    for spot in spots:
        camrewind_link=SpotUrls.lookup[spot]
        page = requests.get(camrewind_link)

            