#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import Tk, Label, Button, PhotoImage, BOTTOM
from PIL import Image
import bs4 as BeautifulSoup
import os
import urllib
import os.path
import platform
import argparse


def parseArgs():
    parser = argparse.ArgumentParser(description='Sexy girl in background,'
                                                 ' no params for GUI')
    parser.add_argument('--folder', help='Folder where picture are saved')
    parser.add_argument('--cli', action='store_true', help='Use usual pic')
    parser.add_argument('--common', action='store_true', help='Use usual pic')
    parser.add_argument('--space', action='store_true', help='Use NASA pic of'
                        + 'the day')
    return parser


# getting the picture
def getBackgoundCommon(page):
    soup = BeautifulSoup.BeautifulSoup(page, "html.parser")
    imageItem = soup.find("div", attrs={"class": "photo"}).find("img")
    return("http://www.la-photo-du-jour.com/"+imageItem['src'])


# getting the picture
def getBackgoundBonjour(page):
    soup = BeautifulSoup.BeautifulSoup(page, "html.parser")
    imageItem = soup.find("div", attrs={"class": "photo"}).find("img")
    return(imageItem['src'])


# getting the picture
def getSpaceBackground(page):
    soup = BeautifulSoup.BeautifulSoup(page, "html.parser")
    imageItem = soup.find("img")
    return("https://apod.nasa.gov/apod/"+imageItem['src'])


def getBackgound(argv):
    if argv.space:
        site = "https://apod.nasa.gov/apod/astropix.html"
    elif (argv.common):
        site = "http://www.la-photo-du-jour.com/"
    else:
        site = "http://dites.bonjourmadame.fr/"

    try:
        content = urllib.urlopen(site).read()
    except Exception:
        content = urllib.request.urlopen(site).read()

    if argv.space:
        url = getSpaceBackground(content)
    elif (argv.common):
        url = getBackgoundCommon(content)
    else:
        url = getBackgoundBonjour(content)
    return url


def getFolder(argv):
    if argv.folder is not None and os.path.isdir(argv.folder):
        root = argv.folder
        pass
    else:
        root = os.path.abspath(os.path.dirname(__file__))
        pass
    return root


# Os background application
def setGnomeBackground(imagePath):
    cmd = "gsettings set org.gnome.desktop.background draw-background false;"
    os.system(cmd)
    cmd = 'gsettings set org.gnome.desktop.background'\
          ' picture-uri "'+imagePath+'"'
    os.system(cmd)
    cmd = "gsettings set org.gnome.desktop.background draw-background true;"
    os.system(cmd)


def setWindowsBackground(imagePath):
    import ctypes
    ok = ctypes.windll.user32.SystemParametersInfoA(20, 0, imagePath, 0)
    command = 'reg add "HKEY_CURRENT_USER\Control'\
              ' Panel\Desktop" /v Wallpaper /t REG_SZ /d ' + imagePath + ' /f'
    ok = os.system(command)
    os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")
    return ok


def setBackground(url, root):
    system = platform.system()
    if system == "Windows":
        DS = "\\"
    elif system == 'Linux':
        DS = "/"
    basePath = root + DS + "Image.jpg"
    # Downloading the sexy girl
    try:
        urllib.request.urlretrieve(url, basePath)
    except Exception:
        urllib.urlretrieve(url, basePath)
    bmpPath = root + DS + "Image.bmp"
    Image.open(basePath).save(bmpPath)
    if system == "Windows":
        result = setWindowsBackground(bmpPath)
    elif system == 'Linux':
        result = setGnomeBackground(bmpPath)
    return result


def runGui(argv):
    def bonjourmadame(argv):
        argv.common = False
        argv.space = False
        setLikeThat(argv)
        pass

    def nasa(argv):
        argv.common = False
        argv.space = True
        setLikeThat(argv)
        pass

    def laphoto(argv):
        argv.common = True
        argv.space = False
        setLikeThat(argv)
        pass

    def setLikeThat(argv):
        root = getFolder(argv)
        url = getBackgound(argv)
        setBackground(url, root)
        pass

    fenetre = Tk()
    fenetre.title("BonjourBackground")
    fenetre.geometry("300x250")
    img = PhotoImage(file=os.path.abspath('icon.png'))
    fenetre.tk.call('wm', 'iconphoto', fenetre._w, img)
    label = Label(fenetre, text="BonjourBackground", font=("Courier", 18),
                  pady=30)
    label.pack()
    bouton = Button(fenetre, text="Bonjour Madame",
                    command=lambda: bonjourmadame(argv),
                    width=100)
    bouton.pack(pady=10, padx=10)
    bouton = Button(fenetre, text="NASA", command=lambda: nasa(argv),
                    width=100)
    bouton.pack(pady=10, padx=10)
    bouton = Button(fenetre, text="La photo du jour",
                    command=lambda: laphoto(argv),
                    width=100)
    bouton.pack(pady=10, padx=10)
    bouton = Button(fenetre, text="Fermer", command=fenetre.quit, width=50)
    bouton.pack(side=BOTTOM)
    return fenetre.mainloop()


def runCli(argv):
    root = getFolder(argv)
    url = getBackgound(argv)
    setBackground(url, root)


def main(argv):
    if argv.cli:
        runCli(argv)
        pass
    else:
        runGui(argv)
        pass


if __name__ == "__main__":
    parser = parseArgs()
    args = parser.parse_args()
    main(args)
