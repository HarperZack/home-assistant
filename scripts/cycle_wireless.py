#!/usr/bin/env python
import sys
sys.path.append('.')

from appliances import plug
import restricted

if __name__ == '__main__':
    wireless = plug.Plug(restricted.WIRELESS_ID, restricted.WIRELESS_IP, restricted.WIRELESS_KEY)
    wireless.turn_on_or_off()
