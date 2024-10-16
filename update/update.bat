rmdir /s /q dist
rmdir /s /q build
pyinstaller --onefile --noconsole --icon "panico.ico" --add-data "panico.ico;." --name update update.py
cd ..
move update\dist\update.exe executables
exit