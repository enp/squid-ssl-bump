# Squid HTTPS inspection example

Root (self-signed) certificate required for inspection as first step:

```
openssl req -new -newkey rsa:2048 -sha256 -days 365 -nodes -x509 -extensions v3_ca \
    -subj "/C=RU/ST=Rostov-on-Don/L=Rostov-on-Don/O=ITX/OU=None/CN=itx.ru" \
    -keyout cert.pem -out cert.pem
```

Next step is just run all services (squid, icap filtering daemon and test client):

```
docker-compose up
```
