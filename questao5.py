# QUESTÃO 4:  Faca um algoritmo que leia e armazene 5 valores inteiros em um vetor Vet1. 
# Leia outros 5 valores inteiros e armazene num vetor Vet2. A partir destes valores lidos, mostre na tela:
#     1. a soma dos elementos de cada vetor, nas respectivas posições
#     2. a diferença dos elementos de cada vetor, nas respectivas posições
#     3. o produto dos elementos de cada vetor, nas respectivas posições 
#     4. a divisão entre os elementos de cada vetor, nas respectivas posições 

#new_vetor = [round(x*1.1, 2) if x<1000 else x for x in vetor]
vet1 = []
vet2 = []

for i in range(1,6,1):
    v1 = int(input(f'Insira o {i}º elemento do vet1: '))
    v2 = int(input(f'Insira o {i}º elemento do vet2: '))

    vet1.append(v1)
    vet2.append(v2)

vetsoma = []
vetdiferenca = []
vetproduto = []
vetquociente = []

for i in range(5):
    vetsoma.append(vet1[i] + vet2[i])
    vetdiferenca.append(vet1[i] - vet2[i])
    vetproduto.append(vet1[i] * vet2[i])
    vetquociente.append(vet1[i] / vet2[i])

print(vetsoma, vetdiferenca, vetproduto, vetquociente)