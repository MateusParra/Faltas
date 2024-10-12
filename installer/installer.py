import os
import requests
import time

class Installer:
    def __init__(self, path):
        self.path = path

    def install_file(self, urls):
        if os.path.exists(self.path):
            os.system(f'del /f /q "{os.path.join(self.path, '*')}"')
            os.system(f'rmdir /s /q "{self.path}"')
        os.makedirs(self.path, exist_ok=False)  # Cria a pasta, o exist_ok serve para caso ela exista ele não de erro no terminal
        # se for True

        urls = list(urls)
        for url in urls:
            name = url
            while True:
                search = name.find('/')
                if search >= 0:
                    name = name[search + 1:]
                else:
                    break

            file_name = name
            full_path = os.path.join(self.path, file_name)  # junta o caminho com o nome do arquivo

            response = requests.get(url)

            if response.status_code == 200:
                with open(full_path, "wb") as file:  # wb é formato de escrita em binario, 'w' write, 'b' binarie
                    file.write(response.content)  # o codigo é pego em formato binario por ser um executavel
                print(f'{file_name} downloaded in {path}')
            else:
                print(f'failed to download, error code: {response.status_code}')

    def shortcut(self, file_name, shortcut_name):
        files = os.listdir(self.path)
        exist = False

        for file in files:
            if file == file_name:
                exist = True

        if exist:
            full_path_file = os.path.join(self.path, file_name)
            full_path_shortcut = os.path.join(self.path, shortcut_name)
            os.symlink(full_path_file, full_path_shortcut)

    def move_shortcut(self, shortcut_name):
        start_menu = '%AppData%\\Microsoft\\Windows\\Start Menu\\Programs'
        desktop = '%USERPROFILE%\\Desktop'
        full_path = os.path.join(path, shortcut_name)
        os.system(f'copy "{full_path}" "{start_menu}"')
        time.sleep(2.5)
        os.system(f'move  "{full_path}" "{desktop}"')
        print(f'{shortcut_name} moved to {start_menu} and {desktop}')


if __name__ == '__main__':
    path = 'C:\\Program Files (x86)\\faltas'
    url1 = 'https://github.com/MateusParra/Faltas/raw/refs/heads/main/executables/main.exe'
    url2 = 'https://github.com/MateusParra/Faltas/raw/refs/heads/main/executables/update.exe'
    url3 = 'https://github.com/MateusParra/Faltas/raw/refs/heads/main/version.txt'
    urls = [url1, url2, url3]

    shortcut_name = 'Faltas'

    installer = Installer(path)
    installer.install_file(urls)
    installer.shortcut('update.exe', shortcut_name)
    installer.move_shortcut(shortcut_name)
    input('...')


