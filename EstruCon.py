numero = int(input('Informe um Numero: '))

if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('O numero é 0')

print('-'*80)

nota = float(input('Informe a nota: '))

if nota >7:
    print('Aprovado')
elif 5 <= nota <= 6.9:
    print('Recuperação')
else:
    print('Reprovado')

print('-'*80)

idade = int(input('Informe a idade: '))

if idade < 12:
    print('Criança')
elif 13 <= idade <= 17:
    print('Adolescente')
elif 18 <= idade <= 59:
    print('Adulto')
else:
    print('idoso')