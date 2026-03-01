from pathlib import Path

caminho = Path('/Users/danilovieira37/Documents/Lendo e Escrevendo Arquivos/3_construindo_caminhos.py')

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    caminho_arquivo = caminho / nome
    print(caminho_arquivo)

print(Path.home())