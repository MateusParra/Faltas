import requests
import os

class Update:
    def __init__(self):
        self.path = os.path.dirname(__file__)

    def check_version(self):
        version = []
        with open('version.txt', 'r') as arquivo:
            for line in arquivo:
                version.append(line)

        if len(version) > 1:
            raise ValueError("Multiplas versões!")
        else:
            version = version[0]

        response = requests.get("https://github.com/MateusParra/Faltas/raw/refs/heads/main/version.txt")

        if response.status_code == 200:
            new_version = response.text
        else:
            raise ValueError(f"Não foi possivel acessar! -- Codigo: {response.status_code}")

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
                with open(os.path.join(self.path, file_name), "wb") as arquivo:
                    arquivo.write(response.content)

                with open('version.txt', 'w') as arquivo:
                    new_version = requests.get("https://github.com/MateusParra/Faltas/raw/refs/heads/main/version.txt")
                    new_version = new_version.text
                    print(new_version)
                    arquivo.write(new_version)
            else:
                print('Falha ao baixar o arquivo!')



if __name__ == '__main__':
    url = 'https://github.com/MateusParra/Faltas/raw/refs/heads/main/executables/main.exe'

    update = Update()
    update.update(url)
