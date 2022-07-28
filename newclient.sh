#!/bin/bash
name=($HOSTNAME)
#wget -O - https://swupdate.openvpn.net/repos/repo-public.gpg|apt-key add -
#echo "deb http://build.openvpn.net/debian/openvpn/stable focal main" > /etc/apt/sources.list.d/openvpn-aptrepo.list

#sudo apt update && apt upgrade -y

STATUS="$(systemctl is-active openvpn@$name.service)"
NEWSTATUS="$(systemctl is-active openvpn@client.service)"
if [ "${STATUS}" = "active" ] || [ "${NEWSTATUS}" = "active" ]; then
	        echo "Disabling current VPN service for $name or client."
		        sudo systemctl disable openvpn@$name
			        sudo killall openvpn
				        sudo ufw allow 1194/tcp
					        sudo mv /etc/openvpn/client /etc/openvpn/client_old
						        sudo mv /etc/openvpn/*.conf /etc/openvpn/client_old
							    else
								            echo " Service not running.... so exiting "
									            exit 1
fi

sudo apt install openvpn-systemd-resolved -y
tar -xvf /tmp/$name.tar.gz -C /etc/openvpn/
sed -i "s/somename/$name/g" /etc/openvpn/client.conf
sudo systemctl enable openvpn@client.service
sudo systemctl start openvpn@client.service
sudo systemctl is-active openvpn@client.service
