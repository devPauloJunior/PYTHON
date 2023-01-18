import os

def add_usuario(usuario, senha):
    novo_arquivo = open("login.txt", "a")
    novo_arquivo.write(usuario + ":" + senha +"\n")
    novo_arquivo.close()
    return None

arquivo_nao_existe = os.path.isfile("login.txt")
if arquivo_nao_existe != True:
    usuario = input("Digite um nome de usuario: ")
    senha = input("Digite uma senha de acesso: ")
    add_usuario(usuario, senha)
else:
    arquivo_vazio = os.stat("login.txt").st_size == 0
    if arquivo_vazio:
        usuario = input("Digite um nome de usuario: ")
        senha = input("Digite uma senha de acesso: ")
        add_usuario(usuario, senha)
    else:
        arquivo = open("login.txt")
        linhas = arquivo.readlines()
        usuario = input("Informe seu usuário: ")
        senha = input("Informe sua senha: ")
        for i, linha in enumerate(linhas):
            nova_linha = linha.replace('\n', '').split(':')
            if  usuario == nova_linha[0] and senha == nova_linha[1]:
                print("Dados OK! Sistema acessado com Sucesso!")
                break
            elif i+1 == len(linhas) and usuario != nova_linha[0]:
                arquivo.close()
                add_usuario(usuario, senha)
                print("Novo usuário cadastrado!")
                break
            else:
                acesso = 0
                if usuario == nova_linha[0]:
                    acesso = 1
                if senha == nova_linha[1]:
                    acesso = 1
                if acesso == 1:
                    print("Usuário ou senha incorreta!")
                    break
        arquivo.close()