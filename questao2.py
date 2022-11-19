# QUESTÃO 2: Armazene num vetor de 5 posições o salário de 5 pessoas. 
# Se o salário for menor que 1000 reais, forneça um aumento de 10% e sobrescreva o valor antigo. 
# Ao final, mostre a lista de salários atualizada.

vetor = [929, 2040, 780, 700, 1500]

new_vetor = [round(x*1.1, 2) if x<1000 else x for x in vetor]

print(new_vetor)