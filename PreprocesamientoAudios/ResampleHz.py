# Imports
import librosa
import soundfile as sf
import os
import ntpath


# Contador de archivos
ContadorArchivos = 0
frecuencia_final= 8192 #Reconmedable multiplos de 2

#Path de origen
path_origen = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\Ciclos\ICBHI-CICLOS-DATABASE\dataset\empty"

#Path de destino
path_destino = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\Ciclos\Ciclos_DEFAULT\Resample_Muestras_8kHz\dataset\empty"


#Funcion para resamplear audio. Params: audio_path= path del audio a resamplear, audioname= nombre del audio para el guardado.
def resample (audio_path, audioname):
    global path_destino 
    x, sr = librosa.load(audio_path, sr=librosa.get_samplerate(audio_path))
    y = librosa.resample(x, sr, frecuencia_final) #Frecuencia a la que queremos downsamplear
    os.chdir(path_destino)
    sf.write(audioname, y, frecuencia_final, format='WAV', subtype='PCM_32') 
    
# Funcion que obtiene el nombre de cada archivo
def namefile(path):
    # Nombre del archivo con extension .txt
    namefile_extension = ntpath.basename(path)

    # Nombre del archivo sin extension .txt
    #namefile_events = os.path.splitext(namefile_extension)[0]

    return str(namefile_extension)
    # print(namefile)



#Cambio al directorio de origen de datos
os.chdir(path_origen)

# Iterador sobre la carpeta
for file in os.listdir():
    # Comprobacion de la extension del archivo
    if file.endswith(".wav"):
        nombre = f"{path_origen}\{file}"
        audioname= namefile(nombre)
        # Llamada a la funcion de resample
        resample(nombre, audioname)
        ContadorArchivos += 1
