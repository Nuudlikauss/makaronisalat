#!/bin/bash

apt update && apt upgrade -y

if [ -f /var/run/reboot-required ]; then
  echo 'reboot required!'

  # Ask if user wants to reboot system
  read -p "Do you want to reboot your system (y/n):" choice
  if [$choice == 'y']; then
       	echo "Rebooting your system in a minute!"
       	sleep 1
	reboot
  else 
	  echo "Reboot canceled"
  fi

else
	echo 'reboot not required'
fi



