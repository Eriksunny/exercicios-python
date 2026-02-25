#Exercicios Simples

#Exercicio para permitir entrada com autorizaçao

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Acesso Permitido!')

elif idade < 16:
    print('Acesso Negado!')

else: # Aqui só entra quem tem autorização
    permissao = input('Você tem autorização dos pais? ').lower()

    if permissao == 'sim':
        print('Acesso permitido, com autorização dos pais!')

    else:
        print('Acesso Negado!')