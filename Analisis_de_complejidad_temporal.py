    
    este modulo pertenece a nuestro arbol general y es del orden de O(n**2) porque tenemos ciclos anidados
    
    def imprimir_arbol_con_hermanos(self, nodo, nivel=0): #recorrido preorder 
        #imprime el nodo considerando hijos y hermanos 
        while nodo:                              -->                       O(n)
            print("  " * nivel + f"- {nodo.evento}")                               
            for hijo in nodo.hijos:              -->                       O(m)
                self.imprimir_arbol_con_hermanos(hijo, nivel + 1)
            nodo = nodo.hermano
                                                                           entonces este metodo tiene un timpo O(m*n) por lo tanto suponiendo que n>m se podria decir que su complejidad temporal es O(n**2)
    
    
_________________________________________________________________________________________________________________________________________________________________________________________________________________
    para calcular el big Oh de la insersion en nuestro arbolAVL es mas complejo porque el metodo de insersion depende de otros metodos
    

    def __obtener_altura(self, nodo): #metodo necesario para obtener la altura de nuestros nodos
        if not nodo:
            return 0
        return nodo.altura       --->     el total de este metodo corresponde a O(1)
    
    def __obtener_balance(self, nodo): #metodo necesario para luego comparar el desbalance o no de nuestros nodos
        if not nodo:
            return 0
        return self.__obtener_altura(nodo.derecho) - self.__obtener_altura(nodo.izquierdo) ---> este metodo tambien corresponde a O(1) 
    
    def __rotar_derecha(self, nodo): #metodo para hacer que el hijo izquierdo sea la nueva raiz y reajusta la altura de los nodos
        nueva_raiz = nodo.izquierdo
        arbol_derecho_auxiliar = nueva_raiz.derecho
        
        nueva_raiz.derecho = nodo
        nodo.izquierdo = arbol_derecho_auxiliar
        
        nodo.altura = 1 + max(self.__obtener_altura(nodo.izquierdo), self.__obtener_altura(nodo.derecho))
        nueva_raiz.altura = 1 + max(self.__obtener_altura(nueva_raiz.izquierdo), self.__obtener_altura(nueva_raiz.derecho))
        
        return nueva_raiz    ---> si bien los metodos de rotacion son mas complejos solo estamos moviendo valores, por lo tanto tambien tienen un valor de O(1)
    
    def __rotar_izquierda(self, nodo): #metodo para hacer que el hijo derecho sea la nueva raiz y reajusta la altura de los nodos
        nueva_raiz = nodo.derecho
        arbol_izquierdo_auxiliar = nueva_raiz.izquierdo
        
        nueva_raiz.izquierdo = nodo
        nodo.derecha = arbol_izquierdo_auxiliar
        
        nodo.altura = 1 + max(self.__obtener_altura(nodo.izquierdo), self.__obtener_altura(nodo.derecho))
        nueva_raiz.altura = 1 + max(self.__obtener_altura(nueva_raiz.izquierdo), self.__obtener_altura(nueva_raiz.derecho))
        
        return nueva_raiz  ---> la rotacion a la izquierda funciona del mismo modo que la rotacion a la derecha

    def __insertar_nodo (self, raiz, nuevo_nodo): #Metodo privado
        if not raiz:
            return NodoPaciente(nuevo_nodo)   ---> en este caso insertar el nodo seria O(1) pero mas adelante
        
        if nuevo_nodo.id < raiz.paciente.id:                                                                #
            raiz.izquierdo = self.__insertar_nodo(raiz.izquierdo, nuevo_nodo)                               # pero ya en esta seccion del codigo ya la complejidad temporal aumenta
        else:                                                                                               # devido a que se realiza una recursion para encontrar el lugar a ocupar por el nodo
            raiz.derecho = self.__insertar_nodo(raiz.derecho, nuevo_nodo)                                   # al estar dividiendo el arbol en cada una de las busqueda acotando el posible resultado pertenece al orden de O(log n)
                                                                                                            
        raiz.altura = 1 + max(self.__obtener_altura(raiz.izquierdo), self.__obtener_altura(raiz.derecho))
        
        balance = self.__obtener_balance(raiz)
        
        #rotacion a la derecha
        if balance > 1 and nuevo_nodo.id < raiz.izquierdo.id:
            return self.__rotar_derecha(raiz)
        #rotacion a la izquierda
        if balance < -1 and nuevo_nodo.id > raiz.izquierdo.id:
            return self.__rotar_izquierda(raiz)
        #rotacion izquierda derecha
        if balance > 1 and nuevo_nodo.id > raiz.izquierdo.id:
            raiz.izquierdo = self.__rotar_izquierda(raiz.izquierdo)
            return self.__rotar_derecha(raiz)
        #rotacion derecha izquierda
        if balance < -1 and nuevo_nodo.id < raiz.derecho.id:
            raiz.derecho = self.__rotar_derecha(raiz.derecho)
            return self.__rotar_izquierda(raiz)
    
        return raiz
    
    def insersion(self, paciente): #metodo publico de insersion 
        self.raiz = self.__insertar_nodo(self.raiz, paciente)  ---> por lo tanto como el caso de mayor complejidad temporal es O(log n) este es el orden al que pertenece el metodo de insersion de nuestro arbol
    
________________________
        
    para poder analizar la eficiencia en terminos de tiempo y espacio del algoritmo que realizamos para la busqueda en cola de prioridad, primero debemos establecer que nosotros hemos tomado la decision de utilizar una estructura tipo Max Heap para poder ordenar los pacientes que requieren una atencion de mayor urgencia. por lo tanto no era necesario realizar de por si una busqueda debido a que la misma estructura ordena de forma ascendente los datos ingresados y eso lo realizamos extrayendo el primer dato del monticulo. Para ello utilizamos el siguiente modulo: 
    def extraer_maximo(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            raiz = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.__burbujeo_abajo(0)
            return raiz
que a su vez este codigo utiliza la funcion burbuejo abajo 

def __burbujeo_abajo(self, index):
        izquierdo = 2*index+1
        derecho = 2*index+2
        mayor = index
        
        if izquierdo < len(self.heap) and self.heap[izquierdo][0] > self.heap[mayor][0]:
            mayor = izquierdo
        if derecho < len(self.heap) and self.heap[derecho][0] > self.heap[mayor][0]:
            mayor = derecho
        if mayor != index:
            self.__intercambio(index, mayor)
            self.__burbujeo_abajo(mayor)
_________________________________________________________________________________________________________________________________________________________________________________________________________________