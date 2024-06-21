import json


class Settings:

    def __init__(self):
        self.settings = json.load("settings.json")
        print(self.settings)
