#!/usr/bin/env bash
sudo apt-get install python-tk python-pip
sudo python -m pip install --upgrade pip setuptools
sudo python -m pip install django
sudo pip install Image
sudo pip install bs4
sudo pip install pyinstaller
pyinstaller BonjourBackground.spec -y
