import math

a = int(input("Valor del cateto A: "))
b = int(input("Valor del cateto B: "))

ab = (a*a + b*b)

c = math.sqrt(ab)

print(f"La hipotenusa es: {c}")