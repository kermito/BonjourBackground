def getBackgound(page):
    import bs4 as BeautifulSoup
    import pprint
    soup = BeautifulSoup.BeautifulSoup(page, "html.parser")
    imageItem = soup.find("div",attrs={"class":"photo"}).find("img")
    return(imageItem['src'])

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
import urllib.request
content = urllib.request.urlopen("http://dites.bonjourmadame.fr/").read()
url = getBackgound(content)

#Downloading the sexy girl
import urllib
urllib.request.urlretrieve(url, "Image.jpg")
import os.path
root = os.path.abspath("")
basePath = root+"/Image.jpg"
bmpPath = root+"/Image.bmp"
#print(basePath)

#Lap dance
import platform
system = platform.system()
if system == "Windows":
	setWindowsBackground(basePath)
elif system  == 'linux':
	from PIL import Image
	Image.open(basePath).save(bmpPath)
	setGnomeBackground(bmpPath)
	pass