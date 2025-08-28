
## Crud em Dicionario

contato = {'nome': "Iago", 'telefone''':"111111"}

print(contato)

print('-'*80)
print('MOSTRANDO O CONTATO')
print(contato['nome'])

print('-'*80)
print('ALTERANDO O TELEFONE')
contato['telefone'] = '222222'
print(contato)

print('-'*80)
print('DELETANDO O CONTATO')
del contato['nome']
print(contato)