class Veiculo():
    def __init__(self, cor, ano, placa, numero_rodas):
        self.cor = cor
        self.ano = ano
        self.placa = placa
        self.numero_rodas = numero_rodas


    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        

    def ligar_motor(self):
        print("Motor ligado.")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, carregado):
        self.carregado = carregado
        
    def está_carregado(self):
        print(f"Está carregado." if self.carregado else "Não está carregado")

print("-----------------------------------------------------------\n")

moto1 = Motocicleta("azul", 2020, "ABC3098", 2)
print(moto1)
moto1.ligar_motor()

print("-----------------------------------------------------------\n")

moto2 = Motocicleta("vermelha", 2001, "FRT5087", 2)
print(moto2)
moto2.ligar_motor()


print("-----------------------------------------------------------\n")

carro1 = Carro("rosa", 1987, "UTY9743", 4)
print(carro1)
carro1.ligar_motor()

print("-----------------------------------------------------------\n")