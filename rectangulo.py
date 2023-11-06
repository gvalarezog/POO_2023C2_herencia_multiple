from color import Color
from figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def calcular_area(self):
        return self.alto * self.ancho

    def calcular_perimetro(self):
        return self.alto * 2 + self.ancho * 2

    def __str__(self):
        return f'Rectanugulo: {self.__dict__.__str__()}'

if __name__=='__main__':
    # Ejemplo de uso
    rectangulo = Rectangulo(6, 8)
    print(rectangulo)
    print(f'Área del rectángulo: {rectangulo.calcular_area()}')
    print(Rectangulo.mro())
    print(f'El area del rectangulo es: {rectangulo.calcular_area()}')
    print(f'El perimetro del rectangulo es: {rectangulo.calcular_perimetro()}')