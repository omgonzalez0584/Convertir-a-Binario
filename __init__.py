from tkinter import *
from tkinter import messagebox

def num_binario():
    r = Text()
    num = int(decimal.get())
    list = []
    mod = 0
    while num > 1:
        mod = int((num % 2))
        num = int((num / 2))
        list.append(str(mod))
    list.append((str(num)))
    list.reverse()
    print("".join(list))
    messagebox.showinfo("numero binario es ","".join(list))


ventana = Tk()
ventana.title("Convertir decimal a binario")
ventana.geometry("400x200")
decimal = StringVar()

etiqueta = Label(ventana, text= "Numero decimal: ", )
etiqueta.pack()
caja = Entry(ventana, textvariable = decimal)
caja.pack()
boton = Button(ventana,text = "Convertir", command = num_binario)
boton.pack()

boton_salir = Button(ventana,text="Salir",command = ventana.quit)
boton_salir.pack()

boton_siguiente = Button(ventana, text = "siguente")
boton_siguiente.pack()

ventana.mainloop()






