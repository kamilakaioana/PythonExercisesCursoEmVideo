#Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

m1 = input('escreva algo:')
print(type(m1))
print('É um numérico?', m1.isnumeric())
print('É um alphanumerico?', m1.isalnum())
print('É alfabetico?', m1.isalpha())
