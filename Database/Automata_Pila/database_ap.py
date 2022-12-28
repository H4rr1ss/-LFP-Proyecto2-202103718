import tkinter.messagebox as MB
from Database.Automata_Pila.ap import AutomataPila

class Database():
    def __init__(self):
        self.lista_AP = []
    # https://www.youtube.com/watch?v=o9eUECLgQno

#---------------------------------------------------------------------------------------------------------------------------|
    def __validacion_Estados(self, listEstados):
        for estado in listEstados:
            if listEstados.count(estado) > 1:
                return False
        return True

    def __validacion_estadoInicial(self, estadoInicial, listEstados):
        if estadoInicial not in listEstados:
            return False
        return True

    def __validacion_estadoAceptacion(self, estadosAceptacion, listEstados):
        conf = True
        for estAceptacion in estadosAceptacion:
            if estAceptacion not in listEstados:
                conf = False
        
        if conf is False:
            return False

        return True

    def __validacion_estadosTransicion(self, transiciones, listEstados, listAlfabeto, listSimboloPila):
        for trans in transiciones:
            estado = True
            alfabeto = True
            simbolo = True
            t = trans.split(',')

            if t[0] not in listEstados:
                estado = False

            if t[2] not in listEstados:
                estado = False

            if (t[1] not in listAlfabeto):
                if t[1] != '$':
                    alfabeto = False

            if (t[3] not in listSimboloPila):
                if t[3] != '$':
                    simbolo = False

            if (t[4] not in listSimboloPila):
                if t[4] != '$':
                    simbolo = False

            if (estado is False) or (alfabeto is False) or (simbolo is False):
                return False

        return True 

    def leerArchivos(self, texto):
        listaAP = []
        listaAux = []
        listaTransiciones = []

        newText = str(texto).replace(' ', '')
        listaString = str(list(map(str.strip, eval(newText))))
        listaConvertida = eval(listaString)

        for linea in listaConvertida:

            if linea == '%':
                listaAux.append(listaTransiciones)
                listaAP.append(listaAux)
                listaAux = []
                listaTransiciones = []
                continue

            if len(listaAux) > 5:
                listaTransiciones.append(linea)
                continue

            listaAux.append(linea)
        
        # ||||    ----VERIFICACIONES----    ||||
        AP = 1

        for ap in listaAP:
            alfabeto_ = ap[1].split(",")
            simbolosPila_ = ap[2].split(",")
            estados_ = ap[3].split(",")
            estadosAceptacion_ = ap[5].split(",")

            # VALIDACIONES ---------------------
            if not self.__validacion_Estados(estados_):
                MB.showerror(message=F'Por favor, revise sus estados del AP {AP}', title='ERROR')
                AP += 1
                continue

            if not self.__validacion_estadoInicial(ap[4], estados_):
                MB.showerror(message=F'Por favor, verifique su estado inicial del AP {AP}', title='ERROR')
                AP += 1
                continue

            if not self.__validacion_estadoAceptacion(estadosAceptacion_, estados_):
                MB.showerror(message=F'Por favor, verifique sus estados de aceptación del AP {AP}', title='ERROR')
                AP += 1
                continue

            transiciones_ = []
            for transicion in range(len(ap[6])):
                t = ap[6][transicion].split(',')
                c3 = t[2].split(';')
                transiciones_.append(f'{t[0]},{t[1]},{c3[1]},{c3[0]},{t[3]}')

            if not self.__validacion_estadosTransicion(transiciones_, estados_, alfabeto_, simbolosPila_):
                MB.showerror(message=F'Por favor, verifique sus transiciones del AP {AP}', title='ERROR')
                AP += 1
                continue
            # -----------------------------------

            transiciones = {}
            for tr in transiciones_:
                tr = tr.split(',')
                entrada = (f'{tr[1]}', f'{tr[2]}', f'{tr[3]}', f'{tr[4]}')

                if tr[0] in transiciones:
                    transiciones[tr[0]].append(entrada)
                    continue

                transiciones[tr[0]] = [entrada]

            # CREACION DE OBJETO (AUTOMATA DE PILA)
            automata = AutomataPila(ap[0], alfabeto_, simbolosPila_, estados_, ap[4], estadosAceptacion_, transiciones)
            self.lista_AP.append(automata)
            AP += 1

        return True

# ---------------------------------------------------------------------------------------------------------------------------|
    def verificacionPila(self, ap, entrada, salida):
        if entrada != '$' and entrada != '':
            ap.setApilar(entrada)

        if salida != '$' and salida != '':

            ultPila = ap.getPila()[-1]
            if ultPila == salida:
                ap.desapilar()
            else:
                return True
    
    def validarCadena(self, nombre, cadena):
        for ap in self.lista_AP:
            if ap.getNombre() != nombre:
                continue

            estado = ap.getEstadoI()
            indice = 0
            pila = 0

            while indice < len(cadena):

                if indice == 1:
                    if alfabeto == '$':
                        indice -= 1
                caracter = cadena[indice]
                encontrado = False
                trans = 1

                for alfabeto, sig, Spila, Epila in ap.getTransiciones()[estado]:

                    if (alfabeto == '$'and indice == 0):
                        estado = sig
                        encontrado = True
                        estadoPila = self.verificacionPila(ap, Epila, Spila)
                        break

                    if caracter == alfabeto:
                        estado = sig
                        encontrado = True
                        estadoPila = self.verificacionPila(ap, Epila, Spila)

                        if estadoPila:
                            break

                        if indice == len(cadena)-1:
                            for alfa, sigi, Spil, Epil in ap.getTransiciones()[estado]:
                                if alfa != '$':
                                    continue
                                estado = sigi
                                estadoPila = self.verificacionPila(ap, Epil, Spil)
                        break

                    if trans == len(ap.getTransiciones()[estado]):
                        for alf in ap.getTransiciones()[estado]:
                            if alf[0] != '$':
                                continue
                            estado = sig
                            encontrado = True
                            estadoPila = self.verificacionPila(ap, Epila, Spila)
                            break
                    trans += 1

                if not encontrado:
                    MB.showerror(message=f"Caracter invalido, no se puede hacer una transicion de {estado} con el simbolo {caracter}.", title="ERROR")
                    break 

                if estadoPila:
                    pila = 1
                    MB.showerror(message="El ultimo elemento no coincide con el simbolo de pila a sacar.", title="ERROR")
                    break

                indice += 1

            if estado not in ap.getEstadoA() and len(ap.getPila()) != 0:
                if pila != 1:
                    MB.showerror(message="Cadena invalida, no termina en el estado de aceptación.", title="ERROR")
            else:
                MB.showinfo(message="Cadena valida", title="VERIFICACIÓN")
#---------------------------------------------------------------------------------------------------------------------------|
DB_AP = Database()