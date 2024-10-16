import os
import requests
import tkinter as tk
import sys

class Installer:
    def __init__(self, path):
        self.path = path
        self._temp_value = None

    def error(self, text):
        if isinstance(text, str):
            root = tk.Tk()
            root.geometry('400x200')
            root.title('Error')
            root.iconbitmap(os.path.join(os.path.dirname(__file__), 'icon.ico'))
            frame_geral = tk.Frame(root)
            frame_geral.pack()
            title_error = tk.Label(frame_geral, text=text)
            title_error.pack(pady=10)

            root.wait_window(root)
            sys.exit()

    def install_file(self, url):
        if os.path.exists(self.path):
            os.system(f'del /f /q "{os.path.join(self.path, '*')}"')
            os.system(f'rmdir /s /q "{self.path}"')
        os.makedirs(self.path, exist_ok=False)  # Cria a pasta, o exist_ok serve para caso ela exista ele não de erro no terminal
        # se for True

        self._temp_value = []

        links = list(url)
        for url in links:
            name = url
            while True:
                search = name.find('/')
                if search >= 0:
                    name = name[search + 1:]
                else:
                    self._temp_value.append(name)
                    break

            file_name = name
            full_path = os.path.join(self.path, file_name)  # junta o caminho com o nome do arquivo
            try:
                response = requests.get(url)

                if response.status_code == 200:
                    with open(full_path, "wb") as file:  # wb é formato de escrita em binario, 'w' write, 'b' binarie
                        file.write(response.content)  # o codigo é pego em formato binario por ser um executavel
                    print(f'{file_name} downloaded in {path}')
                else:
                    self.error(f'Falha no download, codigo do erro: {response.status_code}')
            except:
                self.error('Falha no download, verifique sua conexão e tente novamente!')

    def shortcut(self, url_number, shortcut_name):
        file_name = self._temp_value[url_number]
        files = os.listdir(self.path)
        exist = False

        for file in files:
            if file == file_name:
                exist = True

        if exist:
            full_path_file = os.path.join(self.path, file_name)
            full_path_shortcut = os.path.join(self.path, shortcut_name)
            os.symlink(full_path_file, full_path_shortcut)
            installer.move_shortcut(shortcut_name)

    def move_shortcut(self, shortcut_name):
        start_menu = '%AppData%\\Microsoft\\Windows\\Start Menu\\Programs'
        desktop = '%USERPROFILE%\\Desktop'
        full_path = os.path.join(path, shortcut_name)
        os.system(f'move  "{full_path}" "{desktop}"')
        print(f'{shortcut_name} moved to {desktop}')


if __name__ == '__main__':
    path = 'C:\\faltas'
    url1 = 'https://github.com/MateusParra/Faltas/raw/refs/heads/main/executables/main.exe'
    url2 = 'https://github.com/MateusParra/Faltas/raw/refs/heads/main/executables/update.exe'
    urls = [url1, url2]

    shortcut_name = 'Faltas'

    installer = Installer(path)
    installer.install_file(urls)
    installer.shortcut(2, shortcut_name)
    input('...')


