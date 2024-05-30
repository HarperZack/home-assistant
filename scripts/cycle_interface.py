#!/usr/bin/env python
import sys
sys.path.append('.')

from appliances import plug
import restricted

if __name__ == '__main__':
    interface = plug.Plug(restricted.INTERFACE_ID, restricted.INTERFACE_IP, restricted.INTERFACE_KEY)
    interface.turn_on_or_off()
