#Imports
import os
import shutil
import ntpath

######################################################

#Path base de datos
path_BD = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI_final_database"

#Paths Canales
path_SingleChannel = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionCanales\ICBHI-SingleChannel"
path_MultiChannel = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionCanales\ICBHI-MultiChannel"
#####################################################

# Cambio de directorio
os.chdir(path_BD)

# Contador de archivos
ContadorArchivos= 0
ContadorSingleChannel=0
ContadorMultiChannel=0

#Funcion para clasificar la BD en funcion del microfono
def move_file_clasificator(path_Archivo, numCanal):
    #Utilizamos los contadores globales
    global ContadorSingleChannel
    global ContadorMultiChannel

    nombre_txt = str(path_Archivo)+".txt"
    nombre_wav = str(path_Archivo) + ".wav"
    origen_txt = path_BD + "\\" + nombre_txt
    origen_wav = path_BD + "\\" + nombre_wav

    if (numCanal.upper() == "SC"):
        ContadorSingleChannel += 1
        destino_txt = path_SingleChannel + "\\" + nombre_txt
        destino_wav = path_SingleChannel + "\\" + nombre_wav
        # Copia de los archivos .txt y .wav
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)
        

    elif(numCanal.upper() == "MC"):
        ContadorMultiChannel +=1
        destino_txt = path_MultiChannel + "\\" + nombre_txt
        destino_wav = path_MultiChannel + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)

    else:
        print ("ERROR")

        
    

#Funcion para obetner el nombre del microfono de cada archivo
def NumeroCanales(path_audio):
    # Nombre del archivo con extension .txt
    namefile_extension = ntpath.basename(path_audio)

    # Nombre del archivo sin extension .txt
    namefile_events = os.path.splitext(namefile_extension)[0]
    
    #Obtenemos un vecto con los diferentes parametros que contiene el nombre de cada archivo
    VectorNombre = namefile_events.split('_')

    #Nos quedamos con el ultimo parametro del vector que se corresponde con el nombre del microfono
    canal = VectorNombre[3]
    return canal

   
 # Funcion que obtiene el nombre de cada archivo
def namefile(path):
    # Nombre del archivo con extension .txt
    namefile_extension = ntpath.basename(path)

    # Nombre del archivo sin extension .txt
    namefile_events = os.path.splitext(namefile_extension)[0]

    return namefile_events
    # print(namefile)

# Iterador sobre la carpeta
for file in os.listdir():
    # Comprobacion de la extension del archivo
    if file.endswith(".wav"):
        nombre = f"{path_BD}\{file}"
        # Llamada a la funcion de lectura
        nombreArchivo=namefile(nombre)
        canal=NumeroCanales(nombre)
        move_file_clasificator(nombreArchivo,canal)
        ContadorArchivos += 1

# Print del contador
print("Numero de archivos: ", ContadorArchivos)
print("Single Channel: ", ContadorSingleChannel)
print("Multi Channel: ", ContadorMultiChannel)
 
