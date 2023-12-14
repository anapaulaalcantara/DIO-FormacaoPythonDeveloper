class Cachorro:
    """
    Representa um objeto Cachorro com atributos.

    Atributos:
        nome (str): Nome do cachorro.
        cor (str): Cor do cachorro.
        idade (int): Idade do cachorro em anos.
        sexo (str): Sexo do cachorro (por exemplo, "Macho" ou "Fêmea").
        latindo (bool): Indica se o cachorro está latindo.
        acordado (bool): Indica se o cachorro está acordado.
        uivando (bool): Indica se o cachorro está uivando.
    """

    def __init__(self, nome, cor, idade, sexo, latindo=False, acordado=True, uivando=False):
        """
        Inicializa um objeto Cachorro com os atributos especificados.

        Parâmetros:
            nome (str): Nome do cachorro.
            cor (str): Cor do cachorro.
            idade (int): Idade do cachorro em anos.
            sexo (str): Sexo do cachorro (por exemplo, "Macho" ou "Fêmea").
            latindo (bool): Indica se o cachorro está latindo (padrão é False).
            acordado (bool): Indica se o cachorro está acordado (padrão é True).
            uivando (bool): Indica se o cachorro está uivando (padrão é False).
        """
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.sexo = sexo
        self.latindo = latindo
        self.acordado = acordado
        self.uivando = uivando

    def __str__(self):
        """
        Retorna uma representação de string do objeto Cachorro.
        """
        return f"Nome: {self.nome} - Cor: {self.cor} - Idade: {self.idade} - Sexo: {self.sexo}"

    def latir(self):
        """
        Faz o cachorro latir e atualiza o atributo 'latindo' para True.
        """
        self.latindo = True
        print("Au-au-au!")

    def dormir(self):
        """
        Faz o cachorro dormir e atualiza o atributo 'acordado' para False.
        """
        self.acordado = False
        print("Zzzz....")

    def uivar(self):
        """
        Faz o cachorro uivar e atualiza o atributo 'uivando' para True.
        """
        self.uivando = True
        print("Auuuuuuuuuauuuuuauuuulllllll...")

# Criando uma instância da classe
dog1 = Cachorro("Fofo", "Preto", 2, "Macho")

# Imprimindo a instância da classe usando o método __str__
print(dog1)

# Chamando os métodos
dog1.latir()
dog1.uivar()
dog1.dormir()
