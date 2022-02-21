class Stack:                
    def __init__(self,tamanio):
        self.lista=[]
        self.tope=0
        self.size=tamanio
     
    def empty(self):
        # if self.tope == 0:
        #     return True
        # else:
        #     return False
        return self.tope == 0
    
    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La Pila está Llena")
   
    def pop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return top
            
    def longitud(self):
        return self.tope
        
    def show(self):
        if self.empty():
            print("Lista vacia")
        else:                    
            for tope in range(self.tope-1,-1,-1):
                print("[{}]".format(self.lista[tope]))    
    
    def buscar(self,buscado):
        if self.empty():
            print("La Pila está vacía")
        else:
            pi=False
            for pos,li in enumerate(self.lista):
                if li==buscado:
                    pi=True
                    break
            if pi==True:
                print("el numero se encuentra en : {}".format(pos+1))
                
            else:
                print("no se encuentra en la Pila")
#pila = Stack(5)
#pila.push("4")       
#ila.push("3")       
#pila.push("2")       
#pila.push("5")       
#pila.push("20")       
#pila.push("10")   
#pila.show()    
#print(pila.pop())
#print(pila.pop())
#print(pila.pop())
#print(pila.pop())
#print(pila.pop())
#print(pila.pop())#