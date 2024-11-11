from enum import Enum

class CargoFuncionario(Enum):
    ESTAGIARIO =  1
    VENDEDOR = 2
    GERENTE = 3
    ZELADOR = 4

class Funcionario():
    def __init__(self, nome, cpf, data_nascimento, salario, cargo = CargoFuncionario.ESTAGIARIO):
        self._nome = nome
        self._documento = cpf
        self._data_nascimento = data_nascimento
        self._salario = float(salario)
        self._cargo = cargo
        self._loja = None

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._documento

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario < 1412 or not isinstance(novo_salario, int):
            raise ValueError("Sálario abaixo do permitido por lei.")
        self._salario = novo_salario

    @property
    def cargo(self):
        return self._cargo

    @property
    def loja(self):
        return self._loja

    def alocar(self, loja):
        if loja == None:
            if self._loja == None:
                print(f"{self._nome} já não estava alocado em nenhuma loja")
            else:
                print(f"{self._nome} foi tirado da loja {self._loja.cep} e agora não está em nenhuma")
                self._loja = None
        else:
            if self._loja == None:
                self._loja = loja
                print(f"{self._nome} foi alocado para a loja {loja.cep}")
            else:
                loja_antiga = self._loja
                self._loja = loja
                print(f"{self._nome} saiu da loja {loja_antiga.cep} para a loja {loja.cep}")


    def promover(self):
        if self._cargo == CargoFuncionario.ESTAGIARIO:
            self._cargo = CargoFuncionario.ZELADOR
            print(f"{self._nome} foi promovido para zelador")
        elif self._cargo == CargoFuncionario.ZELADOR:
            self._cargo = CargoFuncionario.VENDEDOR
            print(f"{self._nome} foi promovido para vendedor")
        if self._cargo == CargoFuncionario.VENDEDOR:
            self._cargo = CargoFuncionario.GERENTE
            print(f"{self._nome} foi promovido para gerente")
        if self._cargo == CargoFuncionario.GERENTE:
            print(f"{self._nome} alcançou o topo da hierarquia")

    def pagar(self):
        print(f"{self._nome} recebeu R${self._salario} no banco e gastou tudo para pagar contas")

    def __repr__(self):
        loja = self._loja.cep if self._loja is not None else "(nenhuma)"
        return f"Funcionário {self._nome} atualmente no cargo de {self._cargo.name} na loja {loja} recebendo R${self._salario}"

    def __del__(self):
        print(f"{self._nome} morreu.")

if __name__ == "__main__":
    gerson = Funcionario("Gerson", 99999999900, "28/07/2004", 1412.0)
    adilson = Funcionario("Adilson", 88888888811, "25/10/1987", 5000, cargo = CargoFuncionario.GERENTE)

    print(gerson)
    print(gerson.cpf)
    print(adilson)
    print(adilson.data_nascimento)

    print("")

    gerson.pagar()
    adilson.pagar()

    print("")

    gerson.promover()
    print(gerson)

    print("")

