import sys
import os
import plug


# Returns all plugs, then all locks
def get_all_appliances():
    monitors, interface, extra = plug.get_all_plugs()
    all_plugs = (monitors, interface, extra)

    # all_locks = lock.get_first_lock()
    # return all_plugs, all_locks

    return all_plugs


if __name__ == '__main__':
    monitors, interface, extra = plug.get_all_plugs()
