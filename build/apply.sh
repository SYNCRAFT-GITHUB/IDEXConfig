#!/bin/bash

# bootcmdline

path=/boot/cmdline.txt
content="consoleblank=1 logo.nologo quiet loglevel=1 plymouth.enable=0 vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fastboot noatime nodiratime noram"

if grep -q "rootwait" "$path"; then
    clean=$(grep "rootwait" "$path" | sed 's/\(rootwait\).*$/\1/')
    echo -e "$clean $content" | sudo tee /boot/cmdline.txt
    sudo chmod +x /boot/cmdline.txt
fi

# canbus

content="allow-hotplug can0
iface can0 can static
bitrate 1000000
up ip link set can0 txqueuelen 1024
"

echo -e "$content" | sudo tee /etc/network/interfaces.d/can0

content="[Match]
Type=can

[Link]
TransmitQueueLength=1024
"

echo -e "$content" | sudo tee /etc/systemd/network/10-can.link

content="[Match]
Name=can*

[CAN]
BitRate=1M
"

echo -e "$content" | sudo tee /etc/systemd/network/25-can.network

# packages

install_package() {
    local name="$1"
    sudo apt-get install -qqy $name
}

install_package "udiskie"
install_package "vlc"
install_package "mplayer"

# rclocal

cat rc.local | sudo tee /etc/rc.local
sudo chmod +x /etc/rc.local

# udiskrules

content="ENV{ID_FS_USAGE}==\"filesystem\", ENV{UDISKS_FILESYSTEM_SHARED}=\"1\""

echo $content | sudo tee /etc/udev/rules.d/99-udisks2.rules

# usbsxservice

content="[Unit]
Description=Syncraft USB Mount Service

[Install]
WantedBy=graphical-session.target

[Service]
ExecStart=/usr/bin/udiskie --automount --no-config --notify --tray --appindicator
"

gcodes_dir=/home/pi/printer_data/gcodes

echo -e "$content" | sudo tee /etc/systemd/system/sxusb.service

if [ -d "$gcodes_dir/" ]; then
    sudo rm -rf $gcodes_dir/*
else
    sudo mkdir -p $gcodes_dir
fi

sudo ln -s /media/ $gcodes_dir
sudo mv media USB
mkdir "$gcodes_dir/.JOB"

# xwrapper

xwrapper='allowed_users=anybody
needs_root_rights=yes'

echo -e "$xwrapper" | sudo tee /etc/X11/Xwrapper.config
sudo chmod +x /etc/X11/Xwrapper.config

# copy backups to ..

cp ../backups/SwierVision ..
cp ../backups/variables ..
sudo python3 ../scripts/transfer.py