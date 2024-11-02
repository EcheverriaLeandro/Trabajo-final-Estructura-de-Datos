class Nodo_historial_tratamiento():
      
  def __init__(self,enfermedad,medicacion):
    self.enfermedad = enfermedad
    self.medicacion = medicacion
    self.siguiente = None
      
class Lista_historial_tratamiento():
  
  def __init__(self):
    self.head = None
    
  def agregar_tratamiento(self, enfermedad, medicaion):
    nuevo_tratamiento = Nodo_historial_tratamiento(enfermedad,medicaion)
    if self.head is None:
      self.head = nuevo_tratamiento
    else:
      actual = self.head
      while actual.siguiente != None:
        actual = actual.siguiente
      actual.siguiente = nuevo_tratamiento