def cpf_valido(numero_do_cpf):
        return len(numero_do_cpf) == 11

def nome_valido(nome):
        return nome.isalpha()

def rg_valido(numero_do_rg):
        return len(numero_do_rg) == 9

def celular_valido(numero_do_celular):
        return len(numero_do_celular) == 11