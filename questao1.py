# QUESTÃO 1: Faça um algoritmo que leia 10 salários. 
# Depois de lidos e armazenados, mostre o maior valor. 

salarios = [2000, 1000, 750, 920, 1800, 3500, 2200, 2, 980, 1400]

#salarios.sort(reverse=True)
#print(salarios[0])

# tentar fazer bubble sort

def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # troca de elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

    
resultado = bubble_sort(salarios)
print(resultado)