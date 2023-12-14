class Bicicleta:
    """
    Classe que representa uma bicicleta.

    Atributos:
        cor (str): A cor da bicicleta.
        modelo (str): O modelo da bicicleta.
        ano (int): O ano de fabricação da bicicleta.
        valor (float): O valor da bicicleta em reais.
        buzinando (bool): Indica se a buzina está acionada.
        parado (bool): Indica se a bicicleta está parada.

    Métodos:
        __init__(self, cor, modelo, ano, valor, buzinando=False, parado=False):
            Método de inicialização da classe.
        
        __str__(self):
            Retorna uma representação em string da bicicleta.

        buzinar(self):
            Aciona a buzina da bicicleta.

        parar(self):
            Para a bicicleta.

        correr(self):
            Faz a bicicleta correr.

    """

    def __init__(self, cor, modelo, ano, valor, buzinando=False, parado=False):
        """
        Método que inicializa a bicicleta.

        Parâmetros:
            cor (str): A cor da bicicleta.
            modelo (str): O modelo da bicicleta.
            ano (int): O ano de fabricação da bicicleta.
            valor (float): O valor da bicicleta em reais.
            buzinando (bool): Indica se a buzina está acionada (opcional, padrão é False).
            parado (bool): Indica se a bicicleta está parada (opcional, padrão é False).
        """
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.buzinando = buzinando
        self.parado = parado

    def __str__(self):
        """
        Retorna uma representação em string da instância da classe.

        A representação inclui o nome da classe e uma lista formatada de atributos
        e seus valores associados. Esta abordagem proporciona uma forma automática
        de atualizar a string, refletindo qualquer adição ou modificação nos atributos
        da instância, eliminando a necessidade de alterar manualmente este método.

        Retorna:
            str: Uma representação em string da instância da classe.
        
        Exemplo:
            >>> bike = Bicicleta("vermelha", "mountain", 2022, 1500.00, buzinando=True)
            >>> print(bike)
            'Bicicleta: cor = vermelha, modelo = mountain, ano = 2022, valor = 1500.0, buzinando = True, parado = False'
        """
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

        """
        Vamos dividi-la em partes para entender melhor:

        f"{self.__class__.__name__}": Obtém o nome da classe da instância usando self.__class__.__name__.
        "{}: ".format(self.__class__.__name__) seria equivalente.

        self.__dict__.items(): Obtém um iterável com os pares (chave, valor) dos atributos da instância.
        [f'{chave} = {valor}' for chave, valor in self.__dict__.items()]: Cria uma lista de strings formatadas para cada par de atributo e valor.
        ', '.join(...): Junta os elementos da lista em uma string, separados por vírgula e espaço.
        """    

    def buzinar(self):
        """
        Aciona a buzina da bicicleta.
        """
        self.buzinando = True
        print("Bip... bip... bip!")

    def parar(self):
        """
        Para a bicicleta.
        """
        self.parar = True
        print("Freiaaaaaaaaaaaaaar!")

    def correr(self):
        """
        Faz a bicicleta correr.
        """
        self.correr = True
        print("Pedala, pedala, pedala!")

# Cria uma instância da classe Bicicleta
bike = Bicicleta("branca", "street", 2010, 2000)

# Exibe informações da bicicleta
print(bike)

# Aciona a buzina, para e faz a bicicleta correr
bike.buzinar()
bike.parar()
bike.correr()


