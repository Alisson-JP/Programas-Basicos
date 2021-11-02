#Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.

a = float(input('Por favor, digite o valor A da equação de segundo grau: '))
b = float(input('Digite agora, o valor B da equação de segundo grau: '))
c = float(input('Por último, digite o valor C da equação de segundo grau: '))

delta = (b*b)-4*(a*c)
raiz = float (delta) ** 0.5
x1 = (-b + raiz)/(2*a)
x2 = (-b - raiz)/(2*a)

print(f'Para os valores de {a}, {b} e {c}, o Delta é {delta}.')
print(f'Os valores de x1 e x2, são respectivamente, {x1} e {x2}.')
