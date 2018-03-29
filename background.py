#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import Tk, Label, Button, BOTTOM, Toplevel, PhotoImage
from PIL import Image
import bs4 as BeautifulSoup
import os
import sys
import ctypes
import urllib
import os.path
import platform
import argparse
mainWin = None


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


def createWinStartup(argv, param):
    fileStartup = os.path.expanduser('%ProgramData%\Microsoft\Windows'
                                     '\Start Menu\Programs\Startup'
                                     '\BonjourBackground.cmd')
    file = open(fileStartup, "w")
    exe = os.path.abspath("BonjourBackground.exe")
    tmp = "%appdata%"
    script = '@echo off\n%s --cli --folder %s%s' % exe, tmp, param
    file.write(script)
    file.close()
    return os.path.exists(fileStartup)


def createLinStartup(argv, param):
    fileStartup = os.path.expanduser('~/.config/autostart/'
                                     'BonjourBackground.desktop')
    file = open(fileStartup, "w+")
    exe = os.path.abspath("BonjourBackground")
    icon = os.path.abspath("icon.png")
    script = "[Desktop Entry]\n"
    script += "Type=Application\n"
    script += "Name=BonjourBackground\n"
    script += "Exec=%s --cli%s\n" % (exe, param)
    script += "Icon=%s\n" % icon
    script += "Comment=Every day a new background\n"
    script += "X-GNOME-Autostart-enabled=true\n"
    file.write(script)
    file.close()
    return os.path.exists(fileStartup)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def createStartupScript(argv, param):
    system = platform.system()
    if system == 'Windows':
        success = createWinStartup(argv, param)
        pass
    elif system == "Linux":
        success = createLinStartup(argv, param)
        pass
    else:
        success = False

    if success:
        message('Success')
        pass
    else:
        message("An error as occured")
    pass


def message(msg):
    global mainWin
    sub = Toplevel(mainWin)
    sub.wm_title("BonjourBackground - %s" % msg)
    lab = Label(sub, text=msg)
    lab.pack(side="top", fill="both", expand=True, padx=50, pady=20)
    pass


def addStartup(argv, params):
    system = platform.system()
    if system == 'Windows':
        if is_admin():
            createStartupScript(argv, params)
        else:
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
                                                "", None, 1)
    elif system == "Linux":
        createStartupScript(argv, params)


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

    global mainWin
    mainWin = Tk()
    img = PhotoImage(file='icon.png')
    mainWin.tk.call('wm', 'iconphoto', mainWin._w, img)
    mainWin.title("BonjourBackground")
    mainWin.geometry("300x400")
    label = Label(mainWin, text="BonjourBackground", font=("Courier", 18),
                  pady=30)
    label.pack()

    bouton = Button(mainWin, text="Bonjour Madame",
                    command=lambda: bonjourmadame(argv),
                    width=100)
    bouton.pack(pady=10, padx=10)

    bouton = Button(mainWin, text="Bonjour Madame on startup",
                    command=lambda: addStartup(argv, ""),
                    width=100)
    bouton.pack(pady=10, padx=10)

    bouton = Button(mainWin, text="NASA", command=lambda: nasa(argv),
                    width=100)
    bouton.pack(pady=10, padx=10)
    bouton = Button(mainWin, text="NASA on startup",
                    command=lambda: addStartup(argv, " --space"), width=100)
    bouton.pack(pady=10, padx=10)

    bouton = Button(mainWin, text="La photo du jour",
                    command=lambda: laphoto(argv),
                    width=100)
    bouton.pack(pady=10, padx=10)
    bouton = Button(mainWin, text="La photo du jour on startup",
                    command=lambda: addStartup(argv, "--common"),
                    width=100)
    bouton.pack(pady=10, padx=10)

    bouton = Button(mainWin, text="Fermer", command=mainWin.quit, width=50)
    bouton.pack(side=BOTTOM)
    return mainWin.mainloop()


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
