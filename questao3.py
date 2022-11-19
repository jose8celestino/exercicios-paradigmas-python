# QUESTÃO 3: Faca um programa que leia n valores reais. 
# Armazene estes valores num vetor. Ao final, imprima a média aritmética destes valores. 

from functools import reduce
lista = []

def add(a, b):
    return a + b

while(True):
    q = float(input("Insira um valor numérico (para finalizar digite 0): "))
    if q == 0:
        break
    lista.append(q)
media = sum(lista)/len(lista)

print(media)