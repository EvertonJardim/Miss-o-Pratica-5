# array.sort.py

import random

# Função para exibir o array
def print_array(arr, message):
    print(f"{message}: {arr}")

# Método bubbleSort para ordenar o array
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        # Itera sobre o array, excluindo o último elemento já ordenado
        for j in range(0, n - i - 1):
            # Compara elementos adjacentes e troca se necessário
            if array[j] > array[j + 1]:
                # Troca os elementos
                array[j], array[j + 1] = array[j + 1], array[j]

# Parte 1: Ordenação usando bubbleSort

# Criação do array de números inteiros com 15 posições
num_array = [random.randint(1, 100) for _ in range(15)]
print_array(num_array, "Array original de números inteiros")

# Aplicação do método bubbleSort
bubbleSort(num_array)
print_array(num_array, "Array ordenado de números inteiros (crescente)")

# Parte 2: Ordenação de um array de strings (não faz sentido usar bubbleSort aqui, mas vamos incluir para seguir o pedido)

# Criação do array de strings
string_array = ["nome", "dataNascimento", "cpf", "rg"]
print_array(string_array, "Array original de strings")

# Aplicação do método bubbleSort
bubbleSort(string_array)  # Isso funciona, mas a ordenação de strings pode ter diferentes regras de comparação
print_array(string_array, "Array ordenado de strings (crescente)")
