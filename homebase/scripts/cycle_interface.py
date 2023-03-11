#!/usr/bin/env python
from homebase.appliances import plug
import homebase.misc as misc

if __name__ == '__main__':
    interface = plug.Plug(misc.interface_id, misc.interface_ip, misc.interface_key)
    interface.turn_on_or_off()
