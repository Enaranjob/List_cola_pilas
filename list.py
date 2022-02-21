class Lista:
    def __init__(self,datos=[]):
       self.lista = datos
        
    def push(self,dato):
        self.lista.append(dato)
    
    def eleminarElemento(self,pos):
        if pos < 0 or pos >= len(self.lista):
           return None
        else:    
           self.lista = self.lista[0:pos] + self.lista[pos+1:]
       
    def InsertarElemento(self,pos):
        self.lista.append(pos)
        if pos < 0 or pos >= len(self.lista):
               return None
        else:    
           self.lista = self.lista[posi:pos] + self.lista[pos+1:]
    
    def buscar(self,pos,buscado):
        if pos < 0 or pos > (len(self.lista)+1):
               return print("Posición incorrecta")
        else:    
            self.lista.insert(pos,buscado)
            print("El elemento insertado fue: '{}' en la posición: {}".format(elem,pos))
        return
        
    
    def mostrar(self):
        if self.empty():
            print("Lista vacia")
        else:  
            print("lista"," "*5,"Posicion")                
            for pos, e in enumerate(self.lista):
                print("[{:}] {:9}".format(e,pos))
                
    def empty(self):
        return len(self.lista) == 0
    
        
numeros = Lista()
numeros.push("Daniel")
numeros.push("Yady")
numeros.push("Ana")
numeros.push("Jose")
numeros.push("Moises")
posi = Lista()
posi.InsertarElemento = int(input("Ingresar la posicion"))

# ["Daniel","Jose","Yady","Ana"]    "miguel" 
#      0      1      2    len = 3
#            pos
numeros.eleminarElemento(1)
#print(numeros.pop())
#print(numeros.pop())
print(numeros.lista)