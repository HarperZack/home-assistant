#!/usr/bin/env python
import sys
sys.path.append('.')

from appliances import lock

if __name__ == '__main__':
    my_front_door = lock.get_first_lock()
    my_front_door.unlock()
