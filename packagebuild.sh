#!/bin/bash

read -p 'hostname: ' hostvar
echo $hostvar

rm -v /home/tonyhuy/client/!("ca.crt"|"tls-auth.key")
cp /home/tonyhuy/openvpn_certs/certs/issued/$hostvar.crt /home/tonyhuy/client/
cp /home/tonyhuy/openvpn_certs/certs/private/$hostvar.key /home/tonyhuy/client/
tar -cvf /home/tonyhuy/tar_packages/$hostvar.tar.gz /home/tonyhuy/client.conf /home/tonyhuy/client
mv $hostvar.tar.gz tar_packages/
