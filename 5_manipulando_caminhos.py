from pathlib import Path

'''# Retornando caminho do diretorio de trabalho atual
print(Path.cwd())

# Esse caminho e absoluto
print(Path.cwd().is_absolute())

# Retormando caminho da primeira pasta
print(Path('primeira_pasta'))

# Esse caminho e absoluto
print(Path('primeira_pasta').is_absolute())


# Garantindo que estamos retornando o caminho para a pasta do script
print(__file__)
print(Path(__file__).is_absolute())
print(Path(__file__).parent)

'''

# Trabalhando com partes do caminho
caminho_arquivo = Path(__file__)

print(caminho_arquivo)
print(caminho_arquivo.anchor)
print(type(caminho_arquivo.parent))
print(caminho_arquivo.name)
print(caminho_arquivo.stem)
print(caminho_arquivo.suffix)
print(caminho_arquivo.drive)
print(caminho_arquivo.parent)
print(caminho_arquivo.parents[1])