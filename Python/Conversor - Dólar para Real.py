### Escreva uma sequência de operações em python que converta um valor em real para dólar -> 1 dol = 5.51 real 

real = float(input("Quantos você tem em reais? "))
conv = real / 5.51
print(f"Essa quantia de {real} reais, equivalem a {conv:.2f} dólares.")

