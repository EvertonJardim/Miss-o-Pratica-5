# Abrir (ou criar) um arquivo texto chamado 'texto.txt'
arquivo = open('texto.txt', 'w')

# Criar uma lista
texto = list()

# Adicionar frases à lista usando o método append
texto.append("Esta é a primeira frase.\n")
texto.append("Aqui está a segunda frase.\n")
texto.append("E esta é a terceira frase.\n")

# Escrever o conteúdo da lista no arquivo
arquivo.writelines(texto)

# Fechar o arquivo
arquivo.close()
