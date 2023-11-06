from color import Color
from figura_geometrica import FiguraGeometrica


class Cuadrado(Color, FiguraGeometrica):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self,ancho=lado, alto=lado)  # Cuadrado tiene igual alto y ancho
        Color.__init__(self, color=color)

    def calcular_area(self):
        return self.alto * self.ancho

    def calcular_perimetro(self):
        return 4 * self.alto


    def __str__(self):
        return f'Cuadrado: lado= {self.alto}, color: {self.color}'

if __name__=='__main__':
    c = Cuadrado(5, 'amarillo')
    print(c)
    print(Cuadrado.mro())
    # print(c.mro())
    print(f'El area del cuadrado es: {c.calcular_area()}')
    print(f'El perimetro del cuadrado es: {c.calcular_perimetro()}')