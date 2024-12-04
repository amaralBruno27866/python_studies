def heapify(arr, n, i):
    largest = i  # Inicializa o maior como a raiz
    left = 2 * i + 1  # Filho esquerdo
    right = 2 * i + 2  # Filho direito

    # Verifica se o filho esquerdo é maior que a raiz
    if left < n and arr[i] < arr[left]:
        largest = left

    # Verifica se o filho direito é maior que o maior até agora
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Troca e continua heapificando se a raiz não for a maior
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca
        heapify(arr, n, largest)  # Heapifica a subárvore afetada

def heap_sort(arr):
    n = len(arr)

    # Constrói um maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Um por um extrai os elementos do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca
        heapify(arr, i, 0)

# Exemplo de uso
arr = [4, 10, 3, 5, 1, 13, 20, 4, 7, 18, 101]
print ("Array não ordenado é:", arr)
heap_sort(arr)
print("Array ordenado é:", arr)
