import socket
import json

MY_NAME = {'name': 'Lee Computer'}

UNKNOWN_COMMAND = 'Unknown command'
ALL = 'All'
OK = 'OK'
GOODBYE = 'Goodbye'

server_ip = '127.0.0.1'
port = 3033
server_addr = (server_ip, port) # server address must be tuple

COMMANDS = {}

def getOS():
    import platform
    return platform.platform()
COMMANDS['OS_TYPE'] = getOS
#
#
# def loggedUsers():
#
# COMMANDS['LOGGED_USERS'] = loggedUsers
#
#
# COMMANDS['RUNNING_PROCESSES'] = runningProcesses
# COMMANDS['OPEN_PORTS'] = openPorts
# COMMANDS['STORAGE_USAGE'] = storageUsage
# COMMANDS['GPU_TYPE'] = GPUType


def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # open socket from TCP/IP type
    print('Trying to connect to server...')
    client.connect(server_addr)
    print('Connected')

    print('Sending my name...')
    client.sendall(json.dumps(MY_NAME))
    response = client.recv(4096)
    if response != OK:
        return
    print('Sent and accepted')

    client.sendall(json.dumps(COMMANDS.keys()))
    response = client.recv(4096)
    while response != GOODBYE:
        client.sendall(json.dumps(COMMANDS[response]()))
        response = client.recv(4096)



    print ('Closing connection...')
    client.close()


if __name__ == '__main__':
    main()
    # print(getOS())