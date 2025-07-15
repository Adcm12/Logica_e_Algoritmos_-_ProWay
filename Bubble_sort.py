""" El Bubble Sort es uno de los algoritmos de ordenamiento más simples. Funciona revisando repetidamente una lista, comparando elementos 
adyacentes y cambiándolos de posición si están en el orden incorrecto. Este proceso se repite hasta que la lista esté ordenada. 
No es muy eficiente para listas grandes, pero es excelente para aprender los fundamentos de los algoritmos de ordenamiento. """
from mis_colores import Cores as co

def bubble_sort(vetor):
    n = len(vetor)

    #Recorremos todo el vector
    for i in range(n):
        #for j recorre el vector desde 0 hasta n-i-1 
        for j in range(0, n-i-1):
            #Comparamos el elemento actual con el siguiente
            if vetor[j] > vetor[j+1]:
                # Si el elemento actual es mayor que el siguiente, los intercambiamos
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

    return vetor

numeros_desordenados = [64, 34, 25, 12, 22, 11, 90]
print(co.VERMELHO, "Lista desordenada:", numeros_desordenados)

print(co.VERDE, "Lista ordenada:", bubble_sort(numeros_desordenados), co.RESET)