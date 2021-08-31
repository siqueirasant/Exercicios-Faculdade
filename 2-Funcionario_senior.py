class Funcionario:
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora

    def imprimir(self):
        return (f'Nome: {self.nome}\nHoras trabalhadas: {self.horas_trabalhadas}\n'
                'f'Valor da hora: R$ {self.valor_hora}')

class Senior(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome, horas_trabalhadas, valor_hora)
        self._bonus = 0
    @property
    def bonus(self):
        return self._bonus

    def _calcular_bonus(self):
        self._bonus = self.horas_trabalhadas / 10.0
        return self._bonus

    #override
    def calcular_salario(self):
        return super().calcular_salario() * self._calcular_bonus        
