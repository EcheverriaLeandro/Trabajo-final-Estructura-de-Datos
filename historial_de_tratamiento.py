class Nodo_historial_tratamiento():    #realizamos un nodo con 2 datos para manejar de manera mas eficiente asociando la enfermedad con el medicamento del paciente en un mismo nodo
  def __init__(self,enfermedad,medicamento):
    self.enfermedad = enfermedad
    self.medicamento = medicamento
    self.siguiente = None
      
class Lista_historial_tratamiento():
  def __init__(self):
    self.head = None
    
  def nuevo_tratamiento(self, enfermedad, medicamento):  #cuando agregamos un nodo a nuestra lista cargamos tanto medicamento como enfermedad
    nuevo_tratamiento = Nodo_historial_tratamiento(enfermedad,medicamento)
    if self.head is None:
      self.head = nuevo_tratamiento
    else:
      actual = self.head
      while actual.siguiente != None:
        actual = actual.siguiente
      actual.siguiente = nuevo_tratamiento
      
  def busqueda_recursiva_enfermedad(self,lugar_de_busqueda,enfermedad): #busqueda a traves de enfermedad, devuelve enfermedad y medicamento asociado
    if lugar_de_busqueda is None:
      return ("No hay antecedentes")
    elif lugar_de_busqueda.enfermedad == enfermedad:
      return (f"El paciente tiene antesedentes de: {lugar_de_busqueda.enfermedad}, se lo trato con: {lugar_de_busqueda.medicamento}")
    else:
      return self.busqueda_recursiva_enfermedad(lugar_de_busqueda.siguiente, enfermedad)
      
  def busqueda_recursiva_medicamento(self,lugar_de_busqueda,medicamento): #busqueda a traves de medicamento, devuelve enfermedad y medicamento asociado
    if lugar_de_busqueda is None:
      return ("No hay antecedentes")
    elif lugar_de_busqueda.medicamento == medicamento:
      return (f"El paciente se trato con: {lugar_de_busqueda.medicamento}, luego de sufrir: {lugar_de_busqueda.enfermedad}")
    else:
      return self.busqueda_recursiva_medicamento(lugar_de_busqueda.siguiente, medicamento)