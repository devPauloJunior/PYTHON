#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na Super classe Funcionario você faz:
# atributos: nome, tempo de empresa, salario(encapsular), faturamento mensal
# Nas Subs classes Vendedor e Supervisor você faz:
# atributos: valor_da_comissao, comissao_especial
# Os métodos devem obedecer o polimorfismo
# métodos abaixo:
# calcula_valor_comissao - esse método calcula o percentual de comissão pelo tempo de empresa maior igual 5 anos 3%, maior igual a 10 anos 6% e maior que 15 anos 9%
# calcula_comissao_especial - esse método calcula o percentual de comissão pelo faturamento mensal, até 15mil/mês 3%, maior igual a 15mil 6%
# OBS: Deve ser criado o POLIMORFISMO do ambiente
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça a impressão dos elementos

class Funcionario:
    pass

class Vendedor(Funcionario):
    pass

class Supervisor(Funcionario):
    pass