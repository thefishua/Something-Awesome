#!/bin/bash
if [ $EUID -ne 0 ]; then
	echo "You must use sudo to run this script:"
	echo "sudo $0 $@"
	exit
fi
apt-get update
apt-get upgrade -y
apt-get install rpi-update
BRANCH=next rpi-update c053625

## dwc2 drivers
sed -i -e "\$adtoverlay=dwc2" /boot/config.txt

##Install git and download rspiducky
wget --no-check-certificate https://raw.githubusercontent.com/ossiozac/Raspberry-Pi-Zero-Rubber-Ducky-Duckberry-Pi/master/LICENSE https://raw.githubusercontent.com/ossiozac/Raspberry-Pi-Zero-Rubber-Ducky-Duckberry-Pi/master/duckpi.sh https://github.com/ossiozac/Raspberry-Pi-Zero-Rubber-Ducky-Duckberry-Pi/raw/master/g_hid.ko https://github.com/ossiozac/Raspberry-Pi-Zero-Rubber-Ducky-Duckberry-Pi/raw/master/hid-gadget-test https://github.com/ossiozac/Raspberry-Pi-Zero-Rubber-Ducky-Duckberry-Pi/raw/master/hid-gadget-test.c https://github.com/ossiozac/Raspberry-Pi-Zero-Rubber-Ducky-Duckberry-Pi/raw/master/readme.md https://github.com/ossiozac/Raspberry-Pi-Zero-Rubber-Ducky-Duckberry-Pi/raw/master/usleep https://github.com/ossiozac/Raspberry-Pi-Zero-Rubber-Ducky-Duckberry-Pi/raw/master/usleep.c

##Make all nessisary files executeable
cd /home/pi
chmod 755 hid-gadget-test.c duckpi.sh usleep.c g_hid.ko usleep hid-gadget-test

\cp g_hid.ko /lib/modules/4.4.0+/kernel/drivers/usb/gadget/legacy

cat <<'EOF'>>/etc/modules
dwc2
g_hid
EOF

##Make it so that you can put the payload.dd in the /boot directory
sed -i '/exit/d' /etc/rc.local

cat <<'EOF'>>/etc/rc.local
sleep 3
cat /boot/payload.dd > /home/pi/payload.dd
sleep 1
tr -d '\r' < /home/pi/payload.dd > /home/pi/payload2.dd
sleep 1
/home/pi/duckpi.sh /home/pi/payload2.dd
exit 0
EOF

##Making the first payload
cat <<'EOF'>>/boot/payload.dd
GUI r
DELAY 50
STRING www.youtube.com/watch?v=dQw4w9WgXcQ
ENTER
EOF
