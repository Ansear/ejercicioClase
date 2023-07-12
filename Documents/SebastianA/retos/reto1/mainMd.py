import os 
import pacientes
import veterinarios
import citas
if __name__ == "__main__":
    os.system("clear")
    isRun = True
    print("---ADMINISTRACION DEL CENTRO VETERINARIO---")
    print("1. Gestion de pacientes")
    print("2. Gestion de veterinarios")
    print("3. Gestion de citas")
    print("4. Salir")
    op = int(input("Ingrese una opcion: "))
    while isRun:
        if(op == 1):
            pacientes.infoPaciente()
            pacientes.addPaciente()
        elif(op == 2):
            pass
        elif(op == 3):
            pass
        elif(op == 4):
            isRun = False
        else:
            os.system("clear")
            print("Opcion incorrecta")
            isRun = False