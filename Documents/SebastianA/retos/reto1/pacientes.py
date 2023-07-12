import os 
import core
cont = 0

diccPa = {"data":[]}
def infoPaciente():
    if(core.checkfile("pacientes.json")):
      global diccPa
      diccPa = core.loadInfo("pacientes.json") 
    else:
          core.savefile("pacientes.json",diccPa)

def addPaciente():
    isPaRun = True
    species = {
        "perro":["Pastor Aleman","Pitbull Terrier","Doberman","Golden Retriever","Border Collie"],
        "gato":["Persa","Siames","Ragdoll","Esfinge","Maine Coon"],
        "reptil":["Iguana","Camaleon","Serpiente","cocodrilo","tortuga"],
        "ave":["Aguila","Condor","Paloma","Tucan","Cisne"],
    }
    os.system("clear")
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Mostrar informacion de un paciente")
    print("4. Volver al menu principal")
    op = int(input("Opcion: "))
    if(op == 1 ):
        os.system("clear")
        namePa = input("Ingrese el nombre del paciente: ")
        os.system("clear")
        print("Especie")
        specie = input("Seleccione la especie del paciente: (perro,gato,reptil,ave) ")
        if(species[specie.lower()]):
            for i,item in enumerate(species[specie.lower()]):
                    print(i+1,".",item)
        else:
            print("Especie no encontrada, Ingrese una especie validad")
            isPaRun = False
        race = int(input("Seleccione la raza del paciente: "))
        species[specie.lower()][race-1]
        age = int(input("Ingrese la edad del paciente: "))
        namePro = input(f"Ingrese el nombre del propietario del Paciente {namePa}: ")
        data = {
            "id":cont+1,
            "nombre":namePa,
            "especie":specie,
            "raza":namePa,
            "edad":age,
            "propietario":namePro
        }
        diccPa["data"].append(data)
        core.savefile("pacientes.json",data)
        num = diccPa["data"][-1]["id"]
        if(num == 0):
            num = 1
        print(num)
        input(":")
    elif(op == 2 ):
        pass
    elif(op == 3 ):
        pass
    elif(op == 4 ):
        isPaRun = False
    else: 
        print("Opcion Invalida")
    if(isPaRun):
        addPaciente()