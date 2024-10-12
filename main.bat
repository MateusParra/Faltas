rmdir /s /q dist
rmdir /s /q build
pyinstaller --onefile --noconsole --icon "panico.ico" --add-data "panico.ico;." --name main main.py
move dist\main.exe executables
exit