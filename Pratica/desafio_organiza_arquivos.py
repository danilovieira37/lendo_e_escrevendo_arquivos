# Organiza arquivos por formato
from pathlib import Path
import shutil

# Definindo variaveis
local_arquivos = Path('/Users/danilovieira37/Documents/Lendo e Escrevendo Arquivos/Módulo 02/arquivos_desafio')
pasta_atual = Path(__file__).parent

# Criando a pasta organizada
caminho_pasta_organizada = pasta_atual / 'arquivos_organizados'
caminho_pasta_organizada.mkdir(exist_ok=True)

 
for arquivo in list(local_arquivos.glob('*')):
    caminho_pasta_extensoes = caminho_pasta_organizada / arquivo.suffix[1:]
    caminho_pasta_extensoes.mkdir(exist_ok=True)
    nome_arquivo_copiado = arquivo.name
    shutil.copyfile(arquivo, caminho_pasta_extensoes / nome_arquivo_copiado)

print('Arquivos organizados!')