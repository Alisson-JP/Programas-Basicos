#Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Por favor, digite a altura encontrada (em metros): '))
largura = float(input('Digite agora a largura encontrada (em metros): '))
area = altura * largura
qtd = area / 2
print(f'No total, a área a ser pintada equivale a {area} metros quadrados. Para tanto, você precisará de {qtd} litros de tinta.')
