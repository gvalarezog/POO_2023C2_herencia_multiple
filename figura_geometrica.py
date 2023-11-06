from abc import ABC, abstractmethod


#Abstract Base Class

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, nuevo_alto):
        if nuevo_alto > 0:
            self._alto = nuevo_alto
        else:
            print("El valor del alto debe ser mayor que cero.")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, nuevo_ancho):
        if nuevo_ancho > 0:
            self._ancho = nuevo_ancho
        else:
            print("El valor del ancho debe ser mayor que cero.")

    @abstractmethod
    def calcular_area(self):
        pass
        # return self.alto * self.ancho

    @abstractmethod
    def calcular_perimetro(self):
        pass
        # return self.alto * 2 + self.ancho * 2

    def __str__(self):
        return f'Figura Geometrica: {self.__dict__.__str__()}'

if __name__=='__main__':
    # Ejemplo de uso
    # figura = FiguraGeometrica(5, 7)
    # print(figura)
    pass
