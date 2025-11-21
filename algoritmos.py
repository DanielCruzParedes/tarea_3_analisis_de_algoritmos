import timeit # Libreria para medir tiempos de ejecucion

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        indice_mas_pequeño = i
        for j in range(i+1, n):
            if arr[j] < arr[indice_mas_pequeño]:
                indice_mas_pequeño = j
        valor_minimo = arr.pop(indice_mas_pequeño)
        arr.insert(i, valor_minimo)
        
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
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
            
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l

        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# Menu
opcion = 0

while opcion != 7:
    smallArray = [64, 34, 25, 12, 22, 11, 90, 5, 3, 1]
    mediumArray = [i for i in range(1000, 0, -1)]
    largeArray = [i for i in range(10000, 0, -1)]
    print("Seleccionar algoritmo a probar: "
          "\n 1. Insertion Sort"
          "\n 2. Selection Sort"
          "\n 3. Bubble Sort"
          "\n 4. Merge Sort"
          "\n 5. Heap Sort"
          "\n 6. Quick Sort"
          "\n 7. Salir")
    input_opcion = input("Ingrese una opcion (1-6): ")
    opcion = int(input_opcion)
    
    if input_opcion == '7':
        print("Saliendo del programa...")
        break
    
    print("\nSeleccionar el tamaño del arreglo a ordenar: "
          "\n 1. Arreglo Pequeño (10 elementos)"
          "\n 2. Arreglo Mediano (1000 elementos)"
          "\n 3. Arreglo Muy Grande (10000 elementos)")
    input_size = input("Ingrese una opcion (1-3): ")
    size = int(input_size)
    
    if input_opcion == '1':
        if size == 1:
            tiempo = timeit.timeit('insertion_sort(smallArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Insertion Sort en arreglo pequeño: {tiempo} segundos\n")
            #insertion_sort(smallArray)
        elif size == 2:
            tiempo = timeit.timeit('insertion_sort(mediumArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Insertion Sort en arreglo mediano: {tiempo} segundos\n")
            #insertion_sort(mediumArray)
        elif size == 3:
            tiempo = timeit.timeit('insertion_sort(largeArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Insertion Sort en arreglo muy grande: {tiempo} segundos\n")
            #insertion_sort(largeArray)
            
        print("\n Desea correrlo 15 veces? (s/n)")
        repetir = input().lower()
        if repetir == 's':
            if size == 1:
                for i in range(15):
                    tiempo = timeit.timeit('insertion_sort(smallArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Insertion Sort en arreglo pequeño, corrida {i+1}: {tiempo} segundos\n")
            elif size == 2:
                for i in range(15):
                    tiempo = timeit.timeit('insertion_sort(mediumArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Insertion Sort en arreglo mediano, corrida {i+1}: {tiempo} segundos\n")
            elif size == 3:
                for i in range(15):
                    tiempo = timeit.timeit('insertion_sort(largeArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Insertion Sort en arreglo muy grande, corrida {i+1}: {tiempo} segundos\n")


    elif input_opcion == '2':
        if size == 1:
            tiempo = timeit.timeit('selection_sort(smallArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Selection Sort en arreglo pequeño: {tiempo} segundos\n")
            #selection_sort(smallArray)
        elif size == 2:
            tiempo = timeit.timeit('selection_sort(mediumArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Selection Sort en arreglo mediano: {tiempo} segundos\n")
            #selection_sort(mediumArray)
        elif size == 3:
            tiempo = timeit.timeit('selection_sort(largeArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Selection Sort en arreglo muy grande: {tiempo} segundos\n")
            #selection_sort(largeArray)
    
        print("\n Desea correrlo 15 veces? (s/n)")
        repetir = input().lower()
        if repetir == 's':
            if size == 1:
                for i in range(15):
                    tiempo = timeit.timeit('selection_sort(smallArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Selection Sort en arreglo pequeño, corrida {i+1}: {tiempo} segundos\n")
            elif size == 2:
                for i in range(15):
                    tiempo = timeit.timeit('selection_sort(mediumArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Selection Sort en arreglo mediano, corrida {i+1}: {tiempo} segundos\n")
            elif size == 3:
                for i in range(15):
                    tiempo = timeit.timeit('selection_sort(largeArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Selection Sort en arreglo muy grande, corrida {i+1}: {tiempo} segundos\n")
                    
    elif input_opcion == '3':
        if size == 1:
            tiempo = timeit.timeit('bubble_sort(smallArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Bubble Sort en arreglo pequeño: {tiempo} segundos\n")
            #bubble_sort(smallArray)
        elif size == 2:
            tiempo = timeit.timeit('bubble_sort(mediumArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Bubble Sort en arreglo mediano: {tiempo} segundos\n")
            #bubble_sort(mediumArray)
        elif size == 3:
            tiempo = timeit.timeit('bubble_sort(largeArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Bubble Sort en arreglo muy grande: {tiempo} segundos\n")
            #bubble_sort(largeArray)
    
        print("\n Desea correrlo 15 veces? (s/n)")
        repetir = input().lower()
        if repetir == 's':
            if size == 1:
                for i in range(15):
                    tiempo = timeit.timeit('bubble_sort(smallArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Bubble Sort en arreglo pequeño, corrida {i+1}: {tiempo} segundos\n")
            elif size == 2:
                for i in range(15):
                    tiempo = timeit.timeit('bubble_sort(mediumArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Bubble Sort en arreglo mediano, corrida {i+1}: {tiempo} segundos\n")
            elif size == 3:
                for i in range(15):
                    tiempo = timeit.timeit('bubble_sort(largeArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Bubble Sort en arreglo muy grande, corrida {i+1}: {tiempo} segundos\n")
                    
    elif input_opcion == '4':
        if size == 1:
            tiempo = timeit.timeit('merge_sort(smallArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Merge Sort en arreglo pequeño: {tiempo} segundos\n")
            #merge_sort(smallArray)
        elif size == 2:
            tiempo = timeit.timeit('merge_sort(mediumArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Merge Sort en arreglo mediano: {tiempo} segundos\n")
            #merge_sort(mediumArray)
        elif size == 3:
            tiempo = timeit.timeit('merge_sort(largeArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Merge Sort en arreglo muy grande: {tiempo} segundos\n")
            #merge_sort(largeArray)
    
        print("\n Desea correrlo 15 veces? (s/n)")
        repetir = input().lower()
        if repetir == 's':
            if size == 1:
                for i in range(15):
                    tiempo = timeit.timeit('merge_sort(smallArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Merge Sort en arreglo pequeño, corrida {i+1}: {tiempo} segundos\n")
            elif size == 2:
                for i in range(15):
                    tiempo = timeit.timeit('merge_sort(mediumArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Merge Sort en arreglo mediano, corrida {i+1}: {tiempo} segundos\n")
            elif size == 3:
                for i in range(15):
                    tiempo = timeit.timeit('merge_sort(largeArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Merge Sort en arreglo muy grande, corrida {i+1}: {tiempo} segundos\n")
                    
    elif input_opcion == '5':
        if size == 1:
            tiempo = timeit.timeit('heap_sort(smallArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Heap Sort en arreglo pequeño: {tiempo} segundos\n")
            #heap_sort(smallArray)
        elif size == 2:
            tiempo = timeit.timeit('heap_sort(mediumArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Heap Sort en arreglo mediano: {tiempo} segundos\n")
            #heap_sort(mediumArray)
        elif size == 3:
            tiempo = timeit.timeit('heap_sort(largeArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Heap Sort en arreglo muy grande: {tiempo} segundos\n")
            #heap_sort(largeArray)
    
        print("\n Desea correrlo 15 veces? (s/n)")
        repetir = input().lower()
        if repetir == 's':
            if size == 1:
                for i in range(15):
                    tiempo = timeit.timeit('heap_sort(smallArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Heap Sort en arreglo pequeño, corrida {i+1}: {tiempo} segundos\n")
            elif size == 2:
                for i in range(15):
                    tiempo = timeit.timeit('heap_sort(mediumArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Heap Sort en arreglo mediano, corrida {i+1}: {tiempo} segundos\n")
            elif size == 3:
                for i in range(15):
                    tiempo = timeit.timeit('heap_sort(largeArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Heap Sort en arreglo muy grande, corrida {i+1}: {tiempo} segundos\n")
                    
    elif input_opcion == '6':
        if size == 1:
            tiempo = timeit.timeit('quick_sort(smallArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Quick Sort en arreglo pequeño: {tiempo} segundos\n")
            #quick_sort(smallArray)
        elif size == 2:
            tiempo = timeit.timeit('quick_sort(mediumArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Quick Sort en arreglo mediano: {tiempo} segundos\n")
            #quick_sort(mediumArray)
        elif size == 3:
            tiempo = timeit.timeit('quick_sort(largeArray.copy())', globals=globals(), number=1)
            print(f"\nTiempo de Quick Sort en arreglo muy grande: {tiempo} segundos\n")
            #quick_sort(largeArray)
    
        print("\n Desea correrlo 15 veces? (s/n)")
        repetir = input().lower()
        if repetir == 's':
            if size == 1:
                for i in range(15):
                    tiempo = timeit.timeit('quick_sort(smallArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Quick Sort en arreglo pequeño, corrida {i+1}: {tiempo} segundos\n")
            elif size == 2:
                for i in range(15):
                    tiempo = timeit.timeit('quick_sort(mediumArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Quick Sort en arreglo mediano, corrida {i+1}: {tiempo} segundos\n")
            elif size == 3:
                for i in range(15):
                    tiempo = timeit.timeit('quick_sort(largeArray.copy())', globals=globals(), number=1)
                    print(f"\nTiempo de Quick Sort en arreglo muy grande, corrida {i+1}: {tiempo} segundos\n")
                    
            
    input("Presione Enter para continuar...") 
    
    
    
    