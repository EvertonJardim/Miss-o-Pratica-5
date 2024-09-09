# array.sort.py

import random

# Função para exibir o array
def print_array(arr, message):
    print(f"{message}: {arr}")

# Função para ordenar o array usando o método descrito
def custom_sort(array):
    n = len(array)
    for i in range(n):
        # Variável que armazena o índice do menor valor encontrado
        min_index = i
        for j in range(i + 1, n):
            # Verifica se o valor atual é menor que o valor na posição min_index
            if array[j] < array[min_index]:
                min_index = j
        # Troca os valores se necessário
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

# Criação do array de números inteiros com 15 posições
num_array = [random.randint(1, 100) for _ in range(15)]
print_array(num_array, "Array original de números inteiros")

# Aplicação do método custom_sort
custom_sort(num_array)
print_array(num_array, "Array ordenado de números inteiros (crescente)")
