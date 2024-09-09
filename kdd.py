import time

# Funções de ordenação
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ler o arquivo e processar o conteúdo
def process_file(filename):
    palavras = []
    with open(filename, 'r') as file:
        for linha in file:
            palavras.extend(linha.split())
    return palavras

# Medir tempo e ordenar
def measure_sorting_time(sort_func, palavras):
    start_time = time.time()
    sorted_words = sort_func(palavras.copy())
    end_time = time.time()
    return sorted_words, end_time - start_time

# Nome do arquivo
arquivo_txt = 'documento.txt'  # Substitua pelo nome do seu arquivo txt

# Processar o arquivo
palavras = process_file(arquivo_txt)

# Ordenar usando Bubble Sort
sorted_words_bubble, time_bubble = measure_sorting_time(bubble_sort, palavras)
print("Bubble Sort:")
print(f"Tempo de execução: {time_bubble:.6f} segundos")
print(sorted_words_bubble)

# Ordenar usando Selection Sort
sorted_words_selection, time_selection = measure_sorting_time(selection_sort, palavras)
print("\nSelection Sort:")
print(f"Tempo de execução: {time_selection:.6f} segundos")
print(sorted_words_selection)

# Ordenar usando o método nativo sort()
start_time = time.time()
palavras.sort()
end_time = time.time()
print("\nMétodo nativo sort():")
print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
print(palavras)

# Salvar palavras ordenadas em um novo arquivo
with open('palavras_ordenadas.txt', 'w') as file:
    file.write('\n'.join(palavras))

