#Exercicios Simples

#Criando uma calculadora para duração do produto

total_porcoes = int(input('Quantas porções o produto tem?'))
porcoes_por_dia = int(input('Quantas porções você usa por dia?'))

dias = total_porcoes // porcoes_por_dia

print(f'O produto vai durar {dias} dias!')