pyinstaller --onefile --noconsole --icon "panico.ico" --add-data "panico.ico;." --name main main.py
move dist\main.exe executables
cd update
pyinstaller --onefile --icon "..\panico.ico" --add-data "version.txt;." --name update update.py
cd ..
move update\dist\update.exe executables
cd installer
pyinstaller --onefile --icon "..\panico.ico" --name installer installer.py
cd ..
move installer\dist\installer.exe executables