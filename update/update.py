import requests
import os

class Update:
    def __init__(self, path):
        self.path = path

    def check_version(self):
        version = []
        with open(os.path.join(self.path, 'version.txt'), 'r') as file:
            for line in file:
                version.append(line)

        if len(version) > 1:
            raise ValueError("Multiplas versões!")
        else:
            version = version[0].strip()

        response = requests.get("https://github.com/MateusParra/Faltas/raw/refs/heads/main/version.txt")

        if response.status_code == 200:
            new_version = response.text
        else:
            raise ValueError(f"Não foi possivel acessar! -- Codigo: {response.status_code}")

        print(version, new_version)

        return version == new_version

    def update(self, url):
        file_name = url
        while True:
            search = file_name.find('/')
            if search >= 0:
                file_name = file_name[search + 1:]
            else:
                break

        updated = self.check_version()

        if not updated:
            response = requests.get(url)
            if response.status_code == 200:
                os.system(f'del {os.path.join(self.path, file_name)}')
                with open(os.path.join(self.path, file_name), "wb") as file:
                    file.write(response.content)

                with open(os.path.join(self.path, 'version.txt'), 'w') as file:
                    new_version = requests.get("https://github.com/MateusParra/Faltas/raw/refs/heads/main/version.txt")
                    new_version = new_version.text
                    print(new_version)
                    file.write(new_version)
            else:
                print('Falha ao baixar o arquivo!')

    def start_file(self, file_name):
        os.startfile(os.path.join(self.path, file_name))



if __name__ == '__main__':
    url = 'https://github.com/MateusParra/Faltas/raw/refs/heads/main/executables/main.exe'
    path = 'C:\\Program Files (x86)\\faltas'

    update = Update(path)
    update.update(url)
    update.start_file('main.exe')
