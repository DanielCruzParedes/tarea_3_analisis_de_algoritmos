import timeit



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
    
    print("\nSeleccionar el tamaño del arreglo a ordenar: "
          "\n 1. Arreglo Pequeño"
          "\n 2. Arreglo Mediano"
          "\n 3. Arreglo Muy Grande")
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
            
    input("Presione Enter para continuar...") 
    
    
    
    