import plug
import lock


def get_all_appliances():
    monitors, interface, wireless = plug.get_all_plugs()
    my_door = lock.get_my_front_door()

    return my_door, monitors, interface, wireless


if __name__ == '__main__':
    front_door, monitors, interface, wireless = get_all_appliances()
