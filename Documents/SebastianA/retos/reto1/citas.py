import os 
import core

def addPaciente():
    os.system("clear")
    print("1. Crear cita")
    print("2. Cancelar cita")
    print("3. Consultar citas por fecha")
    print("4. Consultar citas por veterinario")
    print("5. Volver al menu principal")
    op = int(input("Opcion: "))