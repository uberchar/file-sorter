@echo off
cd C:\Users\Jerry\Downloads
dir /b *.mkv > list.txt
echo Created list.txt
echo Running python script
python filesorter.py < list.txt
pause
