from pacientes import Pacientes


class Maxheap():
    def __init__(self):
        self.heap = []
    
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
        
    def mostrar_cola(self):
    
        print("Pacientes en la cola (prioridad descendente):")
        for i in self.heap:
            print(f"paciente :{i[1]} (Prioridad: {i[0]})")
         
# Crear una instancia de Maxheap
cola = Maxheap()

# Crear pacientes
paciente1 = Pacientes("Juan Pérez", 65)
paciente2 = Pacientes("María López", 70)
paciente3 = Pacientes("Carlos Ruiz", 50)

# Asignar prioridades (gravedad)
prioridad1 = 5  # Gravedad de Juan
prioridad2 = 8  # Gravedad de María
prioridad3 = 3  # Gravedad de Carlos

# Insertar pacientes en la cola
cola.insertar(3, paciente1)
cola.insertar(1, paciente2)
cola.insertar(3, paciente3)

# Mostrar la cola
cola.mostrar_cola()

# Atender pacientes según prioridad
print("\nAtendiendo pacientes:")
atendido = cola.extraer_maximo()
print(f"Atendido: {atendido[1]} (Prioridad: {atendido[0]})")

atendido = cola.extraer_maximo()
print(f"Atendido: {atendido[1]} (Prioridad: {atendido[0]})")

atendido = cola.extraer_maximo()
print(f"Atendido: {atendido[1]} (Prioridad: {atendido[0]})")

# Intentar atender a más pacientes
atendido = cola.extraer_maximo()
