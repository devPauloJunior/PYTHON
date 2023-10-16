try:
  f = open("demofile.txt", "w")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Algo deu errado ao gravar no arquivo")
  finally:
    f.close()
except:
  print("Algo deu errado ao abrir o arquivo")


# try:
#   print(x)
# except NameError:
#   print("Variável x não está definida")
# except:
#   print("Algo deu errado")

vezes = 0
while True:
    try:
        x = int(input("Digite um numero inteiro: "))
        break
    except:
        vezes += 1
        print("Errou!")
    finally:
      print(f'Você errou {vezes} veze(s)')