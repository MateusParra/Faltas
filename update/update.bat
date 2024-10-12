rmdir /s /q dist
rmdir /s /q build
pyinstaller --onefile --icon "panico.ico" --add-data "version.txt;." --name update update.py
cd ..
move update\dist\update.exe executables
exit