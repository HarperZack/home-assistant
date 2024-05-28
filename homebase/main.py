from homebase.appliances import lock
from homebase.appliances import plug
import restricted

if __name__ == '__main__':
    # my_front_door = lock.get_first_lock()
    monitors = plug.Plug(restricted.LP6_ID, restricted.LP6_IP, restricted.LP6_KEY)
    interface = plug.Plug(restricted.INTERFACE_ID, restricted.INTERFACE_IP, restricted.INTERFACE_KEY)
    extra = plug.Plug(restricted.EXTRA_ID, restricted.EXTRA_IP, restricted.EXTRA_KEY)
