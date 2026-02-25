#Exercicios Simples

#Criando uma calculadora para duração do produto

quantidade_do_produto = int(input('Digite a quantidade total do produto: '))
porcao = int(input('Digite a quantidade por porção: '))
porcoes_por_dia = int(input('Quantas porções você usa por dia : '))

total_porcoes = quantidade_do_produto // porcao
dias = total_porcoes // porcoes_por_dia

print(f'O produto terá duração de {dias} dias')