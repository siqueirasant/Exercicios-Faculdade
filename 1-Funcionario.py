class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        if not novo_salario >= 0:
            raise ValueError
        self._salario = novo_salario

    def aumentar_salario(self, perc):
        self._salario += self._salario * perc / 100

    def imprimir(self):
        return (f'\nNome: {self.nome}\nSalário: R$ {self.salario:.2f}')


