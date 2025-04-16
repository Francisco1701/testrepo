#crear la clase con la palabra reservada class
class Auto:
    #crear los atributos
    #dentro del constructor predeterminado de python __init__
    def __init__(self, n="Minicooper", c="purpura", m=2022, t="Mini", f="Compacto"):      # void init()
        self.__Nombre = n
        self.__Color = c
        self.__Modelo = m
        self.__Tamanio = t
        self.__Forma = f
        
    #Setter y Getter despues del constructor
    #Setter utilizan la etiqueta @Representate.Setter
    #Getter utilizan la etiqueta @property
    #1ero los Getter e inmediato los Setter
    
    @property #GETTER
    def name(self):
        return self.__Nombre
        
    @name.setter
    def name(self, n):
        self.__Nombre = n
        
    @property
    def color(self):
        return self.__Color
            
    @color.setter
    def color(self, c):
        self.__Color = c
        
    @property
    def mod(self):
        return self.__Modelo
            
    @color.setter
    def mod(self, m):
        self.__Modelo = m
        
    @property
    def size(self):
        return self.__Color
            
    @size.setter
    def size(self, t):
        self.__Tamanio = t
    
    @property
    def shape(self):
        return self.__Forma
            
    @shape.setter
    def shape(self, f):
        self.__Forma = f
    
    
        #Definir los metodos
    def imprimir(self):
        print("Nombre: ", self.__Nombre)
        print("Color: ", self.__Color)
        print("Modelo: ", self.__Modelo)
        print("Tamaño: ", self.__Tamanio)
        print("Forma: ", self.__Forma)
        print()
        
    def mover(self):
        print("El auto se esta moviendo")
        
    def frenar(self):
        print("El auto", self.__Nombre, "freno")
        
    def girarD(self):
        print("Girar a la derecha continua con precaucion")
        
    def girarI(self):
        print("Girar a la izquierda si quiere rebasar")