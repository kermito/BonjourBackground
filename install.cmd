@echo off
python -m pip install --upgrade pip setuptools
python -m pip install django
pip install Image
pip install bs4
pip install pyinstaller
pyinstaller BonjourBackground.spec -y
