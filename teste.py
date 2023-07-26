lista = [x*2 for x in [y for y in range(50) if y % 2 != 0] if x % 2 != 0]
print(lista)

def funcao(x):
    return x**2

a = lambda x: x**2
b = funcao(1)
print(a(2))
print(b(1))