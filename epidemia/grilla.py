from tkinter import *
from collections import Counter
import random

class grilla(Frame):
    def __init__(self,master):
	    Frame.__init__(self,master)
	    self.grid(sticky=N+S+W+E)
	    self.grilla = {}

    def creargrilla(self,datos):
        " crear la grilla a partir de los datos dados "
        
        self.datos = datos
        self.cantidad = self.datos['cantidad']
        self.nacimiento = self.datos['nacimiento %']/100
        self.enferma = self.datos['enferma %']/100
        self.propagacion = self.datos['propagación %']/100
        self.fecundacion = self.datos['fecundación %']/100
        self.muerte = self.datos['muerte %']/100
        self.dias_enfermedad = self.datos['días enfermedad']
        self.dias_simulacion = self.datos['días simulacion']
        self.dias_totales = self.dias_simulacion
        contador = Counter()
        
        
        for i in range(self.cantidad):
            for j in range(self.cantidad):
                probabilidad = random.random()
                if probabilidad <= self.nacimiento:
                    probabilidad = random.random()
                    if probabilidad <= self.enferma:
                        self.grilla[(i,j)] = 1
                        contador['enfermas'] += 1
                    else:
                        self.grilla[(i,j)] = 0
                        contador['sanas'] += 1
                else:
                    self.grilla[(i,j)] = "."
                    contador['vacios'] += 1

        self.contador = contador

    def imprimirgrilla(self):
        " imprimir la grilla "
        for i in range(self.cantidad):
            for j in range(self.cantidad):
                if self.grilla[(i,j)] == ".":
                    l = Label(self,text=".",width=2,bg="white")
                elif self.grilla[(i,j)] == 0:
                    l =Label(self,text="0",width=2,bg="green")
                else:
                    l = Label(self,text=str(self.grilla[(i,j)]),width=2,bg="red")
                l.grid(row=i,column=j)
         

    def estadisticas(self,master):
        " genero las estadisticas, celulas sanas,enfermas,vacias "
        contador = self.contador
        self.sanas = Label(master,text="Dia: "+str(self.dias_totales - self.dias_simulacion))
        self.sanas.grid(row=0,column=0)
        self.sanas = Label(master,text="Celulas sanas: "+str(contador['sanas']))
        self.sanas.grid(row=1,column=0)
        self.enfermas = Label(master,text="Celulas enfermas: "+str(contador['enfermas']))
        self.enfermas.grid(row=2,column=0)
        self.vacios = Label(master,text="Espacios vacios: "+str(contador['vacios']))
        self.vacios.grid(row=3,column=0)
        

    def siguientedia(self):
        " genera la grilla del dia siguiente "
        nuevagrilla = {}
        contador_grl = Counter()
        for i in range(self.cantidad):
            for j in range(self.cantidad):
                contador = Counter()
                if self.grilla[(i,j)] == 0 or self.grilla[(i,j)] == ".":
                    vecinos = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
                    for v in vecinos:
                        if v in self.grilla:
                            contador[self.grilla[v]] += 1
                    if self.grilla[(i,j)] == 0:
                        enfermasvecinas = sum([x for x in contador.values()]) - (contador[0] + contador["."])
                        for k in range(enfermasvecinas):
                            prob = random.random()
                            if prob <= self.propagacion:
                                nuevagrilla[(i,j)] = 1 
                                contador_grl['enfermas'] += 1
                                break
                        else:
                            nuevagrilla[(i,j)] = 0
                            contador_grl['sanas'] += 1
                    else:
                        vecinas = sum([x for x in contador.values()]) - contador["."]
                        for k in range(vecinas):
                            prob = random.random()
                            if prob <= self.fecundacion:  
                                nuevagrilla[(i,j)] = 0
                                contador_grl['sanas'] += 1
                                break
                        else:
                            nuevagrilla[(i,j)] = "."
                            contador_grl['vacios'] += 1
                                    
                else:
                    prob = random.random()
                    if self.grilla[(i,j)] >= self.dias_enfermedad:
                        if prob <= self.muerte: 
                            nuevagrilla[(i,j)] = "."
                            contador_grl['vacios'] += 1
                        else:
                            nuevagrilla[(i,j)] = self.grilla[(i,j)] + 1
                            contador_grl['enfermas'] += 1
                    else:
                        nuevagrilla[(i,j)] = self.grilla[(i,j)] + 1
                        contador_grl['enfermas'] += 1
        self.grilla = nuevagrilla  
        self.contador = contador_grl
        self.dias_simulacion -= 1 
        self.imprimirgrilla()
                        
                        
                       
                        
                    
