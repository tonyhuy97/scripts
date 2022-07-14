#!/bin/bash
name=($HOSTNAME)
#wget -O - https://swupdate.openvpn.net/repos/repo-public.gpg|apt-key add -
#echo "deb http://build.openvpn.net/debian/openvpn/stable focal main" > /etc/apt/sources.list.d/openvpn-aptrepo.list

#sudo apt update && apt upgrade -y

STATUS="$(systemctl is-active openvpn@client.service)"
if [ "${STATUS}" = "active" ]; then
        echo "Disabling current VPN service for $name"
        sudo systemctl disable openvpn@$name
        sudo mv /etc/openvpn/client /etc/openvpn/client_old
        sudo mv /etc/openvpn/*.conf /etc/openvpn/client_old
    else
        echo " Service not running.... so exiting "
        exit 1
fi

sudo apt install openvpn-systemd-resolved -y
tar -xvf /tmp/$name.tar.gz -C /etc/openvpn/
sed -i "s/somename/$name/g" /etc/openvpn/client.conf
sudo systemctl enable openvpn@client
sudo systemctl start openvpn@client
sudo systemctl is-active openvpn@client

