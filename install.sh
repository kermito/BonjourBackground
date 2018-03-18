#!/usr/bin/env bash
sudo apt-get install python-pip
sudo python -m pip install --upgrade pip setuptools
sudo python -m pip install django
sudo pip install Image
sudo pip install bs4

FOLDER= pwd
echo "[Desktop Entry]\nType=Application\nName=BonjourBackground\nExec=\"python $FOLDER/background.py\"\nIcon=\"\"\nComment=\"Every day a new background\"\nX-GNOME-Autostart-enabled=true" >> ~/.config/autostart/BonjourBackground.desktop
