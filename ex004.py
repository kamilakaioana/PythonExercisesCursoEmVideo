#Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

m1 = input('escreva algo:')
print(type(m1))
print('É um número?', m1.isnumeric())
print('É alfanúmerico?', m1.isalnum())
print('É alfabetico?', m1.isalpha())
print('Está em maiusculas?', m1.isupper())
print('Está em minusculas?', m1.islower())
print('Só tem espaços?', m1.isspace())

