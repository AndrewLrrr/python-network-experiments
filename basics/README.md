### Simple UDP client (udp_client.py)
_First terminal_
```
nc localhost -u 3000 -l
```
_Second terminal_
```
python ./udp_client.py
```
_First terminal_
```
AAABBBCCC
```

### Simple TCP client (tcp_client.py)
_First terminal_
```
nc 3000 -l
```
_Second terminal_
```
python ./tcp_client.py
```
_First terminal_
```
GET / HTTP/1.1
Host: localhost

Body of request
```

### Simple TCP server (tcp_server.py)
_First terminal_
```
python ./tcp_server.py

[*] Listening on 0.0.0.0:3000
```
_Second terminal_
```
python ./tcp_client.py

ACK!
```
_First terminal_
```
[*] Received: GET / HTTP/1.1
Host: localhost

Body of request
```

### Replacing Netcat (netcat.py)