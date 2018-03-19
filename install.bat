python -m pip install --upgrade pip setuptools
python -m pip install django
pip install Image
pip install bs4
pip install pyinstaller

pyinstaller background.py -n BonjourBackground --icon "icon.ico" -y
SET FOLDER=%~dp0
SET SCRIPT=%~dp0runscript.cmd
SET EXE=%~dp0dist\BonjourBackground\BonjourBackground.exe
echo @echo off > %SCRIPT%
echo cd %FOLDER:~0,2% >> %SCRIPT%
echo %EXE% >> %SCRIPT%
