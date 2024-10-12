rmdir /s /q dist
rmdir /s /q build
pyinstaller --onefile --icon "icon.ico" --name installer installer.py
cd ..
move installer\dist\installer.exe executables