class Pessoa:

    def __init__(self, cpf, nome, telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        pessoa = {"cpf": cpf, "nome": nome, "telefone": tefefone}
        return pessoa

class Grupo:

    valorDiaria = None
    
    def __init__(self, cod, nome, qtDias):
        self.cod = cod;
        self.nome = nome
        self.qtDias = qtDias
        self.pessoas = []

    def valorPagamento:
        return valorDiaria * qtDias

    def __str__(self):
        grupo = {"cod": cod, "nome": nome, "qtDias": qtDias, "valorDiaria": valorDiaria}
        return grupo
    
class GrupoVip(Grupo):

    def __init__(self, cod, nome, qtDias):
        super().__init__(cod, nome, qtDias)

    def valorPagamento:
        return super().valorPagamento() * 1.1

