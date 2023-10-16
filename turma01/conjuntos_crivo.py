# Funções
def imprime(num, osPrimos): 
    print(f'Primos entre 2 e {num}:')
    for candidato in range(2, num+1):
        if candidato in osPrimos:
            print(candidato, end=", ")
    return None

def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def eratostenes(num):
    primos = set()
    for i in range(2, num+1):
        if primo(i):
            primos.add(i)
    return primos

# Chamada Principal
n = int(input("Diga o valor: "))
primos = eratostenes(n)
imprime(n, primos)
