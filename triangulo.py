from figura_geometrica import FiguraGeometrica


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__(alto=altura, ancho=base)  # Invertimos el alto y ancho para que coincidan con la base y la altura del triángulo

    def calcular_area(self):
        return 0.5 * self.ancho * self.alto

    def calcular_perimetro(self):
        pass
        #calcular hipotenusa y sumarlo con alto y anchoc

    def __str__(self):
        return f'Triangulo: {self.__dict__.__str__()}'

if __name__ == '__main__':
    # Ejemplo de uso
    triangulo = Triangulo(4, 6)
    print(triangulo)
    print(f'Área del triángulo: {triangulo.calcular_area()}')
    print(f'El area del triangulo es: {triangulo.calcular_area()}')
    print(f'El perimetro del triangulo es: {triangulo.calcular_perimetro()}')
