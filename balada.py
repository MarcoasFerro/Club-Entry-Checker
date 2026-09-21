age = int(input('Qual a sua idade? '))
company = input('Você está acompanhado(a/e)? ')

if company == 'sim':
    age_company = int(input('Qual a idade do seu acompanhante? '))

    if age >= 18 and age_company >= 18:
        print('Entrada liberada!')
    else:
        print('Entrada recusada!')

elif company == 'não':
    if age >= 18:
        print('Entrada liberada!')
    else:
        print('Entrada recusada!')
