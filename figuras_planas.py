class Figuras:
    __lados = 0
    __area = 0
    __perimetro = 0

    def __init__(self, lados, area, perimetro):
        self.__lados = lados
        self.__area = area
        self.__perimetro = perimetro

    def show(self):
        return 'Lados: {}\nPerimetro: {}\nArea: {}'.format(self.__lados, self.__perimetro, self.__area)
