#Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.

numero = float(input(f'Por favor, digite um número qualquer: '))
ant = numero - 1
suc = numero + 1
print(f'Você digitou {numero}, o valor imediatamente anterior é {ant}, já o valor imediatamente posterior é {suc}.')
