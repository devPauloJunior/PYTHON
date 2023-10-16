""" notas = []
while True:
    nota = float(input("Nota do aluno"))
    notas.append(nota)
    resp = input("S/N")
    if resp == "n" or resp == "N":
        break
notas.pop()
notas[0] = 3.5

for n in notas:
    print(n)

count = 0
while (count <= 10):
    print(count)
    count = count + 1

lado = int(input("lados"))
perimetro = 4 * lado
area = lado * lado
print("perimetro: ", perimetro, " Area: ", area)

count = 0
while count < 10:
    print("A")
    print("Ola: ", count)
    count = count + 1
    print("B")
print("C")

from fractions import Fraction
def double(x):
    return x * 2

print(double(["A", "B", "C"]))
print(double(Fraction(2,5)))


class InitClass(object): 
    def __init__(self): 
        print('Executing the __init__ method.') 
  
ic = InitClass()
"""

n=int(input("digite: "))
s=[1,0]
i=1
valida = False
while i <= n:
    s.append(s[i]+s[i-1])
    i += 1
    if n in s:
        valida = True
        print("OK")
        break

if valida == False:
    print(n, " NÃO É OK")

print(s)
