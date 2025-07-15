""" Un vector (o arreglo) es una colección ordenada de elementos. En Python, la estructura más común y flexible que usamos
para esto es la lista. Las listas pueden contener elementos de diferentes tipos, su tamaño es dinámico 
(pueden crecer y decrecer) y sus elementos se acceden a través de un índice, comenzando desde 0.

Ejemplos: """
from mis_colores import Cores as co # Importaçao de um módulo de cores

notas_aluno = [9.44, 8.75, 8.50, 7, 7, 10]

print(f"{co.VERDE}Notas do aluno: {notas_aluno}")

total_de_notas = sum(notas_aluno) / len(notas_aluno) # Calcula a média das notas

print(f"Promedio de notas: {total_de_notas:.2f}{co.RESET}")

# Accesando elementos de uma lista
print(f"\n{co.AZUL}Primeira nota: {notas_aluno[0]}")
print(f"Segunda nota: {notas_aluno[1]}")
print(f"Terceira nota: {notas_aluno[2]}{co.RESET}")

# Modificando elementos de uma lista
notas_aluno[0] = 9.50
print(f"\n{co.VERDE}Notas do aluno após modificação: {notas_aluno}{co.RESET}")

# Adicionando elementos a uma lista
notas_aluno.append(9.80)
print(f"\n{co.AZUL}Notas do aluno após adicionar nova nota: {notas_aluno}{co.RESET}")

# Removendo elementos de uma lista
notas_aluno.remove(7)
print(f"\n{co.VERMELHO}Notas do aluno após remover uma nota: {notas_aluno}{co.RESET}")

# Ordenando uma lista
notas_aluno.sort() # sort: ordena a lista em ordem crescente
print(f"\n{co.AZUL}Notas do aluno ordenadas: {notas_aluno}{co.RESET}")

# Verificando se um elemento está na lista
if 10 in notas_aluno:
    print(f"\n{co.VERDE}O aluno tem nota 10!{co.RESET}")






