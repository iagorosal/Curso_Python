n1 = float(input("Informe um numero: "))
n2 = float(input("Informe outro numero: "))

print(f'A soma de {n1} e {n2} é {n1+n2}\n '
      f'A subtração de {n1} e {n2} é {n1-n2}\n'
      f'A Multiplicação de {n1} e {n2} é {n1*n2}\n'
      f'A Divisão de {n1} e {n2} é {n1/n2}')

print('-'*80)
numero = int(input('Informe um numero para verificar se é Par ou Impar: '))

if numero % 2 ==0:
    print('O numero é Par')
else:
    print("O numero é Impar")

print('-'*80)

carteira = int(input("Informe sua idade: "))

if 18 <= carteira <= 30:
    hab = input("Você tem habilitação para dirigir? SIM / NÃO ").islower()
else:
    print('Obrigado!')