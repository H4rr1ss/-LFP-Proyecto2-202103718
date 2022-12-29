'''class AFD:
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


estado_inicial = "A"
transiciones={'A': [('$', 'B', '$', 'z')], 'B': [('0', 'B', '$', 'a'), ('1', 'C', 'a', '$')], 'C': [('1', 'D', '$', '$')], 'D': [('1', 'E', 'a', '$'), ('$', 'F', 'z', '$')], 'E': [('1', 'D', '$', '$')]}
aceptacion = ["F"]
cadena = "001111"

prueba_afd = AFD(estado_inicial,transiciones,aceptacion)

prueba_afd.verificar(cadena)

#000111111
#001111'''
