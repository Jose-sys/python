from tkinter import *
import math

class vector(object):
    def __init__(self,xCoordenada,yCoordenada):
        self.xCoordenada = xCoordenada
        self.yCoordenada = yCoordenada

    def __str__(self):
        return "({0} {1})".format(self.xCoordenada,self.yCoordenada)

    def __add__(self,otro):
        return vector(self.xCoordenada + otro.xCoordenada,self.yCoordenada + otro.yCoordenada)

    def __iadd__(self,otro):
        self.xCoordenada += otro.xCoordenada
        self.yCoordenada += otro.yCoordenada
        return self

    def __rmul__(self,numero):
        return vector(self.xCoordenada * numero, self.yCoordenada * numero)

    def __imul__(self,numero):
        self.xCoordenada *= numero
        self.yCoordenada *= numero
        return self

    def __truediv__(self,escalar):
        if escalar != 0:
            self.xCoordenada /= escalar
            self.yCoordenada /= escalar
        return self

    def __itruediv__(self,escalar):
        if escalar != 0:
            self.xCoordenada /= escalar
            self.yCoordenada /= escalar
        return self

    def __abs__(self):
        return math.sqrt(self.xCoordenada**2+self.yCoordenada**2)

    def __sub__(self,otro):
        return vector(self.xCoordenada - otro.xCoordenada,self.yCoordenada - otro.yCoordenada)

    def __isub__(self,otro):
        self.xCoordenada -= otro.xCoordenada
        self.yCoordenada -= otro.yCoordenada
        return self

    def __ne__(self,otro):
        return self.xCoordenada != otro.xCoordenada or self.yCoordenada != otro.yCoordenada

    def normalizar(self):
        return vector(self.xCoordenada/abs(self),self.yCoordenada/abs(self))

    def paint(self):
        return (round(self.xCoordenada-10), round(self.yCoordenada+10), round(self.xCoordenada+10), round(self.yCoordenada-10))



class pelota(object):
	def __init__(self):
		x = 345
		y = 445 
		self.posicion = vector(x,y)
		self.velocidad = vector(0.7,0.1)
		self.oval = None

class Pong(Frame):
        def __init__(self,master=None):
                Frame.__init__(self,master)
                self.grid(sticky=N+S+W+E)
                self.canvas = Canvas(self, width=1000,height=600, background="#dedede")
                self.canvas.grid(row=1,column=1,columnspan=4)
                self.puntaje_j1 = 0
                self.puntaje_j2 = 0
                self.generarpuntajes()
                self.generarjugadores()
                self.generar_pelota()

        def generarpuntajes(self):
                self.puntaje_j1_label = Label(self,text=self.puntaje_j1,width=71,height=2,relief=SUNKEN,bg="black",fg="green")
                self.puntaje_j1_label.grid(row=0,column=1,columnspan=2)
                self.puntaje_j2_label = Label(self,text=self.puntaje_j2,width=71,height=2,relief=SUNKEN,bg="black",fg="green")
                self.puntaje_j2_label.grid(row=0,column=3,columnspan=2)
                if self.puntaje_j2 < self.puntaje_j1:
                    self.puntaje_j2_label.config(fg="red")
                    self.puntaje_j1_label.config(fg="green")
                elif self.puntaje_j1 < self.puntaje_j2:
                    self.puntaje_j2_label.config(fg="green")
                    self.puntaje_j1_label.config(fg="red")
                else:
                    self.puntaje_j2_label.config(fg="green")
                    self.puntaje_j1_label.config(fg="green")

        def generarjugadores(self):
                self.j1 = self.canvas.create_rectangle(25, 25, 50, 205, fill="black")
                self.j2 = self.canvas.create_rectangle(975,25,950,205, fill="pink")
                self.bind_all("<Key>",self.mover)

        def generar_pelota(self):
                self.pelota = pelota()
                oval = self.canvas.create_oval(self.pelota.posicion.paint(),fill="#FF0000")
                self.pelota.oval = oval
                while True:
                        if self.puntaje_j2 < self.puntaje_j1:
                            if self.puntaje_j2_label.cget("fg") == "white":
                                self.puntaje_j2_label.config(fg="red")
                            else:
                                self.puntaje_j2_label.config(fg="white")
                        elif self.puntaje_j1 < self.puntaje_j2:
                            if self.puntaje_j1_label.cget("fg") == "red":
                                self.puntaje_j1_label.config(fg="white")
                            else:
                                self.puntaje_j1_label.config(fg="red")
                        self.pelota.posicion += 0.1 * self.pelota.velocidad
                        self.canvas.coords(self.pelota.oval,self.pelota.posicion.paint())
                        if self.pelota.posicion.xCoordenada >= self.canvas.coords(self.j2)[0] and self.pelota.posicion.yCoordenada >= self.canvas.coords(self.j2)[1] and self.pelota.posicion.yCoordenada <= self.canvas.coords(self.j2)[1] + 205:
                                 self.pelota.velocidad.xCoordenada *= -1
                                 self.pelota.velocidad.xCoordenada -= 0.05
                        if self.pelota.posicion.xCoordenada <= self.canvas.coords(self.j1)[0] + 25 and self.pelota.posicion.yCoordenada >= self.canvas.coords(self.j1)[1] and self.pelota.posicion.yCoordenada <= self.canvas.coords(self.j1)[1] + 205:
                                self.pelota.velocidad.xCoordenada *= -1
                                self.pelota.velocidad.xCoordenada += 0.05
                        elif self.pelota.posicion.xCoordenada >= 1000:
                                self.pelota.posicion.xCoordenada = 500
                                self.pelota.posicion.yCoordenada = 300
                                self.pelota.velocidad = vector(0.7,0.1)
                                self.pelota.velocidad.xCoordenada *= -1
                                self.puntaje_j1 += 1
                                self.generarpuntajes()
                        elif self.pelota.posicion.xCoordenada <= 0:
                                self.pelota.posicion.xCoordenada = 500
                                self.pelota.posicion.yCoordenada = 300
                                self.pelota.velocidad = vector(0.7,0.1)
                                self.pelota.velocidad.xCoordenada *= -1
                                self.puntaje_j2 += 1
                                self.generarpuntajes()
                        elif self.pelota.posicion.yCoordenada >= 600 or self.pelota.posicion.yCoordenada <= 0 :
                                self.pelota.velocidad.yCoordenada *= -1
                        self.canvas.update()
                        
                        
        def mover(self,e):
                tecla = e.char
                velocidad = 15
                if tecla == 's':
                        coords = self.canvas.coords(self.j1)
                        if coords[1] <= 409:
                                self.canvas.coords(self.j1,coords[0],coords[1]+1+velocidad,coords[0]+25,coords[3]+1+velocidad)
                elif tecla == 'w':
                        coords = self.canvas.coords(self.j1)
                        if coords[1] >= 0:
                                self.canvas.coords(self.j1,coords[0],coords[1]-1-velocidad,coords[0]+25,coords[3]-1-velocidad)
                elif tecla == 'l':
                        coords = self.canvas.coords(self.j2)
                        if coords[1] <= 409:
                                self.canvas.coords(self.j2,coords[0],coords[1]+1+velocidad,coords[0]+25,coords[3]+1+velocidad)
                elif tecla == 'o':
                        coords = self.canvas.coords(self.j2)
                        if coords[1] >= 0:
                                self.canvas.coords(self.j2,coords[0],coords[1]-1-velocidad,coords[0]+25,coords[3]-1-velocidad)

                
                self.canvas.update()

pong = Pong()
pong.mainloop()
