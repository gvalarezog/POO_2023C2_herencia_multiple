from abc import ABC


class Color(ABC):
    def __init__(self, color):
        self._color = color  # Usamos _ para indicar que es un atributo protegido

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color

    def __str__(self):
        return f'Color: {self._color}'

if __name__=='__main__':
    # Ejemplo de uso
    mi_color = Color("rojo")
    print(mi_color)