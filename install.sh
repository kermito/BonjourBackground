#!/usr/bin/env bash
# sudo apt-get install python-pip
# sudo python -m pip install --upgrade pip setuptools
# sudo python -m pip install django
# sudo pip install Image
# sudo pip install bs4


# Check autostart folder
DIRECTORY=~/.config/autostart/
if [ ! -d "$DIRECTORY" ]; then
  mkdir $DIRECTORY
fi

FOLDER=$(pwd)
printf "[Desktop Entry]\n" > ~/.config/autostart/BonjourBackground.desktop
printf "Type=Application\n" >> ~/.config/autostart/BonjourBackground.desktop
printf "Name=BonjourBackground\n" >> ~/.config/autostart/BonjourBackground.desktop
printf "Exec=python %s/background.py\n" "$FOLDER" >> ~/.config/autostart/BonjourBackground.desktop
printf "Icon=%s/icon.png\n" "$FOLDER" >> ~/.config/autostart/BonjourBackground.desktop
printf "Comment=Every day a new background\n" >> ~/.config/autostart/BonjourBackground.desktop
printf "X-GNOME-Autostart-enabled=true\n" >> ~/.config/autostart/BonjourBackground.desktop
# > ~/.config/autostart/BonjourBackground.desktop
