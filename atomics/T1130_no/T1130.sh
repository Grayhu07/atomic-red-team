#!/bin/bash
openssl genrsa -out rootCA.key 4096
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 365 -out rootCA.crt

if [ $(rpm -q --queryformat '%{VERSION}' centos-release) -le "5" ]; then
  cat rootCA.crt >> /etc/pki/tls/certs/ca-bundle.crt
elif [ $(rpm -q --queryformat '%{VERSION}' centos-release) -ge "7" ]; then
  cp rootCA.crt /etc/pki/ca-trust/source/anchors/
  update-ca-trust
fi

