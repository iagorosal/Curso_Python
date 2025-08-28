p = input('Informe uma palavra: ')
print(len(p))

print('-'*80)

numeros = input('Informe 5 numeros separados por Virgula (,): ').split(',')

numeros = [int(num) for num in numeros]
soma =  sum(numeros)
maior = max(numeros)

print(f'O maior numero da Lista foi {maior} e a soma dos numeros é {soma}')

print('-'*80)

inteiro = 10
flutuante = 9.8
boleano = True

print(f'Está é uma variavel inteira {inteiro}, {type(inteiro)}\n'
      f'Está é uma variavel flutuante {flutuante},{type(flutuante)}\n'
      f'Está é uma variavel boleana {boleano}, {type(boleano)}')
