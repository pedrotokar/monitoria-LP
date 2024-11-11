from instrumentos import Guitarra, Baixo, Violao, TipoPonte, TipoCaptacao, TipoCorda
from funcionarios import Funcionario, CargoFuncionario

class Loja():
    def __init__(self, cep):
        self._localizacao = cep
        self._funcionarios = []
        self._estoque = []
        self._lojas_mais_proxima = None

    @property
    def cep(self):
        return self._localizacao

    #COMPOSIÇÃO: Os instrumentos são inicializados totalmente dentro da classe loja, e não existem fora dela.
    #Por isso, o método recebe os parâmetros que são usados para incicialiar um instrumento
    def adicionar_guitarra(self, marca, modelo, preco, numero_cordas = 6, captacao = TipoCaptacao.PASSIVA, ponte = TipoPonte.FIXA):
        self._estoque.append(Guitarra(marca, modelo, preco, numero_cordas, captacao, ponte))

    def adicionar_baixo(self, marca, modelo, preco, numero_cordas = 4, captacao = TipoCaptacao.PASSIVA):
        self._estoque.append(Baixo(marca, modelo, preco, numero_cordas, captacao))

    def adicionar_violao(self, marca, modelo, preco, numero_cordas = 6, cordas = TipoCorda.NYLON):
        self._estoque.append(Violao(marca, modelo, preco, numero_cordas, cordas))

    def vender_instrumento(self):
        if len(self._estoque) == 0:
            print("Não foi possível vender nada, acabaram os instrumentos")
        else:
            print(f"Foi vendido um \"{self._estoque[0]}\"")
            del self._estoque[0] #COMPOSIÇÃO: O instrumento deixa de existir totalmente

    @property
    def estoque(self):
        contagens = [0, 0, 0]
        for instrumento in self._estoque:
            if isinstance(instrumento, Guitarra):
                contagens[0] += 1
            elif isinstance(instrumento, Baixo):
                contagens[1] += 1
            elif isinstance(instrumento, Violao):
                contagens[2] += 1
        return contagens

    #AGREGAÇÃO: O funcionário pode existir mesmo se essa loja não existir. Por isso.
    #o método recebe o objeto representando o funcionário no lugar de criar um internamente
    def alocar_funcionario(self, funcionario: Funcionario):
        self._funcionarios.append(funcionario)
        funcionario.alocar(self)
        print(f"Funcionário {funcionario.nome} foi alocado para a loja {self._localizacao}")

    def remover_funcionario(self):
        if len(self._funcionarios) == 0:
            print("Não há funcionarios para desalocar da loja")
        else:
            print(f"{self._funcionarios[0].nome} foi removido da loja {self._localizacao}")
            self._funcionarios[0].alocar(None)
            self._funcionarios.pop(0) #AGREGAÇÃO: o funcionário segue existindo e não foi deletado

    @property
    def funcionarios(self):
        contagens = [0, 0, 0, 0]
        for funcionario in self._funcionarios:
            if funcionario.cargo == CargoFuncionario.ESTAGIARIO:
                contagens[0] += 1
            elif funcionario.cargo == CargoFuncionario.VENDEDOR:
                contagens[1] += 1
            elif funcionario.cargo == CargoFuncionario.GERENTE:
                contagens[2] += 1
            elif funcionario.cargo == CargoFuncionario.ESTAGIARIO:
                contagens[3] += 1
        return contagens

    @property
    def loja_proxima(self):
        return self._lojas_mais_proxima

    @loja_proxima.setter #ASSOCIAÇÃO: Uma loja pode referenciar a outra mas isso não impacta na vida de nenhuma das duas. Uma loja segue existindo mesmo se a outra não existir
    def loja_proxima(self, loja_perto):
        self._lojas_mais_proxima = loja_perto

    def __repr__(self):
        return f"Loja {self._localizacao}. Estoque: {self.estoque}. Funcionarios: {self.funcionarios}"

    def __del__(self):
        del self._estoque
        for funcionario in self._funcionarios:
            funcionario.alocar(None)


if __name__ == "__main__":
    loja_1 = Loja("22230-010")
    loja_2 = Loja("22250-145")

    print(loja_1)
    print(loja_2)

    loja_1.loja_proxima = loja_2 #ASSOCIAÇÃO: Mesmo se uma das duas for deletada vai tudo ficar ok

    loja_1.adicionar_baixo("Aria Pro II", "Magna Series", 500)
    loja_1.adicionar_guitarra("Giannini", "G-100", 665, captacao = TipoCaptacao.ATIVA)
    loja_1.adicionar_guitarra("Tagima", "TG-510", 1092, numero_cordas = 8, ponte = TipoPonte.MOVEL)
    loja_1.adicionar_violao("Giannini", "GDR", 898, cordas = TipoCorda.ACO)
    loja_1.adicionar_violao("Folk Michael", "VM925DT", 1259, numero_cordas = 5)

    loja_1.vender_instrumento()
    loja_1.vender_instrumento() #COMPOSIÇÃO: Aqui vemos que o método __del__ dos instrumentos foi chamado

    print("")

    gerson = Funcionario("Gerson", 99999999900, "28/07/2004", 1412.0)
    adilson = Funcionario("Adilson", 88888888811, "25/10/1987", 5000, cargo = CargoFuncionario.GERENTE)
    roberto = Funcionario("Rodrigo", 77777777722, "29/02/2000", 8999, cargo = CargoFuncionario.ZELADOR)

    loja_1.alocar_funcionario(gerson)
    loja_1.alocar_funcionario(adilson)
    loja_1.alocar_funcionario(roberto)
    print('-')
    print(gerson)
    print(adilson)
    print(loja_1)

    print("")

    loja_1.remover_funcionario()
    print(loja_1)
    print(gerson) #AGREGAÇÃO: Podemos observar aqui que gerson continua existindo
    print("-")
    loja_2.alocar_funcionario(adilson)
    print(gerson)
    print(loja_2) #AGREGAÇÃO: Trocamos o adilson de loja
    #Mesmo após essas mudanças nenhum funcionario deixou de existir

    print("")
