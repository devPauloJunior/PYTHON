import datetime
# termo = int(input("Informe um numero: "))
# num1, num2 = 0, 1
# contador = 0
# while contador < termo:
#     num3 = num1 + num2
#     if num3 == termo:
#         print("Termo encontrado")
#         break

#     num1 = num2
#     num2 = num3
#     contador += 1

# if contador == termo:
#     print("termo não pretence a sequencia")


# lista = [1, 2, 3, 4, 5, 10, 11, 20, 21, 30, 31, 70, 77, 80, 88, 100]
# for i in range(len(lista)):
#     if lista[i] % 2 == 0:
#         print("%d é par e é multipo de 2" %(lista[i]))
#     else:
#         print("%d é impar" %(lista[i]))


# hora_atual = datetime.datetime.now()
# agora = hora_atual.strftime("%H:%M:%S")
# print("São exatamente: %s"%(agora))
# hora_int = int(hora_atual.strftime("%H"))
# if hora_int >= 5 and hora_int < 12:
#     print("tenha um bom dia!")
# elif hora_int >=12 and hora_int < 18:
#     print("Tenha uma boa tarde!")
# elif hora_int >=18 and hora_int <= 23:
#     print("Tenha uma boa noite!")
# else:
#     print("está na hora de dormir")

lista1 = []
lista2 = []
uniao = []
for i in range(5):
    lista1.append(input("informe um valor da lista 1: "))
    lista2.append(input("informe um valor da lista 2: "))
    uniao.append(lista1[i])
    uniao.append(lista2[i])

print(lista1)
print(lista2)
print(uniao)
