# QUESTÃO 4: Faca um programa que pergunte ao usuário o numero de alunos a ser lido. O tamanho dos vetores
# será o numero informado pelo usuário. Armazene num vetor as notas G1 destes alunos; num outro vetor, 
# armazene as notas G2 destes alunos. Ambas notas, G1 e G2, são informadas pelo usuário. Calcule a 
# media aritmética destes alunos e armazene num terceiro vetor. Ao final, mostre as 3 notas dos alunos. 

num_alunos = int(input("Quantos alunos serão avaliados? "))

g1 = []
g2 = []
g3 = []

for i in range(num_alunos):
    n1 = int(input(f"Qual é a nota g1 do aluno {i+1}? "))
    n2 = int(input(f"Qual é a nota g2 do aluno {i+1}? "))
    g1.append(n1)
    g2.append(n2)
    g3.append((n1+n2)/2)

for i in range(num_alunos):
    print(f"As notas do aluno {i+1} foram {g1[i]}(g1) e {g2[i]}(g2), sua média é {g3[i]}")