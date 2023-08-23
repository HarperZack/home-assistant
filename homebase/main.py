from homebase.appliances import lock
from homebase.appliances import plug
import misc

if __name__ == '__main__':
    print(f'Current active access token is: {6}')

    my_front_door = lock.get_first_lock()
    interface = plug.Plug(misc.interface_id, misc.interface_ip, misc.interface_key)
    monitors = plug.Plug(misc.lp6_id, misc.lp6_ip, misc.lp6_key)
