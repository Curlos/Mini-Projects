import socket


def scanForOpenPorts(ip_address, portsRange):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    openPorts = []
    closedPorts = []

    for port in range(portsRange[0], portsRange[1] + 1):
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            openPorts.append(port)
        else:
            closedPorts.append(port)
        sock.close()
    return f"Open ports: {openPorts}\nClosed ports: {closedPorts}"


# Port shows as open if being used at the time the program is ran
# For example, if a react app or backend server is running on the local hosts port then it will show as open
print(scanForOpenPorts('127.0.0.1', (3000, 3005)))
