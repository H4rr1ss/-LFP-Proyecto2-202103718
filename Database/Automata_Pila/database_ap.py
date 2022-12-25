import tkinter.messagebox as MB


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

            print('listo')


#---------------------------------------------------------------------------------------------------------------------------|
DB_AP = Database()