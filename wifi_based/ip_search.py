from pythonping import ping
import restricted


def get_device_activity():
    time_out_phrase = 'Request timed out'
    active = []
    inactive = []

    for address in restricted.ip_addresses_by_phone:
        try:
            status = ping(restricted.ip_addresses_by_phone[address], timeout=.75)
            reports = list(status)
            did_timeout = False
            for report in reports:
                if time_out_phrase in str(report):
                    did_timeout = True
                if time_out_phrase in str(report) and did_timeout is True:
                    inactive.append(address)
                    break
                else:
                    active.append(address)
                    break
        except RuntimeError as e:
            print('Catch-all for time out error, however error thrown was: ' + e)
            inactive.append(address)
    return active, inactive


def get_device_name(ip):
    ip_keys = list(restricted.ip_addresses_by_phone.keys())
    ip_search_value = list(restricted.ip_addresses_by_phone.values()).index(ip)
    name = ip_keys[ip_search_value]

    return name


active_devices, inactive_devices = get_device_activity()


if __name__ == '__main__':
    test_on = ping(restricted.EXTRA_IP)
    test_off = ping('192.168.1.77')
