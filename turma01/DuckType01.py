class MeuCatalogo:
    def __init__(self, nome, endereco, email, contato):
        self._nome = nome
        self.endereco = endereco
        self.email = email
        self.contato = contato

    @property
    def nome(self):
        return self._nome
    
    def __str__(self):
        return f'Nome: {self._nome} - Endereço: {self.endereco} - E-mail: {self.email} - Contato: {self.contato}'

class PessoaFisica(MeuCatalogo):
    def __init__(self, nome, endereco, email, contato, data_nascimento, cpf):
        super().__init__(nome, endereco, email, contato)
        self.data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf
    
    def __str__(self):
        return f'Nome: {self._nome} - Endereço: {self.endereco} - E-mail: {self.email} - Contato: {self.contato} - Data de Nascimento: {self.data_nascimento} - CPF: {self._cpf}'

class PessoaJuridica(MeuCatalogo):
    def __init__(self, nome, endereco, email, contato, cnpj):
        super().__init__(nome, endereco, email, contato)
        self._cnpj = cnpj

    def __str__(self):
        return f'Nome: {self._nome} - Endereço: {self.endereco} - E-mail: {self.email} - Contato: {self.contato} - Data de Nascimento: {self.data_nascimento} - CNPJ: {self._cnpj}'

class Agenda():
    def __init__(self, MeuCatalogo):
        self._MeuCatalogo = MeuCatalogo
    
    def __getitem__ (self, item):
        return self._MeuCatalogo[item]

    def __len__(self):
        return len(self._MeuCatalogo)
    
    def mostrar(self):
        return self._MeuCatalogo

contato01 = PessoaFisica("Maria", "Rua 3", "teste@teste.com", "081.99494.3535", "05/09/1995", "12365409865")

contato02 = PessoaJuridica("Americanas", "Rua 10", "americanas@am.com", "085.99884.3115", "88123543000198")

contato03 = PessoaFisica("Silva", "Rua 9", "sisil@teste.com", "084.94484.7575", "16/01/1998", "32487190876")

contato04 = PessoaJuridica("Casas Freitas", "Rua 13", "cf@azedo.com", "085.92282.3222", "99453543000106")
print(f'Nome: {contato01._nome} - Endereço: {contato01.endereco} - Contato: {contato01.contato}, Data de Nasc: {contato01.data_nascimento}')

print(f'Nome: {contato02._nome} - Endereço: {contato02.endereco} - Contato: {contato02.contato}')

lista_de_contatos = [contato01]
nova_agenda = Agenda(lista_de_contatos)

print(lista_de_contatos)
"""
for MeuCatalogo in lista_de_contatos:
    print(nova_agenda.mostrar())
    cpf_cnpj = contato01.cpf if hasattr(MeuCatalogo, 'cpf') else MeuCatalogo._cnpj
    print(f'Nome: {MeuCatalogo._nome} - Endereço: {MeuCatalogo.endereco} - Contato: {MeuCatalogo.contato} - Documento: {cpf_cnpj}')"""
