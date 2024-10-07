def isPathCrossing(path: str) -> bool:
    # Inicializar la posición actual y un conjunto para almacenar las posiciones visitadas
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    
    # Recorrer cada movimiento en el path
    for move in path:
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
        
        # Si la posición actual ya ha sido visitada, el camino se cruza
        if (x, y) in visited:
            return True
        
        # Agregar la posición actual al conjunto de posiciones visitadas
        visited.add((x, y))
    
    # Si no se cruza el camino, devolver False
    return False

if __name__ == "__main__":
    path = input("Introduce el camino: ")
    if isPathCrossing(path):
        print("El camino se cruza.")
    else:
        print("El camino no se cruza.")