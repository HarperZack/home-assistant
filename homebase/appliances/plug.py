import tinytuya
import tuyapower
from pprint import pprint as pp


class Plug:
    # Key is difficult to find. Follow this video; link devices as needed: https://www.youtube.com/watch?v=Q1ZShFJDvE0
    # Follow any google guide to get ip and id; those all still work and are quick
    def __init__(self, id, ip, key, version='3.3'):
        self.id = id
        self.ip = ip
        self.key = key
        self.version = version

    def turn_on_or_off(self):
        socket = tinytuya.OutletDevice(self.id, self.ip, self.key, version=self.version)
        is_on = tuyapower.deviceJSON(self.id, self.ip, self.key, self.version).split(',')[1]
        if 'True' in is_on:
            socket.turn_off()
        elif 'False' in is_on:
            socket.turn_on()

    def print_status(self):
        pp(tinytuya.OutletDevice(self.id, self.ip, self.key, version=self.version))
