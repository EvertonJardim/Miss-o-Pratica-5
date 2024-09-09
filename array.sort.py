# array.sort.py

import random

# Função para exibir o array
def print_array(arr, message):
    print(f"{message}: {arr}")

# Parte 1: Ordenação de um array de números inteiros

# Criação do array de números inteiros com 15 posições
num_array = [random.randint(1, 100) for _ in range(15)]
print_array(num_array, "Array original de números inteiros")

# Ordenação crescente
num_array.sort()
print_array(num_array, "Array ordenado de números inteiros (crescente)")

# Ordenação decrescente
num_array.sort(reverse=True)
print_array(num_array, "Array ordenado de números inteiros (decrescente)")

# Parte 2: Ordenação de um array de strings

# Criação do array de strings
string_array = ["nome", "dataNascimento", "cpf", "rg"]
print_array(string_array, "Array original de strings")

# Ordenação crescente
string_array.sort()
print_array(string_array, "Array ordenado de strings (crescente)")

# Ordenação decrescente
string_array.sort(reverse=True)
print_array(string_array, "Array ordenado de strings (decrescente)")
