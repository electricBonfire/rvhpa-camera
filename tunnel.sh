#!/bin/bash
if [ ! -f /proc/$(cat /home/pi/tunnel.pid)/status ]; then
	nohup autossh -M 20000 -R 8022:localhost:22 pi-camera@northrop.io -N > /dev/null 2>&1 &
	echo $! > /home/pi/tunnel.pid
fi