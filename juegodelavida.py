# ocupada con menos de 2 vecinos -> muere
# ocupada con mas de 3 vecinos -> muere
# no ocupado con 3 vecinos -> ocupada
# inicializar poner ocupantes randomicamente

import random,time,os

class life(object):
        def __init__(self,n):
                self.dic = {}
                self.n = n

        def imprimir(self):
                
                for i in range(self.n):
                        linea = ""
                        for j in range(self.n):
                                if (i,j) in self.dic:
                                        linea += " {0:1}".format("*")
                                else:
                                        linea += " {0:1}".format(" ")
                        print (linea)
                print("="*self.n*2)

        def inicializar(self,prob):
                for i in range(self.n):
                        for j in range(self.n):
                                if random.random() < prob:
                                        self.dic[(i,j)] = True

        def actualizar(self):
                newdic = {}
                for i in range(self.n):
                        for j in range(self.n):
                                vecinos = 0
                                if (i-1,j-1) in self.dic:
                                  vecinos += 1
                                if (i-1,j) in self.dic:
                                	vecinos += 1
                                if (i-1,j+1) in self.dic:
                                	vecinos += 1
                                if (i,j-1) in self.dic:
                                	vecinos += 1
                                if (i,j+1) in self.dic:
                                	vecinos += 1
                                if (i+1,j-1) in self.dic:
                                	vecinos += 1
                                if (i+1,j) in self.dic:
                                	vecinos += 1
                                if (i+1,j+1) in self.dic:
                                	vecinos += 1
                                if (i,j) in self.dic and (vecinos == 2 or vecinos == 3):
                                	newdic[(i,j)] = True
                                if (i,j) not in self.dic and vecinos == 3:
                                	newdic[(i,j)] = True
                self.dic = newdic

a = life(20)
a.inicializar(0.5)
while True: 
        a.actualizar()
        time.sleep(1)
        a.imprimir()

