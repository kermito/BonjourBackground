# 🖥️ 👙 BonjourBackground

#### Every day a new sexy girl in background
Made for gnome shell and Windows, this script get the day pick from [Bonjour madame](http://dites.bonjourmadame.fr "Bonjour madame") and put it as wallpaper for your linux machine,You can add the following command to your startup to change the wallpaper automatically
## 🔧 Installation
#### On ubuntu or debian distrib :
*   you can [Download](http://arnaudtriolet.fr/BonjourBackground-Linux.zip "Download") the builded version

*   To install dependencies and Build :
```bash
sh install.sh
```

  Or just build with
  ```bash
  sh build.sh
  ```

  then
  ```bash
  ./dist/BonjourBackground/BonjourBackground
  ```

#### On windows :
*   you can [Download](http://arnaudtriolet.fr/BonjourBackground-Win.zip "Download") the builded version

*   Or build :
To install dependencies and Build :
```bash
install.cmd
```

  Or just build with
  ```bash
  build.cmd
  ```

then run `BonjourBackground.exe` in `dist/BonjourBackground/`


## 🏃‍ Run the script
```bash
BonjourBackground.exe
```
OR
```bash
python script.py
```

## 🐞 Issue
You must run the script in a folder wich have 777 autorisation with your user
```bash
sudo chmod 777 -R ./ && python backgound.py
```
