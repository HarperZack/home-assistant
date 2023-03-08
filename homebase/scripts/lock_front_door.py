#!/usr/bin/env python
from homebase.appliances import lock

if __name__ == '__main__':
    my_front_door = lock.get_first_lock()
    my_front_door.lock()
