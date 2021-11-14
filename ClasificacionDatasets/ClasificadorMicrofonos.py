# Import Modulo
import os
import shutil
import ntpath

######################################################

# Path base de datos
path_BD = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI_final_database"

# Path AKGC417L
path_AKGC417L = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionMicrofono\ICBHI-AKGC417L"

# Path LittC2SE
path_LittC2SE = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionMicrofono\ICBHI-LittC2SE"

# Path Litt3200
path_Litt3200 = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionMicrofono\ICBHI-Litt3200"

# Path Meditron
path_Meditron = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionMicrofono\ICBHI-Meditron"

#####################################################

# Cambio de directorio
os.chdir(path_BD)

# Contador de archivos
ContadorArchivos = 0
ContadorAKGC417L = 0
ContadorLittC2SE = 0
ContadorLitt3200 = 0
ContadorMeditron = 0

#Funcion para clasificar la BD en funcion del microfono
def move_file_clasificator(path_Archivo, nombreMicrofono):
    #Utilizamos los contadores globales
    global ContadorAKGC417L
    global ContadorLitt3200
    global ContadorLittC2SE
    global ContadorMeditron

    nombre_txt = str(path_Archivo)+".txt"
    nombre_wav = str(path_Archivo) + ".wav"
    origen_txt = path_BD + "\\" + nombre_txt
    origen_wav = path_BD + "\\" + nombre_wav

    if (nombreMicrofono.upper() == "AKGC417L"):
        ContadorAKGC417L += 1
        destino_txt = path_AKGC417L + "\\" + nombre_txt
        destino_wav = path_AKGC417L + "\\" + nombre_wav
        # Copia de los archivos .txt y .wav
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)
        

    elif(nombreMicrofono.upper() == "LITTC2SE"):
        ContadorLittC2SE +=1
        destino_txt = path_LittC2SE + "\\" + nombre_txt
        destino_wav = path_LittC2SE + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)

    elif(nombreMicrofono.upper() == "LITT3200"):
        ContadorLitt3200 +=1
        destino_txt = path_Litt3200 + "\\" + nombre_txt
        destino_wav = path_Litt3200 + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)

    elif(nombreMicrofono.upper() == "MEDITRON"):
        ContadorMeditron +=1
        destino_txt = path_Meditron + "\\" + nombre_txt
        destino_wav = path_Meditron + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)
    
    else:
        print("ERROR")

#Funcion para obetner el nombre del microfono de cada archivo
def nombreMicrofono(path_audio):
    # Nombre del archivo con extension .txt
    namefile_extension = ntpath.basename(path_audio)

    # Nombre del archivo sin extension .txt
    namefile_events = os.path.splitext(namefile_extension)[0]
    
    #Obtenemos un vecto con los diferentes parametros que contiene el nombre de cada archivo
    VectorNombre = namefile_events.split('_')

    #Nos quedamos con el ultimo parametro del vector que se corresponde con el nombre del microfono
    nombreMicrofono = VectorNombre[4]
    return nombreMicrofono

   
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
        microfono=nombreMicrofono(nombre)
        move_file_clasificator(nombreArchivo,microfono)
        ContadorArchivos += 1

# Print del contador
print("Numero de archivos: ", ContadorArchivos)
print("AKGC417L:", ContadorAKGC417L)
print("LittC2SE:", ContadorLittC2SE)
print("Litt3200: ", ContadorLitt3200)
print("Meditron: ", ContadorMeditron)
