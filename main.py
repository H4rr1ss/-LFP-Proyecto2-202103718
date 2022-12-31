from tkinter import *
from tkinter import ttk, Tk, filedialog
import tkinter
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
        self.__tbn_moduloGLC = Button(self.frame, text = "Módulo GLC", command= self.__ir_pantalla_GLC, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__tbn_moduloGLC.place(x = 40, y = 31)

        self.__btn_moduloAP = Button(self.frame, text = "Módulo AP", command=self.__ir_pantalla_AP, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_moduloAP.place(x = 40, y = 102)

        self.__tbn_salir = Button(self.frame, text = "Salir", command=self.__ir_pantalla_salir, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C")
        self.__tbn_salir.place(x = 40, y = 173)

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

                if confirmacion is True:
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
        self.nombreGLC = event.widget.get()

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

    def __ir_pantalla_VC(self):
        self.ventana.destroy()
        EvaluarCadena_AP()

    def __ir_pantalla_IG(self):
        self.ventana.destroy()
        IG_AP()

    def __ir_pantalla_RV(self):
        self.ventana.destroy()
        RV_AP()

    def __ir_pantalla_PaP(self):
        self.ventana.destroy()
        PAP_AP()

    def __ir_pantalla_principal(self):
        self.ventana.destroy()
        Principal()

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "350", height = "315", relief = "ridge", bd = 12)

        # BUTTON------
        Button(self.frame, text = "Cargar Archivo", command=self.__ir_pantalla_CA, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 15, y = 10)
        Button(self.frame, text = "Ruta de Validación", command=self.__ir_pantalla_RV, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 160, y = 10)
        Button(self.frame, text = "Información General", command=self.__ir_pantalla_IG, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 15, y = 70)
        Button(self.frame, text = "Paso a Paso", command=self.__ir_pantalla_PaP, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 160, y = 70)
        Button(self.frame, text = "Validar Cadena", command=self.__ir_pantalla_VC, width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 15, y = 130)
        Button(self.frame, text = "Una Pasada", width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 160, y = 130)
        Button(self.frame, text = "Atrás", command=self.__ir_pantalla_principal,  width = 14, height = 2, font = ("Arial", 10), bg = "#E7C09C").place(x = 85, y = 198)
        
        self.frame.mainloop()

# (CARGAR ARCHIVO)--------------->
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

                if confirmacion is True:
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

# (VALIDAR CADENA)--------------->
class EvaluarCadena_AP(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Evaluar Cadena")
        super().centrar(self.ventana, 320, 320)
        self.ventana.geometry("320x300")# ANCHO X LARGO
        self.Ventana_frame()   

    def __ir_pantalla_menu(self):
        self.ventana.destroy()
        AP()      

    def funtionsCombo(self, event):
        var = event.widget.get()
        self.nombreAFD = var

    def __evaluarCadena(self):
        try:
            cadena = self.__tb_validar.get()

            if cadena == '':
                MB.showwarning(message="No ha ingresado nada para evaluar.", title="Revise los campos de texto")
                return 

            DB_AP.validarCadena(self.nombreAFD, cadena)
        except:
            MB.showerror(message="Por favor, elija un AP.", title="ERROR")

    def __listaAP(self):
        try:
            listaAux = []
            for i in DB_AP.lista_AP:
                listaAux.append(i.getNombre())

            # MENU DE AP
            reports = ttk.Combobox(self.frame, width=18, height=5, values = listaAux, state='readonly')
            reports.place(x = 62, y = 45)
            reports.current(0)
            reports.bind('<<ComboboxSelected>>', self.funtionsCombo)
        except:
            MB.showwarning(message="Por favor, ingrese sus automata pila.", title="Carga de archivos")
            
    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "310", height = "320", relief = "ridge", bd = 12)

        # LABLES------
        Label(self.frame, text = "Solo Validar:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 85, y = 86)

        # JTEXFIELD------
        self.__tb_validar = Entry(self.frame, font = ("Comic Sans MS", 10), width = 17, justify = "center")
        self.__tb_validar.place(x = 60, y = 110)

        # BUTTON------
        self.__btn_Regrasar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_menu, width = 26, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_Regrasar.place(x = 36, y = 200)
        self.__btn_SoloValidar = Button(self.frame, text = "Validar", command = self.__evaluarCadena, width = 8, height = 1, font = ("Arial", 8), bg = "#E7C09C")
        self.__btn_SoloValidar.place(x = 100, y = 140)
        self.__btn_MostrarAFD = Button(self.frame, text = "Mostrar AP'S", command = self.__listaAP, width = 12, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_MostrarAFD.place(x = 80, y = 10)

        self.frame.mainloop()

# (INFORMACIÓN GENERAL)---------->
class IG_AP(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Mostrar info.")
        super().centrar(self.ventana, 300, 310)
        self.ventana.geometry("300x290")# ANCHO X LARGO
        self.Ventana_frame() 

    def __regresar(self):
        self.ventana.destroy()
        AP()

    def funtionsCombo(self, event):
        self.nombreAP = event.widget.get()

    def __listaAP(self):
        try:
            listaAux = []
            for i in DB_AP.lista_AP:
                listaAux.append(i.getNombre())

            # MENU DE AP
            reports = ttk.Combobox(self.frame, width=15, height=5, values = listaAux, state='readonly')
            reports.place(x = 15, y = 24)
            reports.current(0)
            reports.bind('<<ComboboxSelected>>', self.funtionsCombo)
        except:
            MB.showwarning(message="Por favor, ingrese sus automata pila.", title="Carga de archivos")
            
    def __graphviz(self):
        try:
            DB_AP.graphviz(self.nombreAP)
        except:
            print('ERROR')

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "290", height = "280", relief = "ridge", bd = 12)

        # BUTTON------
        self.__btn_motrarAP = Button(self.frame, text = "Mostrar AP'S", command = self.__listaAP, width = 10, height = 1, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_motrarAP.place(x = 143, y = 20)

        self.__btn_generarReporte = Button(self.frame, text = "Generar reporte", command = self.__graphviz, width = 13, height = 3, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_generarReporte.place(x = 60, y = 110)

        self.__btn_atras = Button(self.frame, text = "Atrás", command = self.__regresar, width = 6, height = 1, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_atras.place(x = 90, y = 195)

        self.frame.mainloop()

# (PASO A PASO)------------------>
class PAP_AP(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Paso a Paso")
        super().centrar(self.ventana, 650, 430)
        self.ventana.geometry("650x410")# ANCHO X LARGO
        self.Ventana_frame() 

    def __regresar(self):
        self.ventana.destroy()
        AP()

    def funtionsCombo(self, event):
        self.nombreAP = event.widget.get()

    def myfunction(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=200,height=200)

    def __listaAP(self):
        try:
            listaAux = []
            for i in DB_AP.lista_AP:
                listaAux.append(i.getNombre())

            # MENU DE AP
            reports = ttk.Combobox(self.frame, width=30, height=5, values = listaAux, state='readonly')
            reports.place(x = 120, y = 12)
            reports.current(0)
            reports.bind('<<ComboboxSelected>>', self.funtionsCombo)
        except:
            MB.showwarning(message="Por favor, ingrese sus automata pila.", title="Carga de archivos")
            
    def __graficarPasos(self):
        try:
            if self.__tb_validar.get() != '':
                self.cantImas = DB_AP.validarCadenaPAP(self.nombreAP, self.__tb_validar.get())
                self.contSiguientes = 2
                self.img = tkinter.PhotoImage(file = './Grafos/pasos_AP/extras/ap1.png')
                self.canvas.create_image(1, 1, image=self.img, anchor=NW)
        except:
            print('ERROR')

    def __btn_siguiente(self):
        try:
            if self.contSiguientes <= self.cantImas:
                self.img = tkinter.PhotoImage(file = f'./Grafos/pasos_AP/extras/ap{str(self.contSiguientes)}.png')
                self.canvas.create_image(1, 1, image=self.img, anchor=NW)
                self.contSiguientes += 1
            else:
                MB.showwarning(message=f"Ya no hay más imagenes.", title="CUIDADO")
        except:
            print("ERROR")

    def Ventana_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "640", height = "400", relief = "ridge", bd = 12)

        self.myframe=Frame(self.frame,relief=GROOVE,width=551,height=240,bd=2)
        self.myframe.place(x=22,y=99)
        self.myframe.pack_propagate(0)

        self.canvas=Canvas(self.myframe,bg='#FEF4E6',width=550,height=240,scrollregion=(0,0,540,270))
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


        # LABEL-------
        Label(self.frame, text = "Autómata", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 26, y = 10)
        Label(self.frame, text = "Cadena", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 26, y = 55)

        # BUTTON------
        self.__btn_motrarAP = Button(self.frame, text = "Mostrar AP'S", command = self.__listaAP, width = 10, height = 1, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_motrarAP.place(x = 353, y = 9)

        self.__btn_generarReporte = Button(self.frame, text = "Validar", command = self.__graficarPasos, width = 10, height = 1, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_generarReporte.place(x = 353, y = 50)

        self.__btn_sig = Button(self.frame, text = "Siguiente", command=self.__btn_siguiente, width = 9, height = 1, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_sig.place(x = 476, y = 9)

        self.__btn_atras = Button(self.frame, text = "Salir", command = self.__regresar, width = 9, height = 1, font = ("Arial", 10), bg = "#E7C09C")
        self.__btn_atras.place(x = 476, y = 50)

        # JTEXTFIELD--
        self.__tb_validar = Entry(self.frame, font = ("Comic Sans MS", 10), width = 25, justify = "center")
        self.__tb_validar.place(x = 120, y = 57)

        self.frame.mainloop()

# (RUTA DE VALIDACIÓN)----------->
class RV_AP(Menu):
    def __init__(self):
        super().General_ventana()
        self.ventana.title("Ruta de validación")
        super().centrar(self.ventana, 370, 410)
        self.ventana.geometry("370x390")# ANCHO X LARGO
        self.Ventana_frame()   

    def __ir_pantalla_menu(self):
        self.ventana.destroy()
        AP()      

    def funtionsCombo(self, event):
        self.nombreAFD = event.widget.get()
        if self.contador != 1:
            self.__ruta["text"] = ""

    def __rutaValidacion(self):
        try:
            self.cadena = self.__tb_validar.get()

            if self.cadena == '':
                MB.showwarning(message="No ha ingresado nada para evaluar.", title="Revise los campos de texto")
                return 

            ruta = DB_AP.validarRuta(self.nombreAFD, self.cadena)
            
            if ruta is not None:
                self.__ruta = Label(self.frame, text = ruta, bg = "#F9E1BE", font = ("Comic Sans MS", 10))
                self.__ruta.place(x = 119, y = 100)
                self.contador += 1
        except:
            MB.showerror(message="Por favor, elija un AP.", title="ERROR")

    def __listaAP(self):
        try:
            listaAux = []
            for i in DB_AP.lista_AP:
                listaAux.append(i.getNombre())

            # MENU DE AP
            reports = ttk.Combobox(self.frame, width=18, height=5, values = listaAux, state='readonly')
            reports.place(x = 170, y = 45)
            reports.current(0)
            reports.bind('<<ComboboxSelected>>', self.funtionsCombo)
        except:
            MB.showwarning(message="Por favor, ingrese sus automata pila.", title="Carga de archivos")
            
    def Ventana_frame(self):
        self.contador = 1
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bg = "#F9E1BE", width = "360", height = "380", relief = "ridge", bd = 12)

        # LABLES------
        Label(self.frame, text = "Cadena:", bg = "#F9E1BE", font = ("Comic Sans MS", 10)).place(x = 15, y = 15)

        # JTEXFIELD------
        self.__tb_validar = Entry(self.frame, font = ("Comic Sans MS", 10), width = 17, justify = "center")
        self.__tb_validar.place(x = 12, y = 40)

        # BUTTON------
        self.__btn_Regrasar = Button(self.frame, text = "Regresar", command = self.__ir_pantalla_menu, width = 26, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_Regrasar.place(x = 60, y = 301)
        self.__btn_validar = Button(self.frame, text = "Validar ruta", command = self.__rutaValidacion, width = 28, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_validar.place(x = 55, y = 267)
        self.__btn_MostrarAFD = Button(self.frame, text = "Mostrar AP'S", command = self.__listaAP, width = 12, height = 1, font = ("Arial", 9), bg = "#E7C09C")
        self.__btn_MostrarAFD.place(x = 188, y = 10)

        self.frame.mainloop()

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

Menu()