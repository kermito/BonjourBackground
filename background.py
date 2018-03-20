#!/usr/bin/env python
from PIL import Image
import sys
import getopt
import bs4 as BeautifulSoup
import pprint
import os
import urllib
import os.path
import platform
import argparse
try:
    from PIL import Image
    from PIL import ImageFile
except ImportError:
    import Image
    import ImageFile
try:
	import urllib
except Exception:
	import urllib.request

def parseArgs():
    parser = argparse.ArgumentParser(description='Sexy girl in background')
    parser.add_argument('--folder' ,help='Folder where picture are saved')
    return parser


#getting the picture
def getBackgound(page):
    soup = BeautifulSoup.BeautifulSoup(page, "html.parser")
    imageItem = soup.find("div",attrs={"class":"photo"}).find("img")
    return(imageItem['src'])


#Os background application
def setGnomeBackground(imagePath):
	os.system("gsettings set org.gnome.desktop.background draw-background false;")
	command = 'gsettings set org.gnome.desktop.background picture-uri "'+imagePath+'"'
	os.system(command)
	os.system("gsettings set org.gnome.desktop.background draw-background true;")


def setWindowsBackground(imagePath):
	import ctypes
	import win32con
	ok = ctypes.windll.user32.SystemParametersInfoA(20, 0, imagePath, 0)
	command = 'reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d ' + imagePath + ' /f'
	ok = os.system(command)
	os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")
	return ok


def main(argv):
    system = platform.system()
    if system == "Windows":
        DS = "\\"
    elif system  == 'Linux':
        DS = "/"

    if argv.folder is not None and os.path.isdir(argv.folder):
        root = argv.folder
        pass
    else:
        root = os.path.abspath(os.path.dirname(__file__))
        pass

    #getting some sexy page
    try:
    	content = urllib.urlopen("http://dites.bonjourmadame.fr/").read()
    except Exception:
    	content = urllib.request.urlopen("http://dites.bonjourmadame.fr/").read()
    url = getBackgound(content)
    basePath = root + DS + "Image.jpg"
    #Downloading the sexy girl
    try:
    	content = urllib.request.urlretrieve(url, basePath)
    except Exception:
    	content = urllib.urlretrieve(url, basePath)
    print(basePath)
    bmpPath = root + DS + "Image.bmp"
    Image.open(basePath).save(bmpPath)
    if system == "Windows":
    	result = setWindowsBackground(bmpPath)
    elif system  == 'Linux':
    	result = setGnomeBackground(bmpPath)
    	pass

if __name__ == "__main__":
    parser = parseArgs()
    args = parser.parse_args()
    main(args)
