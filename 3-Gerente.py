from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, salario, num_funcionarios):
        super().__init__(nome, salario)
        self.num_funcionarios = num_funcionarios

# Sobrescrever o metodo aumentar_salario (override = sobrescrição de método)

    def aumentar_salario(self, perc):
        super().aumentar_salario(perc + 5)

# Sobrescrever o metodo imprimir (override)        

    def imprimir(self):
        return (f'{super().imprimir()}\n'
                f'Número de funcionários que gerencia: {self.num_funcionarios}')