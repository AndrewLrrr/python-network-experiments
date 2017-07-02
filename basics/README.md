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
[*] Accepted connection from: 127.0.0.1:59279
[*] Received: GET / HTTP/1.1
Host: localhost

Body of request
```

### Replacing Netcat (netcat.py)
_First terminal_
```
/Path/To/File/netcat.py -l -p 9999 -c
```
_Second terminal_
```
/Path/To/File/netcat.py -t localhost -p 9999
<CTRL-D>
<BHP:#>  pwd
/Some/Path
```

### TCP Proxy (proxy.py)
_Terminal_
```
sudo python proxy.py [localhost] 80 [remotehost] 80 False
```
Open browser or curl for example and try to connect your localhost on port 80.