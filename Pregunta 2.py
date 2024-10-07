def find_peaks(mountain):
    """
    Encuentra los picos en una lista de alturas de montaña.
    
    Un pico se define como un elemento que es mayor que sus vecinos adyacentes.
    
    Args:
    mountain (list): Lista de enteros que representan las alturas de la montaña.
    
    Returns:
    list: Lista de índices donde se encuentran los picos.
    """
    peaks = []  # Lista para almacenar los índices de los picos encontrados
    
    # Iterar a través de la lista desde el segundo elemento hasta el penúltimo
    for i in range(1, len(mountain) - 1):
        # Comprobar si el elemento actual es mayor que el anterior y el siguiente
        if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
            peaks.append(i)  # Si es un pico, agregar el índice a la lista de picos
    
    return peaks  # Devolver la lista de picos

# Ejemplos de uso
print(find_peaks([2, 4, 4]))  # Salida esperada: []
print(find_peaks([1, 4, 3, 8, 5]))  # Salida esperada: [1, 3]