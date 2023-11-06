from cuadrado import Cuadrado
from figura_geometrica import FiguraGeometrica
from rectangulo import Rectangulo
from triangulo import Triangulo

# fg = FiguraGeometrica(ancho=5,alto=3)

c1 = Cuadrado(lado=4, color='blanco')
c2 = Cuadrado(lado= 10, color='negro')

r1 = Rectangulo(ancho=5,alto=8)
r2 = Rectangulo(ancho=10,alto=16)
r3 = Rectangulo(alto=4, ancho=5)

t1 = Triangulo(altura=6, base=3)
t2 = Triangulo(altura=12, base=6)

figuras = list()
figuras.append(c1)
figuras.append(c2)
figuras.append(r1)
figuras.append(r2)
figuras.append(t1)
figuras.append(t2)
figuras.append(r3)

print(figuras)

for figura in figuras:
    print(figura)

def sume_areas(figuras):
    areas = 0
    suma_cuadrados = 0
    suma_rect = 0
    for figura in figuras:
        areas += figura.calcular_area()
        if isinstance(figura, Cuadrado):
            suma_cuadrados += 1
        elif isinstance(figura, Rectangulo):
            suma_rect +=1
    print(f'La suma de las areas es: {areas}')
    print(f'La cantidad de cuadrados es: {suma_cuadrados}')
    print(f'La cantidad de rectangulos es: {suma_rect}')

sume_areas(figuras)