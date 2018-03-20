@echo off
SET SCRIPT=%~dp0runscript.cmd
copy "%SCRIPT%" "%ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup"
pause
