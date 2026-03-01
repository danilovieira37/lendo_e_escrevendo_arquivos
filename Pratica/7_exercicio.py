from pathlib import Path

# Desenvolva um script para encontrar um arquivo dentro da pasta home do usuario
caminho = Path.home()
name = input('Digite o nome do arquivo: ')

def encontra_arquivo(caminho, nome_do_arquivo):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file():
            if arquivo.stem == nome_do_arquivo:
                print(f'Arquivo encontrado: {arquivo}')

encontra_arquivo(caminho, name)