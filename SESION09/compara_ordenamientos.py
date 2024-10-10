import time
import random

# Generar una lista de 10,000 números aleatorios
lista = [random.randint(0, 10000) for _ in range(10000)]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Función para medir el tiempo de ejecución de cada algoritmo
def medir_tiempo(algoritmo, arr):
    start_time = time.time()
    algoritmo(arr.copy())
    end_time = time.time()
    return end_time - start_time

# Comparar tiempos y guardar en un diccionario
tiempos = {
    "Bubble Sort": medir_tiempo(bubble_sort, lista),
    "Selection Sort": medir_tiempo(selection_sort, lista),
    "Insertion Sort": medir_tiempo(insertion_sort, lista),
    "Merge Sort": medir_tiempo(merge_sort, lista)
}

# Clasificar del más rápido al más lento
clasificados = sorted(tiempos.items(), key=lambda x: x[1])

# Imprimir resultados
print("Tiempos de ejecución para una lista de 10,000 elementos:\n")
for algoritmo, tiempo in clasificados:
    print(f"{algoritmo}: {tiempo:.4f} segundos")

print("\nClasificación del más rápido al más lento con sus tiempos:")
for algoritmo, tiempo in clasificados:
    print(f"{algoritmo}: {tiempo:.4f} segundos")
