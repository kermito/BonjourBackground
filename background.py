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
	command = 'reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "'+imagePath+'" /f'
	os.system(command)
	os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")

#getting some sexy page
try:
	import urllib
	content = urllib.urlopen("http://dites.bonjourmadame.fr/").read()
except Exception, e:
	import urllib.request
	content = urllib.request.urlopen("http://dites.bonjourmadame.fr/").read()

url = getBackgound(content)

#Downloading the sexy girl
try:
	import urllib
	content = urllib.request.urlretrieve(url, "Image.jpg")
except Exception, e:
	import urllib
	content = urllib.urlretrieve(url, "Image.jpg")
	

import os.path
root = os.path.abspath("")
basePath = root+"/Image.jpg"
bmpPath = root+"/Image.bmp"
#print(basePath)

#Lap dance
import platform
system = platform.system()
#print(system)
if system == "Windows":
	setWindowsBackground(basePath)
elif system  == 'Linux':
	print"nux"
	from PIL import Image
	Image.open(basePath).save(bmpPath)
	setGnomeBackground(bmpPath)
	pass