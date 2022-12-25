from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Tk
import tkinter
import tkinter as tk
import tkinter.messagebox as MB
from Database.Automata_Pila.database_ap import DB_AP
from Database.Gramatica_LC.database_glc import DB_GLC

# -----------------------------------------------------------------MENU INICIAL-----------------------------------------------------------------|
class Menu():
    def __init__(self):
        self.General_ventana()
        self.ventana.title("Pantalla inicio")
        self.centrar(self.ventana, 545, 285)
        self.ventana.geometry("545x270")
        self.Ventana_frame()

    def General_ventana(self):
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(bg = "#BB0D6A", relief = "flat", bd = 16)

    def centrar(self, ventana, ancho, alto):
        altura_pantalla = ventana.winfo_screenheight()
        ancho_pantalla = ventana.winfo_screenwidth()
        x = (ancho_pantalla//2) - (ancho//2)
        y = (altura_pantalla//2) - (alto//2)
        ventana.geometry(f"+{x}+{y}")

    def MostrarVentana(self):
        global cont
        if cont != 6:
            self.frame.config(bg = "#F9E1BE", width = "525", height = "250", relief = "ridge", bd = 12)
            self.label["text"] = f"Esta pantalla se destruirá en {cont} segundos."
            self.frame.after(1000, self.OcultarVentana)
        else:
            self.ventana.destroy()
            Principal()
        cont += 1
        
    def OcultarVentana(self):
        self.frame.place_forget() 
        self.frame.after(100, self.MostrarVentana)

    def Ventana_frame(self):
        global cont 
        cont = 1
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "525", height = "250", relief = "ridge", bd = 12)

        # LABELS-----
        Label(self.frame, text = "Lenguajes Formales y de Programación Sección N", bg = "#F9E1BE", font = ("Comic Sans MS", 13)).place(x = 30, y = 30)
        Label(self.frame, text = "Nombre estudiante: Harry Aaron Gómez Sanic", bg = "#F9E1BE", bd = 0, font = ("Arial", 12)).place(x = 30, y = 70)
        Label(self.frame, text = "carnet: 202103718", bg = "#F9E1BE", bd = 0, font = ("Arial", 12)).place(x = 30, y = 100)
        self.label = Label(self.frame, text = "Esta pantalla se destruirá en 5 segundos", bg = "#F9E1BE", bd = 0, font = ("Arial", 12))
        self.label.place(x = 100, y = 150)

        self.frame.after(100, self.OcultarVentana)

        self.frame.mainloop() 

# ----------------------------------------------------------------------------------------------------------------------------------------------|       




# -----------------------------------------------------------------MENU PRINCIPAL---------------------------------------------------------------|
class Principal(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Menú principal")
        super().centrar(self.ventana, 260, 330)
        self.ventana.geometry("260x310")# ANCHO X LARGO
        self.Ventana_frame() 

    def __ir_pantalla_GLC(self):
        self.ventana.destroy()
        GLC()

    def __ir_pantalla_AP(self):
        self.ventana.destroy()
        AP()

    def __ir_pantalla_salir(self):
        self.ventana.destroy()
        salir()

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "265", height = "315", relief = "ridge", bd = 12)

        # BUTTON------
        self.__btn_crearAFD = Button(self.frame, text = "Módulo GLC", command= self.__ir_pantalla_GLC, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_crearAFD.place(x = 40, y = 31)

        self.__btn_EvaluarCadena = Button(self.frame, text = "Módulo AP", command=self.__ir_pantalla_AP, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_EvaluarCadena.place(x = 40, y = 102)

        self.__btn_GenerarReporte = Button(self.frame, text = "Salir", command=self.__ir_pantalla_salir, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_GenerarReporte.place(x = 40, y = 173)

        self.frame.mainloop()

# ----------------------------------------------------------------------------------------------------------------------------------------------|




# -----------------------------------------------------GRAMATICA LIBRE DE CONTEXTO--------------------------------------------------------------|
class GLC(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Gramatica libre de contexto")
        super().centrar(self.ventana, 320, 330)
        self.ventana.geometry("320x310")# ANCHO X LARGO
        self.Ventana_frame() 

    def __ir_pantalla_CA_GLC(self):
        self.ventana.destroy()
        CA_GLC()
        
    def __ir_pantalla_IG(self):
        self.ventana.destroy()
        IG_GLC()

    def __ir_pantalla_AD(self):
        self.ventana.destroy()
        AD_GLC()

    def __ir_pantalla_R(self):
        self.ventana.destroy()
        Principal()


    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "310", height = "315", relief = "ridge", bd = 12)

        # BUTTON------
        Button(self.frame, text = "Cargar Archivo", command=self.__ir_pantalla_CA_GLC, width = 17, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 55, y = 15)
        Button(self.frame, text = "Información General", command=self.__ir_pantalla_IG, width = 17, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 55, y = 75)
        Button(self.frame, text = "Árbol de Derivación", command=self.__ir_pantalla_AD, width = 17, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 55, y = 135)
        Button(self.frame, text = "Atrás", command=self.__ir_pantalla_R, width = 17, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 55, y = 195)
        
        self.frame.mainloop()

# (CARGAR ARCHIVO)---------->
class CA_GLC(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Cargar Archivos GLC")
        super().centrar(self.ventana, 300, 190)
        self.ventana.geometry("300x170")# ANCHO X LARGO
        self.Ventana_frame() 

    def __regresar(self):
        self.ventana.destroy()
        GLC()
    
    def __cargarArchivo(self):
        try:
            Tk().withdraw()
            archivo = filedialog.askopenfilename(title = 'Select content image', filetypes= [('Archivo GLC', '*.glc'), ('Archivo GR', '*.gre')])

            with open(archivo, 'r') as file:

                texto = file.readlines()
                
                
                if texto == '':
                    MB.showerror('aviso', 'No existe datos en el archivo que ha seleccionado')
                    return 0

                confirmacion = DB_GLC.leerArchivos(texto)

                if confirmacion != 0:
                    MB.showinfo(message="Se agrego correctamente!", title="Archivo leído")
                    self.ventana.destroy()
                    GLC() 
        except:
            MB.showerror('Error', 'No ha cargado ningun archivo, por favor vuelva a internarlo')

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "305", height = "175", relief = "ridge", bd = 12)

        # BUTTON------
        self.__btn_cargarAFD = Button(self.frame, text = "Cargar archivo", command = self.__cargarArchivo, width = 15, height = 3, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_cargarAFD.place(x = 10, y = 25)

        self.__btn_Regresar = Button(self.frame, text = "Salir", command = self.__regresar, width = 8, height = 3, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_Regresar.place(x = 158, y = 25)

        self.frame.mainloop()

# (INFORMACIÓN GENERAL)---------->
class IG_GLC(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Información general GLC")
        super().centrar(self.ventana, 500, 430)
        self.ventana.geometry("500x410")# ANCHO X LARGO
        self.Ventana_frame()

    def __regresar(self):
        self.ventana.destroy()
        GLC()
    
    def funtionsCombo(self, event):
        var = event.widget.get()
        self.nombreGLC = var

        try:
            listaGLC = DB_GLC.lista_GLC
            for glc in listaGLC:
                if glc.nombre != self.nombreGLC:
                    continue
                Label(self.frame, text = f"Nombre: {glc.nombre}", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 15, y = 50)
                Label(self.frame, text = f"No terminales: {glc.noTerminales}", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 15, y = 100)
                Label(self.frame, text = f"Terminales: {glc.terminales}", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 15, y = 150)
                Label(self.frame, text = f"No terminal inicial: {glc.noTerminalInicial}", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 15, y = 200)

                Label(self.frame, text = f"Producciones:", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 260, y = 50)

                listaAux = []
                for produccion in glc.producciones:
                    listaAux.append(produccion.origen)

                listaAux = sorted(listaAux)

                for sweet in listaAux:
                    if listaAux.count(sweet) > 1:
                        listaAux.remove(sweet)

                listP = []
                posY = 70
                for aux in listaAux:
                    for produc in glc.producciones:
                        if aux == produc.origen:
                            if produc.origen not in listP:
                                if len(produc.destinos) == 3:
                                    Label(self.frame, text = f"{produc.origen} > {produc.destinos[0]} {produc.destinos[1]} {produc.destinos[2]}", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 265, y = posY)
                                    posY += 20
                                    listP.append(produc.origen)
                                    continue
                                if len(produc.destinos) == 2:
                                    Label(self.frame, text = f"{produc.origen} > {produc.destinos[0]} {produc.destinos[1]}", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 265, y = posY)
                                    posY += 20
                                    listP.append(produc.origen)
                                    continue
                                if len(produc.destinos) == 1:
                                    Label(self.frame, text = f"{produc.origen} > {produc.destinos[0]}", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 265, y = posY)
                                    posY += 20
                                    listP.append(produc.origen)
                                    continue

                            if len(produc.destinos) == 3:
                                Label(self.frame, text = f"   | {produc.destinos[0]} {produc.destinos[1]} {produc.destinos[2]}", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 265, y = posY)
                                posY += 20
                                continue
                            if len(produc.destinos) == 2:
                                Label(self.frame, text = f"   | {produc.destinos[0]} {produc.destinos[1]}", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 265, y = posY)
                                posY += 20
                                continue
                            if len(produc.destinos) == 1:
                                Label(self.frame, text = f"   | {produc.destinos[0]}", bg = "#F9E1BE", font = ("Comic Sans MS", 9)).place(x = 265, y = posY)
                                posY += 20
                                continue

        except:
            MB.showwarning(message="Seleccione una GLC para generar el grafo.", title="ERROR")

    def __listaGLC(self):
        try:
            listaAux = []
            for i in DB_GLC.lista_GLC:
                listaAux.append(i.nombre)

            # MENU DE GLC'S
            reports = ttk.Combobox(self.frame, width=18, height=5, values = listaAux, state='readonly')
            reports.place(x = 100, y = 12)
            reports.current(0)
            reports.bind('<<ComboboxSelected>>', self.funtionsCombo)
        except:
            MB.showwarning(message="Por favor, ingrese sus GLC.", title="Carga de archivos")

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "490", height = "400", relief = "ridge", bd = 12)

        # BUTTON------
        Button(self.frame, text = "Atrás", command=self.__regresar, width = 12, height = 1, font = ("Arial", 10), bg = "#E7C09C").place(x = 165, y = 320)
        self.__btn_MostrarGLC = Button(self.frame, text = "Mostrar GLC", command = self.__listaGLC, width = 12, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_MostrarGLC.place(x = 245, y = 10)
        self.frame.mainloop()

# (ARBOL DE DERIVACION)---------->
class AD_GLC(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Árbol de derivación GLC")
        super().centrar(self.ventana, 500, 600)
        self.ventana.geometry("500x580")# ANCHO X LARGO
        self.Ventana_frame()

    def __regresar(self):
        self.ventana.destroy()
        GLC()
    
    def myfunction(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=200,height=200)

    def funtionsCombo(self, event):
        var = event.widget.get()
        self.nombreGLC = var

        try:
            DB_GLC.graphviz(self.nombreGLC)
            self.img = tkinter.PhotoImage(file = './arboles_GLC/arbol_GLC.png')
            self.canvas.create_image(20, 20, image=self.img, anchor=NW)

        except:
            MB.showwarning(message="Seleccione una GLC para generar el grafo.", title="ERROR")

    def __listaGLC(self):
        try:
            listaAux = []
            for i in DB_GLC.lista_GLC:
                listaAux.append(i.nombre)

            # MENU DE GLC'S
            reports = ttk.Combobox(self.frame, width=18, height=5, values = listaAux, state='readonly')
            reports.place(x = 95, y = 12)
            reports.current(0)
            reports.bind('<<ComboboxSelected>>', self.funtionsCombo)
        except:
            MB.showwarning(message="Por favor, ingrese sus GLC.", title="Carga de archivos")

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "490", height = "580", relief = "ridge", bd = 12)

        ########################################333
        self.myframe=Frame(self.frame,relief=GROOVE,width=400,height=420,bd=2)
        self.myframe.place(x=20,y=60)
        self.myframe.pack_propagate(0)

        self.canvas=Canvas(self.myframe,bg='#EA6D9D',width=300,height=300,scrollregion=(0,0,390,1150))
        self.hbar=Scrollbar(self.canvas,orient=HORIZONTAL)
        self.hbar.pack(side=BOTTOM,fill=X)
        self.hbar.pack_propagate(0)
        self.hbar.config(command=self.canvas.xview)
        self.vbar=Scrollbar(self.canvas,orient=VERTICAL)
        self.vbar.pack(side=RIGHT,fill=Y)
        self.vbar.pack_propagate(0)
        self.vbar.config(command=self.canvas.yview)
        self.canvas.config(width=300,height=300)
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.pack(side=LEFT,expand=True,fill=BOTH)
        self.canvas.pack_propagate(0)
        #######################################33333

        # BUTTON------
        Button(self.frame, text = "Atrás", command=self.__regresar, width = 12, height = 1, font = ("Arial", 10), bg = "#E7C09C").place(x = 156, y = 492)
        self.__btn_MostrarGLC = Button(self.frame, text = "Mostrar GLC", command = self.__listaGLC, width = 12, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_MostrarGLC.place(x = 240, y = 10)

        self.frame.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------|




# ----------------------------------------------------------AUTOMATA DE PILA--------------------------------------------------------------------|
class AP(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Autómata de pila")
        super().centrar(self.ventana, 360, 330)
        self.ventana.geometry("360x310")# ANCHO X LARGO
        self.Ventana_frame() 

    def __ir_pantalla_CA(self):
        self.ventana.destroy()
        CA_AP()

    def __ir_pantalla_principal(self):
        self.ventana.destroy()
        Principal()

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "350", height = "315", relief = "ridge", bd = 12)

        # BUTTON------
        Button(self.frame, text = "Cargar Archivo", command=self.__ir_pantalla_CA, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 15, y = 10)
        Button(self.frame, text = "Ruta de Validación", width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 160, y = 10)
        Button(self.frame, text = "Información General", width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 15, y = 70)
        Button(self.frame, text = "Paso a Paso", width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 160, y = 70)
        Button(self.frame, text = "Validar Cadena", width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 15, y = 130)
        Button(self.frame, text = "Una Pasada", width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 160, y = 130)
        Button(self.frame, text = "Atrás", command=self.__ir_pantalla_principal,  width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 85, y = 198)
        
        self.frame.mainloop()

# (CARGAR ARCHIVO)---------->
class CA_AP(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Cargar Archivos AP")
        super().centrar(self.ventana, 300, 190)
        self.ventana.geometry("300x170")# ANCHO X LARGO
        self.Ventana_frame() 

    def __regresar(self):
        self.ventana.destroy()
        AP()
    
    def __cargarArchivo(self):
        try:
            Tk().withdraw()
            archivo = filedialog.askopenfilename(title = 'Select content image', filetypes= [('Archivo AP', '*.ap'), ('Archivo GR', '*.gre')])

            with open(archivo, 'r', encoding='utf-8') as file:

                texto = file.readlines()
                
                if texto == '':
                    MB.showerror('aviso', 'No existe datos en el archivo que ha seleccionado')
                    return 0

                confirmacion = DB_AP.leerArchivos(texto)

                if confirmacion != 0:
                    MB.showinfo(message="Se agrego correctamente!", title="Archivo leído")
                    self.ventana.destroy()
                    AP() 
        except:
            MB.showerror('Error', 'No ha cargado ningun archivo, por favor vuelva a internarlo')

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "305", height = "175", relief = "ridge", bd = 12)

        # BUTTON------
        self.__btn_cargarAFD = Button(self.frame, text = "Cargar archivo", command = self.__cargarArchivo, width = 15, height = 3, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_cargarAFD.place(x = 10, y = 25)

        self.__btn_Regresar = Button(self.frame, text = "Atrás", command = self.__regresar, width = 8, height = 3, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_Regresar.place(x = 158, y = 25)

        self.frame.mainloop()

# (RUTA DE VALIDACIÓN)---------->


# (INFORMACIÓN GENERAL)---------->


# (PASO A PASO)---------->


# (VALIDAR CADENA)---------->


# (UNA PASADA)---------->


# ----------------------------------------------------------------------------------------------------------------------------------------------|




# -------------------------------------------------------------------SALIR----------------------------------------------------------------------|
class salir(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Salir")
        super().centrar(self.ventana, 545, 285)
        self.ventana.geometry("545x270")
        self.Ventana_frame() 

    def MostrarVentana(self):
        if self.conta != 0:
            self.frame.config(bg = "#F9E1BE", width = "525", height = "250", relief = "ridge", bd = 12)
            self.label["text"] = f"Esta pantalla se destruirá en {self.conta} segundos."
            self.frame.after(1000, self.OcultarVentana)
        else:
            self.ventana.destroy()

        self.conta -= 1
        
    def OcultarVentana(self):
        self.frame.place_forget() 
        self.frame.after(100, self.MostrarVentana)

    def Ventana_frame(self):
        self.conta = 5
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "525", height = "250", relief = "ridge", bd = 12)

        # LABELS-----
        Label(self.frame, text = "Pantalla de despedida.", bg = "#F9E1BE", bd = 1, font = ("Arial", 15)).place(x = 140, y = 70)
        self.label = Label(self.frame, text = "Esta pantalla se destruirá en 5 segundos", bg = "#F9E1BE", bd = 0, font = ("Arial", 14))
        self.label.place(x = 70, y = 150)

        self.frame.after(100, self.OcultarVentana)
        self.frame.mainloop() 

# ----------------------------------------------------------------------------------------------------------------------------------------------|

Principal()