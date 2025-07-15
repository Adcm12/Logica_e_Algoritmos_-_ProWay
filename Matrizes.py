""" Una matriz es una estructura de datos bidimensional, organizada en filas y columnas. En Python, la forma más sencilla 
de representar una matriz es mediante una lista de listas, donde cada lista interna representa una fila. """

from mis_colores import Cores as co  # Importación de un módulo de colores

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Imprimiendo la matriz
print(f"{co.VERDE}Matriz 1:")
for fila in matriz1:
    print(fila)

# Accediendo a elementos de una matriz
print(f"\n{co.AZUL}Elemento en la fila 1, columna 2: {matriz1[0][1]}")  # Acceso al elemento 2
print(f"Elemento en la fila 2, columna 3: {matriz1[1][2]}{co.RESET}")  # Acceso al elemento 6

# Modificando un elemento de la matriz
matriz1[0][1] = 10
print(f"\n{co.VERDE}Matriz 1 después de modificar un elemento:")
for fila in matriz1:
    print(fila)

# Agregando una nueva fila a la matriz
nueva_fila = [10, 11, 12]
matriz1.append(nueva_fila)
print(f"\n{co.AZUL}Matriz 1 después de agregar una nueva fila:")
for fila in matriz1:
    print(fila)

# Eliminando una fila de la matriz
matriz1.remove([4, 5, 6])
print(f"\n{co.VERMELHO}Matriz 1 después de eliminar una fila:")
for fila in matriz1:
    print(fila)

# Ordenando una fila de la matriz
matriz1[0].sort()   # Ordena la primera fila en orden ascendente
print(f"\n{co.AZUL}Matriz 1 después de ordenar la primera fila:")
for fila in matriz1:
    print(fila)

# Verificando si un elemento está en la matriz
if 10 in matriz1[0]:
    print(f"\n{co.VERDE}El número 10 está en la primera fila de la matriz.{co.RESET}")




