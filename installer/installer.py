import os
import requests


def install_file(path, url):
    name = url
    while True:
        search = name.find('/')
        if search >= 0:
            name = name[search + 1:]
        else:
            break

    file_name = name
    full_path = os.path.join(path, file_name)  # junta o caminho com o nome do arquivo

    if os.path.exists(path):
        os.system(f'del /f /q "{os.path.join(path, '*')}"')
        os.system(f'rmdir /s /q "{path}"')
    os.makedirs(path, exist_ok=False)  # Cria a pasta, o exist_ok serve para caso ela exista ele não de erro no terminal
    # se for True

    response = requests.get(url)

    if response.status_code == 200:
        with open(full_path, "wb") as file:  # wb é formato de escrita em binario, 'w' write, 'b' binarie
            file.write(response.content)  # o codigo é pego em formato binario por ser um executavel
        print('Arquivo baixado com sucesso!')
    else:
        print(f'Falha ao baixar o arquivo, codigo: {response.status_code}')

def shortcut(path, file_name, shortcut_name):
    files = os.listdir(path)
    exist = False

    for file in files:
        if file == file_name:
            exist = True

    if exist:
        full_path_file = os.path.join(path, file_name)
        full_path_shortcut = os.path.join(path, shortcut_name)
        os.symlink(full_path_file, full_path_shortcut)

if __name__ == '__main__':
    path = 'C:\\Program Files (x86)\\faltas'
    url = 'https://github.com/MateusParra/Faltas/raw/refs/heads/main/dist/main.exe'

    install_file(path, url)
    shortcut(path, 'faltas.exe', 'Calcular Faltas')

