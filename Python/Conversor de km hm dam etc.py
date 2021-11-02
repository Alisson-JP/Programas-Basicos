#Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.

# a saber
# km, hm, dam, m, dm, cm, mm

valor = float(input('Por favor, digite a medida em metros: '))
dam = valor / 10
hm = dam / 10
km = hm / 10
dm = valor * 10
cm = dm * 10
mm = cm * 10

print(f'Você digitou {valor} metros, isso equivale, respectivamente a: ')
print(f'{dam:.4f} decâmetros; {hm:.4f} hectômetros; {km:.4f} kilômetros;')
print(f'{dm:.2f} decímetros; {cm:.2f} centímetros; {mm:.2f} milímetros.')

