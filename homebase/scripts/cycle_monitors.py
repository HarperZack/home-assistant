#!/usr/bin/env python
from homebase.appliances import plug
import homebase.restricted as restricted

if __name__ == '__main__':
    monitors = plug.Plug(restricted.LP6_ID, restricted.LP6_IP, restricted.LP6_KEY)
    monitors.turn_on_or_off()
