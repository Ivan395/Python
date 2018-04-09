class Celular:
    __modelo = ""
    __marca = ""
    __numero = ""
    
    def __init__(self, modelo, marca, numero):
        self.modelo = modelo
        self.marca = marca
        self.numero = numero

    def show(self):
        return 'Modelo: {}\nMarca: {}\nNúmero: {}'.format(self.modelo, self.marca, self.numero)
