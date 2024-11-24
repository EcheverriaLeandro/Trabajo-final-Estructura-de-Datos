import historial_de_tratamiento
#declaracion de la clase principal para nuestro programa
class Pacientes:
    contador_id = 0 #contador declarado para auto asignar id a los pacientes
    
    def __init__ (self, nombre, edad): 
        Pacientes.contador_id +=1
        self.nombre = nombre
        self.edad = edad
        self.historial= []
        self.medicamento= []
        self.id = Pacientes.contador_id
        
    def __agregar_diagnostico (self, enfermedad):
        self.historial.append(enfermedad)

    def __agregar_medicamento (self, medicamento):
        self.medicamento.append(medicamento)
        
    def agregar_tratamiento(self, enfermedad, medicamento): #declaramos este metodo de tal forma que alimente las listas de la clase paciente asi como el historial de tratamiento
        historial_de_tratamiento.Lista_historial_tratamiento.nuevo_tratamiento(enfermedad,medicamento)
        Pacientes.__agregar_medicamento(medicamento)
        Pacientes.__agregar_diagnostico(enfermedad)
        
    def modificar_edad (self, nueva_edad):
        self.edad = nueva_edad 
        print (f"edad de {self.nombre} ha sido modificada a {self.edad} años")
    
    def mostrar_informacion(self):
        print(f"Paciente ID: {self.id}, Nombre: {self.nombre}, Edad: {self.edad}")