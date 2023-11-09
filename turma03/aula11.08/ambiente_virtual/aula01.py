nome = "Paulo Junior"
altura = 1.70
peso = 79
imc = peso / (altura * altura)

# A reposta dessa questão deve ser:
# FULANO tem ALT de altura, pesa PES quilos e seu imc é: 
# VALOR

print(nome, " tem ", altura, "de altura,")
print("pesa ", peso, " quilos e seu IMC é: ")
print(imc)

print(f'{ nome } tem {altura:.2f} de altura, pesa { peso } quilos e seu imc é: ')
print(f'{imc:.2f}')