class MeusContatos:
    def __init__(self, nome, endereco, email, contato):
        self._nome = nome
        self.endereco = endereco
        self.email = email
        self.contato = contato

class PessoaFisica(MeusContatos):
    def __init__(self, nome, endereco, data_nascimento, cpf, email):
        super().__init__(nome, endereco)
        self.data_nascimento = data_nascimento
        self._cpf = cpf
		 self.email = email

    @property
    def cpf(self):
        return self._cpf

class PessoaJuridica(MeusContatos):
    def __init__(self, nome, endereco, email, contato, cnpj):
        super().__init__(nome, endereco, email, contato)
        self._cnpj = cnpj

contato01 = PessoaFisica("Maria", "Rua 3", "teste@teste.com", "081.99494.3535", "05/09/1995", "12365409865")

contato02 = PessoaJuridica("Americanas", "Rua 10", "americanas@am.com", "085.99884.3115", "88123543000198")

contato03 = PessoaFisica("Raimundo", "Rua 11", "rt@rt.com", "086.93444.5535", "10/10/1983", "65743298901")

contato04 = PessoaJuridica("Casas Freitas", "Rua 6", "casasfreitas@cf.com", "088.98814.2358", "99143765000106")
#print(f'Nome: {contato01._nome} - Endereço: {contato01.endereco} - Contato: {contato01.contato}, Data de Nasc: {contato01.data_nascimento}')

#print(f'Nome: {contato02._nome} - Endereço: {contato02.endereco} - Contato: {contato02.contato}')

lista_de_contatos = [contato01, contato02, contato03, contato04]

for MeusContatos in lista_de_contatos:
    cpf_cnpj = contato01.cpf if hasattr(MeusContatos, 'cpf') else MeusContatos._cnpj
    print(f'Nome: {MeusContatos._nome} - Endereço: {MeusContatos.endereco} - Contato: {MeusContatos.contato} - Documento: {cpf_cnpj}')
