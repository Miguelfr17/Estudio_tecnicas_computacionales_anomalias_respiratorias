import wave
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import os
from scipy import signal
from scipy.signal import filtfilt
from scipy.signal.signaltools import lfilter
import os
import ntpath


ContadorArchivos = 0
path_origen = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\Ciclos\Ciclos_DEFAULT\AudioNormalizado_8kHz\dataset\wheezes"

path_destino = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\Ciclos\Ciclos_BUTTER\Dataset_Butter\dataset\wheezes"


def Filtro_Chebyshev(pathArchivo, nombreAudio):
    # open the audio file and extract some information
    sr, y = wavfile.read(pathArchivo)

    # create the filter
    N = 5  # ORDEN DEL FILTRO##########
    nyquist_freq = 0.5*sr
    low = 100 / nyquist_freq
    high = 2500 / nyquist_freq
    b, a = signal.cheby1(N, [low, high], btype='bandpass')

    # apply filter
    x = lfilter(b, a, y)

    # ceate output file
    # Convert to 32 bit integers
    os.chdir(path_destino)
    wavfile.write(nombreAudio, sr, x.astype(np.int32))


# Funcion que obtiene el nombre de cada archivo
def namefile(path):
    # Nombre del archivo con extension .txt
    namefile_extension = ntpath.basename(path)
    # Nombre del archivo sin extension .txt
    namefile = os.path.splitext(namefile_extension)[0]
    #añadir extensdion wav
    namefile = namefile+'.wav'

    return str(namefile)
    # print(namefile)


#Cambio al directorio de origen de datos
os.chdir(path_origen)

# Iterador sobre la carpeta
for file in os.listdir():
    # Comprobacion de la extension del archivo
    if file.endswith(".wav"):
        nombre = f"{path_origen}\{file}"
        audioname = namefile(nombre)
        # Llamada a la funcion de resample
        Filtro_Chebyshev(nombre, audioname)
        ContadorArchivos += 1
