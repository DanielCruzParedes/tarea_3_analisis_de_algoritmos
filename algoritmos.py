import timeit



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Menu
opcion = 0

while opcion != 6:
    smallArray = [64, 34, 25, 12, 22, 11, 90]
    largeArray = [i for i in range(10000, 0, -1)]
    print("Seleccionar algoritmo a probar: "
          "\n 1. Insertion Sort"
          "\n 2. Bubble Sort"
          "\n 3. Merge Sort"
          "\n 4. Heap Sort"
          "\n 5. Quick Sort"
          "\n 6. Salir")
    input_opcion = input("Ingrese una opcion (1-6): ")
    opcion = int(input_opcion)
    
    print("\nSeleccionar el tamaño del arreglo a ordenar: "
          "\n 1. Arreglo Pequeño"
          "\n 2. Arreglo Muy Grande")
    input_size = input("Ingrese una opcion (1-2): ")
    size = int(input_size)
    
    if input_opcion == '1':
        if size == 1:
            tiempo = timeit.timeit('insertion_sort(smallArray.copy())', globals=globals(), number=1000)
            print(f"\nTiempo de Insertion Sort en arreglo pequeño: {tiempo} segundos\n")
            #insertion_sort(smallArray)
        elif size == 2:
            tiempo = timeit.timeit('insertion_sort(largeArray.copy())', globals=globals(), number=10)
            print(f"\nTiempo de Insertion Sort en arreglo muy grande: {tiempo} segundos\n")
            #insertion_sort(largeArray)

        #print("Arreglo ordenado:", smallArray if size == 1 else largeArray)
            
    input("Presione Enter para continuar...") 
    
    
    
    