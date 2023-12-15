"""
Vamos estudar o comportamento básico das classes e funções.
"""
class Animal:
    """
    Representa uma classe genérica de animais.

    Atributos:
    - Nenhum atributo é definido nesta classe.

    Métodos:
    - fazer_som(): Imprime um som genérico de um animal.
    """

    def fazer_som(self):
        """Imprime um som genérico de um animal."""
        print("Som genérico de um animal")


class Gato(Animal):
    """
    Representa uma classe que herda de Animal e representa um gato.

    Atributos:
    - Nenhum atributo adicional é definido nesta classe.

    Métodos:
    - fazer_som(): Chama o método fazer_som da classe base (Animal).
    """

    def fazer_som(self):
        """Chama o método fazer_som da classe base (Animal) e imprime 'Miau!'."""
        super().fazer_som()
        print("Miau!")

    
zoe = Gato()
zoe.fazer_som() # Som genérico de um animal

