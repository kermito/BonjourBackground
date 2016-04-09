def getBackgound(page):
    import bs4 as BeautifulSoup
    import pprint
    soup = BeautifulSoup.BeautifulSoup(page, "html.parser")
    imageItem = soup.find("div",attrs={"class":"photo"}).find("img")
    return(imageItem['src'])

#getting some sexy page
import urllib
content = urllib.urlopen("http://dites.bonjourmadame.fr/").read()
url = getBackgound(content)

#Downloading the sexy girl
urllib.urlretrieve(url, "Image.jpg")
import os.path
root = os.path.abspath("")
basePath= root+"/Image.jpg"
bmpPath= root+"/Image.bmp"
#print(basePath)

#Lap dance
import os
os.system("gsettings set org.gnome.desktop.background draw-background false;")
command = 'gsettings set org.gnome.desktop.background picture-uri "'+basePath+'"'
os.system(command)
os.system("gsettings set org.gnome.desktop.background draw-background true;")