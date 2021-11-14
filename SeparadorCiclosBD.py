from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import shutil
import ntpath
import numpy as np



######################################################

# Path base de datos
path_origen = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI_final_database"

# Path Crackles
path_crackles = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-CiclosDatabase\dataset\crackles"

# Path Wheezes
path_wheezes = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-CiclosDatabase\dataset\wheezes"

# Path Crackles y Wheezes
path_crackles_wheezes = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-CiclosDatabase\dataset\both"

# Path Empty
path_empty = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-CiclosDatabase\dataset\empty"

ContadorArchivos=0

def obtenerCiclo(path_audioOrigen,nombreAudiofinal, t1, t2, C, W):
    if ((C==1)and(W==0)):
        os.chdir(path_crackles)
    elif((C==0)and(W==1)):
        os.chdir(path_wheezes)
    elif((C==1)and(W==1)):
        os.chdir(path_crackles_wheezes)
    elif((C==0)and(W==0)):
        os.chdir(path_empty)
    else:
        print("ERROR: el ciclo no se corresponde con ninguna de las opciones de clasificacion")
    ffmpeg_extract_subclip(path_audioOrigen, t1, t2, targetname=nombreAudiofinal)


def namefileWAV(path):
    # Nombre del archivo con extension .txt
    namefile_extension = ntpath.basename(path)
    # Nombre del archivo sin extension .txt
    namefile = os.path.splitext(namefile_extension)[0]
    #añadir extensdion png
    namefile_wav = namefile + '.wav'

    return str(namefile_wav)

def pathOrigen(path, nombreAudio):
    pathFinal = os.path.join(path, nombreAudio)
    return pathFinal

def leerCiclos(path_txt):
    #Funcion que obtiene un vector con los ciclos respiratorios de cada archivo
    file=path_txt
    tiempo_inicio=0.0
    tiempo_fin=0.0
    crackles=0
    wheezes=0

    data = []
    with open(file) as fobj:
        for line in fobj:
            row = line.split()
            data.append(row[:4])
    Ciclo=1   
    for audio in data:
        tiempo_inicio= float(audio[0])
        tiempo_fin=float(audio[1])
        crackles= int(audio[2])
        wheezes= int(audio[3])
        nombreAudio=namefileWAV(file)
        pathAudioOrigen=pathOrigen(path_origen,nombreAudio)
        nombreAudioFinal = "Ciclo"+str(Ciclo)+"_"+nombreAudio
        obtenerCiclo(pathAudioOrigen,nombreAudioFinal,tiempo_inicio,tiempo_fin,crackles,wheezes)
        Ciclo +=1

os.chdir(path_origen)
# Iterador sobre la carpeta
for file in os.listdir():
    # Comprobacion de la extension del archivo
    if file.endswith(".txt"):
        nombre = f"{path_origen}\{file}"
        # Llamada a la funcion
        leerCiclos(nombre)
        ContadorArchivos += 1
    print(ContadorArchivos)
