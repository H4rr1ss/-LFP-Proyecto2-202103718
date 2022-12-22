import tkinter as tk

class WindowExample(tk.Tk): 
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Agregar los widgets....

        self.labelExample = tk.Label(self, text="Este es un ejemplo de un widget (en este caso un label)")
        self.labelExample.place(x=13, y=15)

        HideLabelButton = tk.Button(self, text="Ocultar el label", command=self.HideLabel)
        ShowLabelButton = tk.Button(self, text="Mostrar el label", command=self.ShowLabel)

        HideLabelButton.place(x=485, y=12)
        ShowLabelButton.place(x=359, y=12)

    def ShowLabel(self): # Mostrar los widgets por medio de esta función al hacer clic
        self.labelExample.place(x=13, y=15)

    def HideLabel(self): # Ocultar los widgets por medio de esta función al hacer clic
        self.labelExample.place_forget() 

if __name__ == "__main__":
    root = WindowExample()
    root.title('Ejemplo ventana: Ocultar y mostrar widgets')
    root.geometry('600x80')
    root.resizable(0,0)
    root.mainloop() # Fin ciclo de eventos



'''import tkinter as tk

root = tk.Tk()
root.geometry('400x400')
root.title('Esta ventana se va a cerrar...')


def MostrarVentana():
    root.iconify()
    root.deiconify()
    root.title('Ventana visible de nuevo') # Renombrar título de la ventana al volverla a iniciar.

def OcultarVentana():
    root.withdraw()
    root.after(3000, MostrarVentana)


root.after(3000, OcultarVentana) # Dentro de 3s más o menos inicia la función de eliminación u desaparición de la ventana
root.mainloop()'''