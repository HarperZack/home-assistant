import tinytuya
import tuyapower
# The tuyapower pypi entry has some fixes; follow that if it's still weird. Issues with Crypto module not installing
# properly. Just install individually or uninstall things and it works fine

from pprint import pprint as pp
import homebase.restricted as restricted


class Plug:
    # https://pypi.org/project/tinytuya/
    # Go there and everything will make sense. Use the wizard and get data from there. You will need your
    # API Key (Access ID/Client ID)
    # Secret (Access Secret/Client Secret)
    # and region (US West apparently?)
    # THESE IDS AND IPS ARE DIFFERENT THAN THE TUYA WEBSITE GIVES YOU BECAUSE IT IS NOW PAYWALLED, I think...

    # https://platform.tuya.com/cloud/basic?id=p1716553590504gvvg85&toptab=project
    # Go here to get the data and register the plugs and such

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


if __name__ == '__main__':
    extra_plug = Plug(restricted.EXTRA_ID, restricted.EXTRA_IP, restricted.EXTRA_KEY)
    interface = Plug(restricted.INTERFACE_ID, restricted.INTERFACE_IP, restricted.INTERFACE_KEY)
    monitors = Plug(restricted.LP6_ID, restricted.LP6_IP, restricted.LP6_KEY)

