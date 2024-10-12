import requests
import os

class Update:
    def __init__(self):
        path = os.path.dirname(__file__)

    def check_version(self):
        response = requests.get("https://github.com/MateusParra/Faltas/raw/refs/heads/main/version.txt")
        new_version = response.text
