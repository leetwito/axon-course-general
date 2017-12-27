import socket
import json
import threading

NAME_TAKEN = 'This name is already taken'
OK = 'OK'
GOODBYE = 'Goodbye :)'

my_ip = '127.0.0.1'
listening_ip = '0.0.0.0' # server's IP
server_port = 3033
server_addr = (listening_ip, server_port)
clients = {} # dictionary contains all the clients. each element is one client. for now I assume only one client
             # in each element we have name as key and tuple-value with commands and next command


def handleIO(commands_list):
    print 'choose command from list:'
    for i in range(len(commands_list)-1):
        print('{}. {}'.format(i, commands_list[i]))
    command_index = raw_input('x to finish')
    if command_index.lower() == 'x':
        return GOODBYE
    return commands_list[command_index]


def handleClient(server):
    conn, address = server.accept() # conn is the socket, address is the client's address
    name = conn.recv(4096)
    name = json.loads(name)
    print name
    if name in clients:
        conn.sendall(json.dumps(NAME_TAKEN))
        conn.close()
        return
    print 'client {} was connected successfully'
    conn.sendall(json.dumps(OK))
    commands = conn.recv(4096)
    commands = json.loads(commands)
    clients[name] = commands # next command initiated to None # next command removed, supports only single client
    while True:
        input_thread = threading.Thread(handleIO, clients[name])  # create object thread
        next_command = input_thread.start()
        # there should be another thread to send next command and receive answer
        if next_command == GOODBYE:
            conn.close()
            print ('{}  from client {}'.format(GOODBYE, name))
            return
        conn.sendall(json.dumps(next_command))
        respone = conn.recv(4096)
        print 'for command {} to client {} got response {}'.format(next_command, name, respone)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(server_addr) # this socket now listens to all of the messages to server_addr
    server.listen(5)
    print 'server is on. listening to {}:{}'.format(*server_addr)
    accepting_thread = threading.Thread(
                                        target=handleClient,
                                        args=(server,)
                                        ) # create object thread
    accepting_thread.start() # start activity



if __name__ == '__main__':
    main()
