class AutomataPila:
    def __init__(self, nombre, alfabeto, simbolosPila, estados, estadoInicial, estadoAcept, transiciones):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.simbolosPila = simbolosPila
        self.estados = estados
        self.estadoInicial = estadoInicial
        self.estadoAcept = estadoAcept
        self.transiciones = transiciones
        
        # PILA AUX
        self.pila = []

    def getNombre(self):
        return self.nombre

    def getAlfabeto(self):
        return self.alfabeto

    def getSimbolos(self):
        return self.simbolosPila

    def getEstados(self):
        return self.estados

    def getEstadoI(self):
        return self.estadoInicial

    def getEstadoA(self):
        return self.estadoAcept

    def getTransiciones(self):
        return self.transiciones

    def getPila(self):
        return self.pila

    def setApilar(self, entrada):
        self.pila.append(entrada)
    
    def desapilar(self):
        self.pila.pop()