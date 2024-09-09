# Abrir o arquivo usando open e ler todo o conteúdo
arquivo = open('loremipsum.txt', 'r')

# Ler e imprimir todo o conteúdo do arquivo
conteudo_completo = arquivo.read()
print("Conteúdo completo do arquivo:")
print(conteudo_completo)

# Fechar o arquivo após a leitura
arquivo.close()

# Ler apenas a primeira linha do arquivo
arquivo = open('loremipsum.txt', 'r')
primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:")
print(primeira_linha)

# Fechar o arquivo após a leitura
arquivo.close()

# Ler os 3 primeiros caracteres do arquivo
arquivo = open('loremipsum.txt', 'r')
primeiros_tres_caracteres = arquivo.read(3)
print("\nPrimeiros 3 caracteres do arquivo:")
print(primeiros_tres_caracteres)

# Fechar o arquivo após a leitura
arquivo.close()

# Utilizando with para abrir o arquivo e ler o conteúdo completo
print("\nConteúdo usando with:")
with open('loremipsum.txt', 'r') as arquivo_with:
    conteudo_with = arquivo_with.read()
    print(conteudo_with)
