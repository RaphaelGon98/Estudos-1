class Pessoa:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome


pessoa1 = Pessoa('raphael', 'gonçalves', '18/09/1998')
pessoa2 = Pessoa('matheus', 'cervelheri', '07/10/1998')

print(pessoa1.nome_completo())
print(Pessoa.nome_completo(pessoa2))
