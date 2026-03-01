from pathlib import Path
import os

# Listando arquivos de uma pasta
# print(os.listdir(Path.cwd()))
# print(list(Path.cwd().glob('*')))

# Listando arquivos de uma determinada extensao
# print(list(Path.cwd().glob('*.py')))

# Listar tudo dentro de uma pasta
# print(list(Path.cwd().glob('**/*.txt')))

# Validando caminhos
nao_existe = Path.home() / 'nao_existe'
# print(Path.home().exists())
# print(nao_existe.exists())

# Verificando se e arquivo ou pasta
print(Path(__file__))
print(Path(__file__).is_file())

print(Path(__file__).parent)
print(Path(__file__).parent.is_file())

print(Path(__file__).parent)
print(Path(__file__).parent.is_dir())

print(Path(__file__))
print(Path(__file__).is_dir())