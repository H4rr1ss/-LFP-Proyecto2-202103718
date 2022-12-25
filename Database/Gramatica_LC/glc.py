class Producciones:
    def __init__(self, origen, destinos):
        self.origen = origen
        self.destinos = destinos

class Gramatica:
    def __init__(self, nombre, noTerminales, terminales, noTerminalInicial, producciones):
        self.nombre = nombre
        self.noTerminales = noTerminales
        self.terminales = terminales
        self.noTerminalInicial = noTerminalInicial
        self.producciones = producciones