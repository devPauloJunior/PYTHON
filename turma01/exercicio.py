def soma_tres_numeros(a,b,c):
    return a+b+c

def corta_vogal(informacao):
    informacao.lower()
    vogais = "aeiou"
    for i in range(len(vogais)):
        informacao = informacao.replace(vogais[i],"BACK")           
    print(informacao)
