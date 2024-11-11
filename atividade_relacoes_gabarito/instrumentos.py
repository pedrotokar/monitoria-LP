from enum import Enum

class TipoCaptacao(Enum):
    PASSIVA = 1
    ATIVA = 2

class TipoPonte(Enum):
    FIXA = 1
    MOVEL = 2

class TipoCorda(Enum):
    NYLON = 1
    ACO = 2

class Instrumento():
    def __init__(self, marca, modelo, preco, numero_cordas):
        self._marca = marca
        self._modelo = modelo
        self._preco = float(preco)
        self._len_cordas = numero_cordas

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def numero_cordas(self):
        return self._len_cordas

    @numero_cordas.setter
    def numero_cordas(self, numero_cordas):
        if numero_cordas < 1 or numero_cordas > 20 or not isinstance(numero_cordas, int):
            raise ValueError("Infelizmente não existem instrumentos com esse número de cordas")
        self._len_cordas = numero_cordas

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        if preco <= 0 or not isinstance(preco, float):
            raise ValueError("Preço invalido para o instrumento")
        self._preco = preco

    def tocar(self, nota):
        raise NotImplementedError("Subclasse não implementou essse método.")

    def __repr__(self):
        return f"{self._marca} {self._modelo} com {self._len_cordas} cordas. Custando R${self._preco}."

    def __del__(self):
        print(f"deletando instrumento {self._marca} {self._modelo}")

class Baixo(Instrumento):
    def __init__(self, marca, modelo, preco, numero_cordas = 4, captacao = TipoCaptacao.PASSIVA):
        super().__init__(marca, modelo, preco, numero_cordas)
        self._tipo_captacao = captacao

    @property
    def captacao(self):
        return self._tipo_captacao

    def tocar(self, nota):
        print(f"Tocaram um {nota} muito grave no baixo. MUITO grave.")

    def __repr__(self):
        return super().__repr__() + f" Captação {self._tipo_captacao.name}"

class Guitarra(Instrumento):
    def __init__(self, marca, modelo, preco, numero_cordas = 6, captacao = TipoCaptacao.PASSIVA, ponte = TipoPonte.FIXA):
        super().__init__(marca, modelo, preco, numero_cordas)
        self._tipo_captacao = captacao
        self._tipo_ponte = ponte

    @property
    def captacao(self):
        return self._tipo_captacao

    @property
    def ponte(self):
        return self._tipo_ponte

    def tocar(self, nota):
        print(f"Tocaram um solo em {nota} cheio de tappings")
        if self._tipo_ponte == TipoPonte.MOVEL:
            print("E usaram a alavanca pra deixar mais do rock ainda")

    def __repr__(self):
        return super().__repr__() + f" Captação {self._tipo_captacao.name} e ponte {self._tipo_ponte.name}"

class Violao(Instrumento):
    def __init__(self, marca, modelo, preco, numero_cordas = 6, cordas = TipoCorda.NYLON):
        super().__init__(marca, modelo, preco, numero_cordas)
        self._tipo_cordas = cordas

    @property
    def cordas(self):
        return self._tipo_cordas

    def tocar(self, nota):
        print("Tocaram um sertanejo.")

    def __repr__(self):
        return super().__repr__() + f" Cordas de {self._tipo_cordas.name}"

if __name__ == "__main__":
    #Testando representações e deleções, além da troca de atributos
    guitarra_1 = Guitarra("Giannini", "G-100", 665, captacao = TipoCaptacao.ATIVA)
    guitarra_2 = Guitarra("Tagima", "TG-510", 1092, numero_cordas = 8, ponte = TipoPonte.MOVEL)
    guitarra_1.preco = 999.0
    try:
        guitarra_2.numero_cordas = 9
    except Exception as e:
        print(f"ERRO: {e}") #Mesmo atribuindo um valor, ele por de baixo dos panos roda as verificações

    print(guitarra_1)
    print(guitarra_2)
    guitarra_1.tocar("lá")
    guitarra_2.tocar("ré")

    print("")

    baixo = Baixo("Aria Pro II", "Magna Series", 500)
    print(baixo)
    try:
        baixo.captacao = TipoCaptacao.ATIVA
    except Exception as e:
        print(f"ERRO: {e}") #Não é possível modificar propriedade que não tem setter
    baixo.tocar("si")

    print("")

    violao_1 = Violao("Giannini", "GDR", 898, cordas = TipoCorda.ACO)
    violao_2 = Violao("Folk Michael", "VM925DT", 1259, numero_cordas = 5)
    print(violao_1)
    print(violao_2)
    violao_1.tocar("mi")
    violao_2.tocar("sol")

    print("")
