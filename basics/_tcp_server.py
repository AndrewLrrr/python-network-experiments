import socket


def receive(sock, msg_len):
    msg = ''
    while len(msg) < msg_len:
        chunk = sock.recv(msg_len - len(msg))
        if chunk.strip() == 'close':
            raise RuntimeError('broken')
        msg += chunk
    return msg


def send(sock, msg):
    total_sent = 0
    while total_sent < len(msg):
        sent = sock.send(msg[total_sent:])
        if sent == 0:
            raise RuntimeError('broken')
        total_sent += sent


def start_server(bind_ip, bind_port, msg_len):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(10)

    while True:
        conn, addr = server.accept()
        while True:
            try:
                data = receive(conn, msg_len)
            except RuntimeError:
                break
            try:
                send(conn, data)
            except RuntimeError:
                break
        conn.close()


def main():
    bind_ip = '0.0.0.0'
    bind_port = 2222
    msg_len = 1024
    start_server(bind_ip, bind_port, msg_len)


if __name__ == '__main__':
    main()
