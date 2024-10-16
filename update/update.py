import requests
import os
import tkinter as tk

class Update:
    def __init__(self, path):
        self.path = path
        self.file_path = os.path.dirname(__file__)

    def error(self, text):
        if isinstance(text, str):
            root = tk.Tk()
            root.geometry('400x200')
            root.title('Error')
            root.iconbitmap(os.path.join(os.path.dirname(__file__), 'panico.ico'))
            frame_geral = tk.Frame(root)
            frame_geral.pack()
            title_error = tk.Label(frame_geral, text=text)
            title_error.pack(pady=10)

            root.wait_window(root)

    def check_version(self):
        version = []
        with open(os.path.join(self.path, 'version.txt'), 'r') as file:
            for line in file:
                version.append(line)

        if len(version) > 1:
            raise ValueError("Multiplas versões!")
        else:
            version = version[0].strip()

        try:
            response = requests.get("https://github.com/MateusParra/Faltas/raw/refs/heads/main/version.txt")

            if response.status_code == 200:
                new_version = response.text
            else:
                new_version = 0
        except:
            new_version = 0
            status_code = 0
            self.error('Falha no download, verifique sua conexão e tente novamente!')
            return version == new_version, status_code

        return version == new_version, response.status_code

    def update(self, url):
        file_name = url
        while True:
            search = file_name.find('/')
            if search >= 0:
                file_name = file_name[search + 1:]
            else:
                break

        updated, status_code = self.check_version()

        try:
            response = requests.get(url)
            if not updated:
                if response.status_code == 200 and status_code == 200:
                    with open(os.path.join(self.path, file_name), "wb") as file:
                        file.write(response.content)

                    with open(os.path.join(self.path, 'version.txt'), 'w') as file:
                        new_version = requests.get("https://github.com/MateusParra/Faltas/raw/refs/heads/main/version.txt")
                        new_version = new_version.text
                        file.write(new_version)
                else:
                    self.error(f'Falha ao instalar a atualização, codigo do erro: {status_code if status_code != 200 else response.status_code}')
        except:
            return



    def start_file(self, file_name):
        os.startfile(os.path.join(self.path, file_name))



if __name__ == '__main__':
    url = 'https://github.com/MateusParra/Faltas/raw/refs/heads/main/executables/main.exe'
    path = 'C:\\faltas'

    update = Update(path)
    update.update(url)
    update.start_file('main.exe')
