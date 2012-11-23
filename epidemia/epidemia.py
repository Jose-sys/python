from tkinter import *
from grilla import *

class App(Frame):
        def __init__(self,master=None):
                Frame.__init__(self,master)
                self.grid(sticky=N+S+W+E)
                self.fin = False
                self.crearventana()
                
        def crearventana(self):
                valores = ['cantidad','nacimiento %','enferma %','propagación %','fecundación %','muerte %','días enfermedad','días simulacion']
                self.entrys = {}
                for i in valores:
                        Label(self,text=i).grid(row=0,column=valores.index(i))
                        self.entrys[i] = Entry(self)
                        self.entrys[i].grid(row=1,column=valores.index(i))
                        
                Button(self,text="Generar",command=self.generar).grid(row=1,column=len(valores))
                self.group = LabelFrame(self, padx=10,text="Grilla", pady=10)
                self.estadisticas = LabelFrame(self, padx=10,text="Estadisticas", pady=10)
                self.grilla = grilla(self.group)
                self.siguientedia = Button(self,text="Siguiente dia",command=self.siguientedia)
                self.fin_label = Label(self,fg="red",text="")
                self.fin_label.grid(row=3,column=0,columnspan=3)
                
        def generar(self):

                if self.fin:
                        self.fin_label.config(text="")
                        self.siguientedia.config(state=ACTIVE)
                        self.fin = False

                datos = {}
                for x,y in self.entrys.items():
                        if y.get().isdigit() and int(y.get()) >= 0 and int(y.get()) <= 100:
                                datos[x] = int(y.get())
                        else:
                                datos[x] = 0

                
                self.grilla.destroy()
                self.grilla = grilla(self.group) 
                self.grilla.creargrilla(datos)
                self.grilla.imprimirgrilla()
                self.group.grid(row=2,column=0,columnspan=3)
                self.estadisticas.grid(row=2,column=5,columnspan=3) 
                self.grilla.estadisticas(self.estadisticas)
                self.siguientedia.grid(row=2,column=3,columnspan=2) 
                self.finsimulacion() 

        def siguientedia(self):
                if not self.fin:
                        self.grilla.siguientedia()  
                        self.estadisticas.grid_forget() 
                        self.estadisticas.grid(row=2,column=5,columnspan=3) 
                        self.grilla.estadisticas(self.estadisticas)
                        self.finsimulacion()
                        

        def finsimulacion(self):
                if self.grilla.dias_simulacion == 0:
                        self.fin_label.config(text="FIN DE LA SIMULACION (Limite de dias)")          
                elif self.grilla.contador['enfermas'] == 0 and self.grilla.contador['sanas'] == 0:
                        self.fin_label.config(text="FIN DE LA SIMULACION (No hay poblacion)")
                elif self.grilla.contador['enfermas'] == 0:
                        self.fin_label.config(text="FIN DE LA SIMULACION (No hay celulas enfermas)")
                else:
                        return False
                self.siguientedia.config(state=DISABLED)
                self.fin = True
                

epidemia = App()
epidemia.master.title("Simulacion de Epidemia")
epidemia.mainloop()
