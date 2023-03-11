#!/usr/bin/env python
from homebase.appliances import plug
import homebase.misc as misc

if __name__ == '__main__':
    monitors = plug.Plug(misc.lp6_id, misc.lp6_ip, misc.lp6_key)
    monitors.turn_on_or_off()
