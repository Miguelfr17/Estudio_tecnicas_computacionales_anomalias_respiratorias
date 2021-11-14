# Import Modulo
import os
import shutil
import ntpath

######################################################

# Path base de datos
path_BD = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI_final_database"

# Path Traquea
path_traquea = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionChestLocation\ICBHI-Traquea"

# Paths Zona Posterior
path_PosteriorLeft = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionChestLocation\ICBHI-PosteriorLeft"
path_PosteriorRight = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionChestLocation\ICBHI-PosteriorRight"

# Paths Zona Anterior
path_AnteriorLeft = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionChestLocation\ICBHI-AnteriorLeft"
path_AnteriorRight = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionChestLocation\ICBHI-AnteriorRight"

# Paths Zonas laterales
path_LateralLeft = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionChestLocation\ICBHI-LateralLeft"
path_LateralRight = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\ICBHI-ClasificacionChestLocation\ICBHI-LateralRight"
#####################################################

# Cambio de directorio
os.chdir(path_BD)

# Contador de archivos
ContadorArchivos= 0
ContadorTraquea = 0
ContadorPosteriorLeft = 0
ContadorPosteriorRight = 0
ContadorAnteriorLeft = 0
ContadorAnteriorRight = 0
ContadorLateralLeft=0
ContadorLateralRight=0

#Funcion para clasificar la BD en funcion del microfono
def move_file_clasificator(path_Archivo, zonaChest):
    #Utilizamos los contadores globales
    global ContadorTraquea
    global ContadorPosteriorLeft
    global ContadorPosteriorRight
    global ContadorAnteriorLeft
    global ContadorAnteriorRight
    global ContadorLateralLeft
    global ContadorLateralRight

    nombre_txt = str(path_Archivo)+".txt"
    nombre_wav = str(path_Archivo) + ".wav"
    origen_txt = path_BD + "\\" + nombre_txt
    origen_wav = path_BD + "\\" + nombre_wav

    if (zonaChest.upper() == "TC"):
        ContadorTraquea += 1
        destino_txt = path_traquea + "\\" + nombre_txt
        destino_wav = path_traquea + "\\" + nombre_wav
        # Copia de los archivos .txt y .wav
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)
        

    elif(zonaChest.upper() == "PL"):
        ContadorPosteriorLeft +=1
        destino_txt = path_PosteriorLeft + "\\" + nombre_txt
        destino_wav = path_PosteriorLeft + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)

    elif(zonaChest.upper() == "PR"):
        ContadorPosteriorRight +=1
        destino_txt = path_PosteriorRight + "\\" + nombre_txt
        destino_wav = path_PosteriorRight + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)

    elif(zonaChest.upper() == "AL"):
        ContadorAnteriorLeft +=1
        destino_txt = path_AnteriorLeft + "\\" + nombre_txt
        destino_wav = path_AnteriorLeft + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)
    
    elif(zonaChest.upper() == "AR"):
        ContadorAnteriorRight += 1
        destino_txt = path_AnteriorRight + "\\" + nombre_txt
        destino_wav = path_AnteriorRight + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)
    
    elif(zonaChest.upper() == "LL"):
        ContadorLateralLeft += 1
        destino_txt = path_LateralLeft + "\\" + nombre_txt
        destino_wav = path_LateralLeft + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)
    
    elif(zonaChest.upper() == "LR"):
        ContadorLateralRight += 1
        destino_txt = path_LateralRight + "\\" + nombre_txt
        destino_wav = path_LateralRight + "\\" + nombre_wav
        # Copia del archivo
        shutil.copyfile(origen_txt, destino_txt)
        shutil.copyfile(origen_wav, destino_wav)
    
    else:
        print("ERROR")

        
    

#Funcion para obetner el nombre del microfono de cada archivo
def zonaChest(path_audio):
    # Nombre del archivo con extension .txt
    namefile_extension = ntpath.basename(path_audio)

    # Nombre del archivo sin extension .txt
    namefile_events = os.path.splitext(namefile_extension)[0]
    
    #Obtenemos un vecto con los diferentes parametros que contiene el nombre de cada archivo
    VectorNombre = namefile_events.split('_')

    #Nos quedamos con el ultimo parametro del vector que se corresponde con el nombre del microfono
    zona = VectorNombre[2]
    return zona

   
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
        zona=zonaChest(nombre)
        move_file_clasificator(nombreArchivo,zona)
        ContadorArchivos += 1

# Print del contador
print("Numero de archivos: ", ContadorArchivos)
print("Traquea:", ContadorTraquea)
print("Posterior Left:", ContadorPosteriorLeft)
print("Posterior Right: ", ContadorPosteriorRight)
print("Anterior Left: ", ContadorAnteriorLeft)
print("Anterior Right: ", ContadorAnteriorRight)
print("Lateral Left: ", ContadorLateralLeft)
print("Lateral Right: ", ContadorLateralRight)
