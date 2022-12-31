import os
import tkinter.messagebox as MB
import cv2
import imutils
from fpdf import FPDF
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

#---------------------------------------------------------------------------------------------------------------------------|
    def graphviz(self, nombre):
        for ap in self.lista_AP:

            if nombre != ap.getNombre():
                continue

            # -----------------------------------------------GRAFICACIÓN-----------------------------------------------
            graphviz = 'digraph Patron{ \n\n    rankdir = LR\n    layout = dot\n    node[shape = circle, width = 1, height = 1]; \n    subgraph Cluster_A{ \n    label = "' + 'Nombre: '+ str(ap.getNombre()) + '"   \n    fontcolor ="black" \n    fontsize = 30 \n    bgcolor ="#F1DFB2" \n'
            
            for estado in ap.getEstados():
                if estado == ap.getEstadoI():
                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'\n(inicio)" fontcolor = "#000000" fontsize = 20 fillcolor = "#CFF7E7" style = filled shape = cds]; \n'
                    continue

                if estado in ap.getEstadoA():
                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#D0F3E6" style = filled shape = doublecircle]; \n'
                    continue
                
                graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#CFF7E7" style = filled]; \n'

            # .....................CONEXION DE NODOS.......................|
            for E_origen in ap.getTransiciones():
                listEstado = ap.getTransiciones().get(E_origen)
                
                for elemento in listEstado:
                    simbolo = elemento[0]
                    E_destino = elemento[1]
                    salidaPila = elemento[2]
                    entradaPila = elemento[3]
                    graphviz += f'    node{str(E_origen)}->node{str(E_destino)}[label = "{str(simbolo)},{str(salidaPila)};{str(entradaPila)}"]\n'

            graphviz += '\n    } \n\n}'

            document = './Grafos/info_AP/extras/grafica.txt'

            with open(document, 'w') as grafica:
                grafica.write(graphviz)

            # .....................MODIFICACION DE TAMAÑO IMAGEN.......................|
            jpg = './Grafos/info_AP/extras/ap.jpg'
            os.system(f"dot.exe -Tjpg {document} -o {jpg}")

            img = cv2.imread('./Grafos/info_AP/extras/ap.jpg')
            img_salida = imutils.resize(img, width=725)

            cv2.imwrite('./Grafos/info_AP/extras/ap.jpg', img_salida)
            cv2.destroyAllWindows()

            # .....................GENERACION DEL PDF(REPORTE).......................|
            pdf = FPDF(orientation = "L", unit = "mm", format = "A4")
    
            pdf.add_page(),
            pdf.image("./Grafos/info_AP/extras/ap.jpg", x = 15, y = 100)
            pdf.image("./Grafos/logo.png", x = 270, y = 9, w = 22, h = 22)

            pdf.set_font('Arial', '', 15)
            pdf.text(x=80, y=10, txt=f'Estados: {ap.getEstados()}')
            pdf.text(x=80, y=20, txt=f'Alfabeto: {ap.getAlfabeto()}')
            pdf.text(x=80, y=30, txt=f'Alfabeto  de pila: {ap.getSimbolos()}')
            pdf.text(x=80, y=40, txt=f'Estados de aceptacion: {ap.getEstadoA()}')
            pdf.text(x=80, y=60, txt=f'Estado inicial: {ap.getEstadoI()}')
            pdf.text(x=170, y=10, txt='Transiciones:')

            posY = 20
            for EstadoOrigen in ap.getTransiciones():
                listEstadoo = ap.getTransiciones().get(EstadoOrigen)
                
                for element in listEstadoo:
                    pdf.text(x=173, y=posY, txt=f'{EstadoOrigen},{element[0]};{element[1]}')
                    posY += 10

            pdf.output(f"./Grafos/info_AP/Reporte__{ap.getNombre()}.pdf")
            MB.showinfo(message="Se genero correctamente.", title="Reporte creado")
            break
#---------------------------------------------------------------------------------------------------------------------------|


    def validarRuta(self, nombre, cadena):
        rutaValidacion = ''
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
                        rutaValidacion += f'{estado},{alfabeto},{Spila};{sig},{Epila}\n'
                        estado = sig
                        encontrado = True
                        estadoPila = self.verificacionPila(ap, Epila, Spila)
                        break

                    if caracter == alfabeto:
                        rutaValidacion += f'{estado},{alfabeto},{Spila};{sig},{Epila}\n'
                        estado = sig
                        encontrado = True
                        estadoPila = self.verificacionPila(ap, Epila, Spila)

                        if estadoPila:
                            break

                        if indice == len(cadena)-1:
                            for alfa, sigi, Spil, Epil in ap.getTransiciones()[estado]:
                                if alfa != '$':
                                    continue
                                rutaValidacion += f'{estado},{alfa},{Spil};{sigi},{Epil}\n'
                                estado = sigi
                                estadoPila = self.verificacionPila(ap, Epil, Spil)
                        break

                    if trans == len(ap.getTransiciones()[estado]):
                        for alf in ap.getTransiciones()[estado]:
                            if alf[0] != '$':
                                continue
                            rutaValidacion += f'{estado},{alfabeto},{Spila};{sig},{Epila}\n'
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
                return rutaValidacion
#---------------------------------------------------------------------------------------------------------------------------|

#---------------------------------------------------------------------------------------------------------------------------|
    def graphvizPAP(self, nombre, actual, simboloEntrada, cont):
        for ap in self.lista_AP:

            if nombre != ap.getNombre():
                continue

            # -----------------------------------------------GRAFICACIÓN-----------------------------------------------
            graphviz = 'digraph Patron{ \n\n    rankdir = LR\n    layout = dot\n    node[shape = circle, width = 1, height = 1]; \n    subgraph Cluster_A{ \n    label = "' + 'Nombre: '+ str(ap.getNombre()) + '"   \n    fontcolor ="black" \n    fontsize = 30 \n    bgcolor ="#F1DFB2" \n'
            
            for estado in ap.getEstados():
                if estado == ap.getEstadoI():
                    if estado == actual:
                        graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'\n(inicio)" fontcolor = "#000000" fontsize = 20 fillcolor = "#1BB427" style = filled shape = cds]; \n'
                        continue

                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'\n(inicio)" fontcolor = "#000000" fontsize = 20 fillcolor = "#CFF7E7" style = filled shape = cds]; \n'
                    continue

                if estado in ap.getEstadoA():
                    if estado == actual:
                        graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#1BB427" style = filled shape = doublecircle]; \n'
                        continue

                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#D0F3E6" style = filled shape = doublecircle]; \n'
                    continue
                
                if estado == actual:
                    graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#1BB427" style = filled]; \n'
                    continue

                graphviz += f'    node{estado}' + '[label = "'+ str(estado) +'" fontcolor = "#000000" fontsize = 20 fillcolor = "#CFF7E7" style = filled]; \n'

            # .....................CONEXION DE NODOS.......................|
            for E_origen in ap.getTransiciones():
                listEstado = ap.getTransiciones().get(E_origen)
                
                for elemento in listEstado:
                    simbolo = elemento[0]
                    E_destino = elemento[1]
                    salidaPila = elemento[2]
                    entradaPila = elemento[3]

                    if simbolo == simboloEntrada:
                        graphviz += f'    node{str(E_origen)}->node{str(E_destino)}[label = "{str(simbolo)},{str(salidaPila)};{str(entradaPila)}" fontcolor = "#9F2149"]\n'
                        continue

                    graphviz += f'    node{str(E_origen)}->node{str(E_destino)}[label = "{str(simbolo)},{str(salidaPila)};{str(entradaPila)}"]\n'

            graphviz += '\n    } \n\n}'

            document = './Grafos/pasos_AP/extras/grafica.txt'

            with open(document, 'w') as grafica:
                grafica.write(graphviz)

            # .....................MODIFICACION DE TAMAÑO IMAGEN.......................|
            jpg = f'./Grafos/pasos_AP/extras/ap{cont}.png'
            os.system(f"dot.exe -Tpng {document} -o {jpg}")

            img = cv2.imread(f'./Grafos/pasos_AP/extras/ap{cont}.png')
            img_salida = imutils.resize(img, width=530)

            cv2.imwrite(f'./Grafos/pasos_AP/extras/ap{cont}.png', img_salida)
            cv2.destroyAllWindows()
            break

    def validarCadenaPAP(self, nombre, cadena):
        for ap in self.lista_AP:
            if ap.getNombre() != nombre:
                continue

            estado = ap.getEstadoI()
            indice = 0
            pila = 0
            cont = 1

            while indice < len(cadena):

                if indice == 1:
                    if alfabeto == '$':
                        indice -= 1
                caracter = cadena[indice]
                encontrado = False
                trans = 1

                for alfabeto, sig, Spila, Epila in ap.getTransiciones()[estado]:

                    if (alfabeto == '$'and indice == 0):
                        self.graphvizPAP(ap.getNombre(), estado, alfabeto, cont)
                        cont += 1
                        estado = sig
                        encontrado = True
                        estadoPila = self.verificacionPila(ap, Epila, Spila)
                        break

                    if caracter == alfabeto:
                        self.graphvizPAP(ap.getNombre(), estado, alfabeto, cont)
                        cont += 1
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
                                self.graphvizPAP(ap.getNombre(), estado, alfa, cont)
                                estadoPila = self.verificacionPila(ap, Epil, Spil)
                        break

                    if trans == len(ap.getTransiciones()[estado]):
                        for alf in ap.getTransiciones()[estado]:
                            if alf[0] != '$':
                                continue

                            self.graphvizPAP(ap.getNombre(), estado, alf, cont)
                            estado = sig
                            cont += 1
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

        return cont
#---------------------------------------------------------------------------------------------------------------------------|

DB_AP = Database()