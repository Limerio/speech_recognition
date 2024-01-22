import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}


class ElgatoApi():
    def __init__(self, url: str):
        self.url = url

    def turn_off(self):
        data = '{"numberOfLights": 1,"lights": [{"on": 0}]}'
        response = requests.put(
            f'http://{self.url}:9123/elgato/lights', headers=headers, data=data)

        return response.json()

    def turn_on(self):
        data = '{"numberOfLights": 1,"lights": [{"on": 1}]}'
        response = requests.put(
            f'http://{self.url}:9123/elgato/lights', headers=headers, data=data)

        return response.json()
