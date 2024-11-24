import pacientes

class Maxheap():
    def __init__(self):
        heap = []
    
    def __intercambio(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def __burbujeo_arriba(self, index):
        padre = (index - 1) // 2
        if index > 0 and self.heap[index][0] > self.heap[padre][0]:
            self.__intercambio(index, padre)
            self.__burbujeo_arriba(padre)

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
            
    def insertar(self, prioridad, paciente):
            self.heap.append((prioridad, paciente))
            self.__burbujeo_arriba(len(self.heap)-1)
            
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