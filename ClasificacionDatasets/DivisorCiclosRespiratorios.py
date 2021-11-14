# Import Modulo
import os
import shutil
import ntpath

######################################################

# Path de eventos a leer
path = r"C:\Users\Miguel\Desktop\ICBHI-ClasificacionEventos\Events\events"

# Path base de datos
path_BD = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI_final_database"

# Path Crackles
path_crackles = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionEventos\ICBHI-Crackles"

# Path Wheezes
path_wheezes = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionEventos\ICBHI-Wheezes"

# Path Crackles y Wheezes
path_crackles_wheezes = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionEventos\ICBHI-Crackles y Wheezes"

# Path Empty
path_empty = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionEventos\ICBHI-Empty"

#####################################################


# Cambio de directorio
os.chdir(path)

# Contador de archivos
ContadorArchivos = 0
ContadorCrackles = 0
ContadorWheezes = 0
ContadorBoth = 0
ContadorEmpty = 0


# Funcion para leer cada txt
def read_text_file(nombre):
    global ContadorCrackles
    global ContadorWheezes
    global ContadorBoth
    global ContadorEmpty
    with open(nombre, 'r') as evento:
        contenido = evento.read()
        # Imprime el archivo por consola
        # print(evento.read())
        if ("crackle" in contenido):
            if("wheeze" in contenido):
                # Si tiene Crakles y Wheezes
                ContadorBoth += 1
                nombreArchivo = namefile(nombre)
                move_file_clasificator(nombreArchivo, "crackles_wheezes")
            else:
                # Si tiene solo Crackles
                ContadorCrackles += 1
                nombreArchivo = namefile(nombre)
                move_file_clasificator(nombreArchivo, "crackles")
        elif("wheeze" in contenido):
            # Si tiene solo Wheezes
            ContadorWheezes += 1
            nombreArchivo = namefile(nombre)
            move_file_clasificator(nombreArchivo, "wheezes")
        else:
            # Si esta vacio
            ContadorEmpty += 1
            nombreArchivo = namefile(nombre)
            move_file_clasificator(nombreArchivo, "empty")

# Funcion para clasificar el audio y texto de cada archivo


def move_file_clasificator(nombre, path_destino):
    nombre_txt = str(nombre)+".txt"
    nombre_wav = str(nombre) + ".wav"
    origen_txt = path_BD + "\\" + nombre_txt
    origen_wav = path_BD + "\\" + nombre_wav

    if (path_destino == "crackles"):
        destino_txt = path_crackles + "\\" + nombre_txt
        destino_wav = path_crackles + "\\" + nombre_wav
        # Copia de los archivos .txt y .wav
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)

    elif(path_destino == "wheezes"):
        destino_txt = path_wheezes + "\\" + nombre_txt
        destino_wav = path_wheezes + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)

    elif(path_destino == "crackles_wheezes"):
        destino_txt = path_crackles_wheezes + "\\" + nombre_txt
        destino_wav = path_crackles_wheezes + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)

    elif(path_destino == "empty"):
        destino_txt = path_empty + "\\" + nombre_txt
        destino_wav = path_empty + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)

    else:
        print("ERROR")


#Funcion que obtiene un vector con los ciclos respiratorios de cada archivo
f = open(file, "r")
lines = f.readlines()
result = []
for x in lines:
    result.append(x.split(' ')[1])
f.close()

# Funcion que obtiene el nombre de cada archivo


def namefile(path):
    # Nombre del archivo con extension .txt
    namefile_extension = ntpath.basename(path)

    # Nombre del archivo sin extension .txt
    namefile_events = os.path.splitext(namefile_extension)[0]

    # Nombre del archivo eliminando la ultima palabra (_events)
    namefile = namefile_events.replace("_events", "")
    return namefile
    # print(namefile)


# Iterador sobre la carpeta
for file in os.listdir():
    # Comprobacion de la extension del archivo
    if file.endswith(".txt"):
        nombre = f"{path}\{file}"
        # Llamada a la funcion de lectura
        read_text_file(nombre)
    ContadorArchivos += 1

# Print del contador
print("Numero de archivos: ", ContadorArchivos)
print("Crackles:", ContadorCrackles)
print("Wheezes:", ContadorWheezes)
print("Both: ", ContadorBoth)
print("Empty: ", ContadorEmpty)
