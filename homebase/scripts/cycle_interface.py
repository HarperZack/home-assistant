#!/usr/bin/env python
from homebase.appliances import plug
import homebase.restricted as restricted

if __name__ == '__main__':
    interface = plug.Plug(restricted.INTERFACE_ID, restricted.INTERFACE_IP, restricted.INTERFACE_KEY)
    interface.turn_on_or_off()
