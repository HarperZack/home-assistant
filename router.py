import nmap
import misc


def whos_online():
    online = []
    scanner = nmap.PortScanner()
    for person in misc.people:
        scan = scanner.scan(hosts=misc.people[person])
        online_bits = scan['scan']
        # Comes back as JSON with either entry or not; doesn't want to be False/empty though.
        if len(online_bits) > 0:
            print(online_bits)
            online.append(person)
    if online is False:
        return None
    else:
        return online


if __name__ == '__main__':
    print(whos_online())

