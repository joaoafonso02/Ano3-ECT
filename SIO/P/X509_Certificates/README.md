# Mac OS

```bash
python3 validity.py < /usr/local/etc/openssl\@1.1/cert.pem 
```

# Linux
```bash
python3 validity.py < /etc/ssl/certs/*.pem
```

# "Hackear o site da UA" - Search Certificates
```bash
openssl s_client -connect www.ua.pt:443 -showcerts
```

# Noice WebSites

- https://www.alvestrand.no/objectid/2.5.29.19.html
