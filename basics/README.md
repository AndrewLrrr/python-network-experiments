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
_First terminal_
```
python proxy.py [localhost] 9000 [remotehost] 80 False
```
_Second terminal_
```
telnet 127.0.0.1 9000
[...]
GET / HTTP/1.1
Host: [remotehost]
Accept-Encoding: identity
Cache-Control: no-cache
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36



```
