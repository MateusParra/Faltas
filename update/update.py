import requests
import os

class Update:
    def __init__(self, path):
        self.path = path
        self._temp_value = None

    def find_name_in_url(self, url):
        while True:
            search_parameter = '/'
            parameter = url.find(search_parameter)
            if parameter >= 0:
                url = url[parameter + 1:]
            else:
                name = url
                return name

    def update(self, url):
        if os.path.exists(self.path):
            name = self.find_name_in_url(url)

            file_path = os.path.join(self.path, name)

            self._temp_value = file_path  # Salva no self para utilizar no start depois

            try:  # Caso a internet esteja desconectada ele vai dar um erro, e isso serve para identificar
                response = requests.get(url)
            except:  # Se a internet não estiver conectada ele retorna
                return

            if response.status_code == 200:  # Caso ele tenha encontrado o arquivo ele pega o valor binario dele
                web_file = response.content
            else:  # Caso não tenha funcionado ele retorna
                return

            if os.path.exists(file_path):  # Se o arquivo existe ele executa
                with open(file_path, 'rb') as file:  # Pega o codigo binario do arquivo
                    installed_file = file.read()

                if not installed_file == web_file:  # Caso os codigos binarios não sejam iguais ele atualiza
                    with open(file_path, 'wb') as file:
                        file.write(web_file)
            else:
                with open(file_path, 'wb') as file:  # Se o arquivo não existe ele cria um já atualizado
                    file.write(web_file)

    def start(self):
        os.startfile(self._temp_value)
        self._temp_value = None


if __name__ == '__main__':
    path = 'C:\\faltas'
    url = 'https://github.com/MateusParra/Faltas/raw/refs/heads/main/executables/main.exe'

    update = Update(path)
    update.update(url)
    update.start()
