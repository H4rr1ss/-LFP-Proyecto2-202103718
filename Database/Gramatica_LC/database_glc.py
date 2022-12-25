import sys
import tkinter.messagebox as MB
from itertools import groupby as eliminar_repetidos
import cv2
import imutils
from Database.Gramatica_LC.glc import Gramatica, Producciones

class Database():
    def __init__(self):
        self.lista_GLC = []
        self.lista_nombres_GLC = []

#---------------------------------------------------------------------------------------------------------------------------|
    def __validacion_terminalesYnoTerminales(self, nombre, lista_no_terminales, lista_terminales):
        for listae in lista_no_terminales:
            for listaa in lista_terminales:
                if listaa == listae:
                    self.lista_nombres_GLC.remove(nombre)
                    return False
        return True

    def leerArchivos(self, File):
        try:
            lista_producciones = []
            lista_terminales = []
            lista_no_terminales = []
            lctxt = False
            x = 1

            for file in File:
                file = file.rstrip('\n')

                if x==1:
                    nombre = file
                    if not(nombre in self.lista_nombres_GLC):
                        self.lista_nombres_GLC.append(nombre)
                        x += 1
                        continue

                    MB.showwarning(message=F"La Gramatica ** {nombre} ** séra saltada debido a que ya existe ...", title="ALERTA")
                    x = '%'

                if x==2:
                    file = file.replace(' ','')
                    list_noTerminales_ = file.split(",")
                    for noTerm in list_noTerminales_:
                        lista_no_terminales.append(noTerm)

                    x += 1
                    continue

                if x==3:
                    list_terminales_ = file.split(',')
                    list_terminales_.sort()

                    if not self.__validacion_terminalesYnoTerminales:
                        MB.showerror(message="No fue posible crear el automata debido a que el alfabeto\n de entrada contiene simbolos no terminales", title="ERROR")
                        x = '%'
                    else:
                        lista_terminales = list(lista for lista, _ in eliminar_repetidos(list_terminales_))
                        x += 1
                        continue

                if x==4:
                    einic = file
                    recorrer = False
                    if einic in lista_no_terminales:
                        recorrer = True
                            
                    if recorrer is False:
                        MB.showerror(message="No fue posible crear el automata debido a que el estado inicial no es un no terminal", title="ERROR")
                        self.lista_nombres_GLC.remove(nombre)
                        x = '%'
                    else:
                        einicial = False
                        x += 1
                        continue

                if x != '%':
                    if x>=5 and file != '%':
                        files = file.split('>')
                        files2 = files[1].split()
                        if len(files2) >= 3:
                            lctxt = True

                        if ((files[0] in lista_no_terminales) and (files[1] in lista_no_terminales)):
                            lctxt = True
                        
                        if (files[0] in lista_terminales) and (files[1] in lista_terminales):
                            lctxt = True

                        if len(files2) == 1 and files2[0] in lista_no_terminales:
                            lctxt = True
                        
                        lista_producciones.append(Producciones(files[0], files2))

                if file == '%' and x!="%":
                    if lctxt is True:
                        self.lista_GLC.append(Gramatica(nombre, lista_no_terminales, lista_terminales, einic, lista_producciones))
                        lista_producciones = []
                        lista_terminales = []
                        lista_no_terminales = []
                        x = 0
                        lctxt = False
                    else:
                        MB.showerror(message="No fue posible crear la gramatica debido a que la gramatica no es libre de contexto", title="ERROR")
                        self.lista_nombres_GLC.remove(nombre)
                        lista_producciones = []
                        lista_terminales = []
                        lista_no_terminales = []
                        x = 0

                if file == '%':
                    lista_producciones = []
                    lista_terminales = []
                    lista_no_terminales = []
                    x = 0

                if x!='%':
                    x+=1
            
            return True
    
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])

    def graphviz(self, nombreGLC):
        j = self.lista_nombres_GLC.index(nombreGLC)
        resp = str(j+1)

        try:
            if resp !='0' and int(resp)>0:
                from graphviz import Graph

                dot = Graph(name='GramaticaLC', encoding='utf-8', format='png', filename='GramaticasLC')
                dot.attr(rankdir='TB', layout='dot', shape='none')

                numero = -1
                listaP = []
                indice = 0
                aux = 0
                lista_Nodos = []
                r_2 = int(resp)-1
                for nodo in self.lista_GLC[r_2].producciones:
                    aux = 0
                    if lista_Nodos[:] != []:
                        for x in lista_Nodos:
                            if nodo.origen == x:
                                indice = aux
                            aux+=1
                    else:
                        numero+=1
                        dot.node(name='nodo'+str(numero), label=nodo.origen, shape='none')
                        lista_Nodos.append(nodo.origen)
                    
                    for y in nodo.destinos:
                        numero +=1
                        dot.node(name='nodo'+str(numero), label=y, shape='none')
                        listaP.append(numero)
                        lista_Nodos.append(y)
                    for z in listaP:
                        dot.edge('nodo'+str(indice), 'nodo'+str(z))
                    listaP = []
                    aux = 0
                dot.render('arboles_GLC/arbol_GLC', format='png' ,view=False)

                # PRUEBAS DE IMAGEN DE SALIDA DE ARBOL GLC
                img = cv2.imread('arboles_GLC/arbol_GLC.png')
                img_salida = imutils.resize(img, width=335)

                cv2.imwrite('./arboles_GLC/arbol_GLC.png', img_salida)
                cv2.destroyAllWindows()

            elif int(resp) <0:
                print('\nERROR: Selecciona una opcion valida\n')

            else:
                z = True
        except:
            print("\nPor favor seleccione una opción correcta...")

#---------------------------------------------------------------------------------------------------------------------------|
DB_GLC = Database()