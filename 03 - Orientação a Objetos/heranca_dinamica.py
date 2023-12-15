'''
Sobre tornar os atributos da classe principal dinamicos nas classes filhas.
Seria um problema para a manutenção no código atualizar manualmente as classes filhas sempre que um novo atributo fosse modificado na classe principal.
'''

class Veiculo:
    """
    Classe base representando um veículo.

    Atributos:
    - cor (str): A cor do veículo.
    - ano (int): O ano de fabricação do veículo.
    - placa (str): A placa do veículo.
    - numero_rodas (int): O número de rodas do veículo, padrão é 4.

    Métodos:
    - __init__(**kwargs): Inicializa um veículo com os atributos fornecidos. Aceita argumentos nomeados (chave, valor).
    - descricao(): Imprime uma descrição do veículo.
    """

    def __init__(self, **kwargs):
        """Inicializa um veículo com os atributos fornecidos. Aceita argumentos nomeados (chave, valor)."""
        self.cor = kwargs.get('cor', None)
        self.ano = kwargs.get('ano', None)
        self.placa = kwargs.get('placa', None)
        self.numero_rodas = kwargs.get('numero_rodas', None)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    

class Motocicleta(Veiculo):
    """
    Classe derivada de Veiculo representando uma motocicleta.

    Métodos:
    - __init__(**kwargs): Inicializa uma motocicleta. Chama o construtor da classe base (Veiculo) com número de rodas padrão 2.
    """

    def __init__(self, **kwargs):
        """Inicializa uma motocicleta. Chama o construtor da classe base (Veiculo) com número de rodas padrão 2."""
        super().__init__(**kwargs, numero_rodas=2)

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.carregado = kwargs.get('carregado', False)
        
    def está_carregado(self):
        print(f"Está carregado." if self.carregado else "Não está carregado")

# Exemplo de uso:
moto1 = Motocicleta(cor="azul", ano=2020, placa="ABC3098")
print(moto1)  


caminhao1 = Caminhao(cor="preto", ano=2024, placa="FRE7645", carregado=True)
print(caminhao1)
caminhao1.está_carregado()

'''
Sucesso em partes.
Ainda não sei se é a melhor forma de fazer, porém funciona.

Problema que ainda não sei resolver:
- **kwargs (dicionário) não mostra os atributos ao instanciar um objeto da classe, diferente de uma variável
- é possível fazer um DocString, mas já dificulta a manutenção já que teria que ser manual e não dinâmica.

Não gostei muito dessa abordagem, principalmente quando existem heranças multiplas. 

'''
