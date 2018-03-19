#!/usr/bin/env python
try:
    from PIL import Image
    from PIL import ImageFile
except ImportError:
    import Image
    import ImageFile
#getting the picture
def getBackgound(page):
    import bs4 as BeautifulSoup
    import pprint
    soup = BeautifulSoup.BeautifulSoup(page, "html.parser")
    imageItem = soup.find("div",attrs={"class":"photo"}).find("img")
    return(imageItem['src'])

#Os background application
def setGnomeBackground(imagePath):
	import os
	os.system("gsettings set org.gnome.desktop.background draw-background false;")
	command = 'gsettings set org.gnome.desktop.background picture-uri "'+imagePath+'"'
	os.system(command)
	os.system("gsettings set org.gnome.desktop.background draw-background true;")

def setWindowsBackground(imagePath):
	goodPath = convertToBMP(imagePath)
	import ctypes
	import win32con
	ok = ctypes.windll.user32.SystemParametersInfoA(20, 0, goodPath, 0)
	command = 'reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d '+goodPath+' /f'
	ok = os.system(command)
	os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")
	return ok


def convertToBMP(imagePath):

    def resize(imagePath,maxh=1920,maxw=1080,method=Image.BILINEAR): #bilinear offers decent quality and low processing time
        im = Image.open(imagePath)
        w,h = im.size

        if w > maxw:    #width conformity
            whRatio = float(w)/h
            im = im.resize((maxw,int(float(maxw)/whRatio)),method)
        if im.size[1] > maxh:   #height conformity
            im = im.resize(int(maxh*whRatio),maxh)

        im.save(imagePath)
        return imagePath

    f = open(imagePath,'rb')
    p = ImageFile.Parser()
    p.feed(f.read())
    newPath = os.path.join(os.getcwd(),'d.bmp') #automatically infers image format from extension name, and writes as such.
    p.close().save(newPath)
    return resize(newPath)



#getting some sexy page
try:
	import urllib
	content = urllib.urlopen("http://dites.bonjourmadame.fr/").read()
except Exception:
	import urllib.request
	content = urllib.request.urlopen("http://dites.bonjourmadame.fr/").read()

url = getBackgound(content)

#Downloading the sexy girl
try:
	import urllib
	content = urllib.request.urlretrieve(url, "Image.jpg")
except Exception:
	import urllib
	content = urllib.urlretrieve(url, "Image.jpg")


import os.path
root = os.path.abspath(os.path.dirname(__file__))
#print(basePath)

#Lap dance
import platform
system = platform.system()
#print(system)
if system == "Windows":
	bmpPath = root+"\Image.bmp"
	basePath = root+"\Image.jpg"
	result = setWindowsBackground(basePath)
	print(result)
elif system  == 'Linux':
	basePath = root+"/Image.jpg"
	bmpPath = root+"/Image.bmp"
	from PIL import Image
	Image.open(basePath).save(bmpPath)
	result = setGnomeBackground(bmpPath)
	pass
