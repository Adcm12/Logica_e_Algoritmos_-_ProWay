""" Un vector (o arreglo) es una colección ordenada de elementos. En Python, la estructura más común y flexible que usamos
para esto es la lista. Las listas pueden contener elementos de diferentes tipos, su tamaño es dinámico 
(pueden crecer y decrecer) y sus elementos se acceden a través de un índice, comenzando desde 0.

Ejemplos: """
from mis_colores import Cores as co # Importaçao de um módulo de cores

notas_aluno = [9.44, 8.75, 8.50, 7, 7, 10]

print(f"{co.VERDE}Notas do aluno: {notas_aluno}")

total_de_notas = sum(notas_aluno) / len(notas_aluno) # Calcula a média das notas

print(f"Total de notas: {total_de_notas:.2f}{co.RESET}")



