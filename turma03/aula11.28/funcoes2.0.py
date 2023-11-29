# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 232 -> 232
def numero_reverso (numero):
    reverso = 0
    while numero > 0:
        #pegar o ultimo valor do numero
        ultimo_valor = numero % 10

        # add ultimo valor
        reverso = (reverso * 10) + ultimo_valor

        # tira ultimo valor
        numero = numero // 10
    #retorna o reverso
    return reverso

numero = int(input('Informe um numero: '))
resultado = numero_reverso(numero)
print(f'O numero informado foi { numero } e o reverso dele é: { resultado }')