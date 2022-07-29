#!/bin/bash
for hostvar in $(cat hosts.txt); do
client_hosts=$hostvar
    echo $client_hosts
    rm -v /home/tonyhuy/client/!("ca.crt"|"tls-auth.key")
    cp /home/tonyhuy/openvpn_certs/certs/issued/$client_hosts.crt /home/tonyhuy/client/
    cp /home/tonyhuy/openvpn_certs/certs/private/$client_hosts.key /home/tonyhuy/client/
    tar -cvf /home/tonyhuy/tar_packages/$client_hosts.tar.gz /home/tonyhuy/client.conf /home/tonyhuy/client
    mv $client_hosts.tar.gz /tmp/; 
done
