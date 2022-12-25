class AFD:
    def __init__(self, estado_inicial,transiciones,aceptacion):
        self.estado_inicial = estado_inicial
        self.transiciones = transiciones
        self.aceptacion = aceptacion
        self.pila = []

    def verificacionPila(self, entrada, salida):
        if entrada != '$' and entrada != '':
            self.pila.append(entrada)

        if salida != '$' and salida != '':

            ultPila = self.pila[-1]
            if ultPila == salida:
                self.pila.pop()
            else:
                return True



    def verificar(self, cadena):
        estado = self.estado_inicial
        indice = 0

        while indice < len(cadena):

            if indice == 1:
                if alfabeto == '$':
                    indice -= 1
            caracter = cadena[indice]
            encontrado = False
            trans = 1

            for alfabeto, sig, Spila, Epila in self.transiciones[estado]:

                if (alfabeto == '$'and indice == 0):
                    estado = sig
                    encontrado = True
                    estadoPila = self.verificacionPila(Epila, Spila)
                    break

                if caracter == alfabeto:
                    estado = sig
                    encontrado = True
                    estadoPila = self.verificacionPila(Epila, Spila)

                    if estadoPila:
                        break

                    if indice == len(cadena)-1:
                        for alfa, sigi, Spil, Epil in self.transiciones[estado]:
                            if alfa != '$':
                                continue
                            estado = sigi
                            estadoPila = self.verificacionPila(Epil, Spil)

                    break

                if trans == len(self.transiciones[estado]):
                    for alf in self.transiciones[estado]:
                        if alf[0] != '$':
                            continue
                        estado = sig
                        encontrado = True
                        estadoPila = self.verificacionPila(Epila, Spila)
                        break
                trans += 1

            if not encontrado:
                print("caracter invalido, no se puede hacer una transicion de "+estado+" con el simbolo "+caracter )
                break 

            if estadoPila:
                print('ERROR en pila, el ultimo elemento no coincide con el simbolo de pila a sacar.')
                break

            indice += 1

        if estado not in self.aceptacion and len(self.pila) != 0:
            print("cadena invalida, no termina en el estado de aceptacion")
        else:
            print("cadena valida")


estado_inicial = "S0"
transiciones={"S0":[("$","S1","$","#")],"S1":[("x","S1","$","x"),("y","S2","x","$")],"S2":[("y","S2","x","$"), ("$","S3","#","$")]}
aceptacion = ["S3"]
cadena = "xxyyy"

prueba_afd = AFD(estado_inicial,transiciones,aceptacion)

prueba_afd.verificar(cadena)
