#!/usr/bin/env python
import sys
sys.path.append('.')

from appliances import plug
import restricted

if __name__ == '__main__':
    wireless = plug.Plug(restricted.EXTRA_ID, restricted.EXTRA_IP, restricted.EXTRA_KEY)
    wireless.turn_on_or_off()
