
#Imports
import soundfile as sf
from matplotlib import pyplot as plt
import os
import ntpath

ContadorArchivos = 0

#Path Origen Muestras
path_origen = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\Ciclos\Ciclos_DEFAULT\Resample_Muestras_8kHz\dataset\empty"

#Path de destino de audios normalizados
path_audioNormalizado = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\Ciclos\Ciclos_DEFAULT\AudioNormalizado_8kHz_224\dataset\empty"
#Path de destino de imagenes de onda sonora
path_destinoImagenes = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\Ciclos\Ciclos_DEFAULT\OndasSonoras_8kHz_224\dataset\empty"

#Funcion para guardar las imagenes en disco
def print_plot_play(ImageName, x, Fs, text=''):

    print('%s Fs = %d, x.shape = %s, x.dtype = %s' %
          (text, Fs, x.shape, x.dtype))
    my_dpi = 70  # pixeles por pulgada, especifico de cada pantalla
    plt.figure(figsize=(222/my_dpi, 208.5/my_dpi))
    plt.plot(x, color='blue')
    plt.xlim([0, x.shape[0]])
    plt.xlabel('Time (samples)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    #plt.show()
    plt.axis('off')
    os.chdir(path_destinoImagenes)
    plt.savefig(ImageName, bbox_inches='tight',
                transparent=True, pad_inches=0.0)
    plt.pause(0.01)
    plt.close()
    plt.close(1)
    plt.close('all')
    #ipd.display(ipd.Audio(data=x, rate=Fs))

#Funcion para obetener el dibujo de la onda
def BandaSonora(pathAudio, nombreArchivoPNG, nombreArchivoWAV):

    # Leer archivo wav con dtype= 'int32'
    fn_wav = pathAudio
    x, Fs = sf.read(fn_wav, dtype='int32')
    #print_plot_play(x=x, Fs=Fs, text='Archivo WAV (dtype=int32): ')

    #Escribir archivo wav 'int32' normalizado
    pathFinal= os.path.join(path_audioNormalizado, nombreArchivoWAV)
    fn_out = pathFinal
    sf.write(fn_out, x, Fs, subtype='PCM_32')
    x, Fs = sf.read(fn_out)
    print_plot_play(nombreArchivoPNG,
        x=x, Fs=Fs, text='Señal (int32)')
        


# Funciones que obtiene el nombre de cada archivo
def namefilePNG(path):
    # Nombre del archivo con extension .txt
    namefile_extension = ntpath.basename(path)
    # Nombre del archivo sin extension .txt
    namefile = os.path.splitext(namefile_extension)[0]
    #añadir extensdion png
    namefile_png = namefile+'.jpg'

    return str(namefile_png)
    # print(namefile)

def namefileWAV(path):
    # Nombre del archivo con extension .txt
    namefile_extension = ntpath.basename(path)
    # Nombre del archivo sin extension .txt
    namefile = os.path.splitext(namefile_extension)[0]
    #añadir extensdion png
    namefile_wav =namefile + '.wav'

    return str(namefile_wav)


#Cambio al directorio de origen de datos
os.chdir(path_origen)

# Iterador sobre la carpeta
for file in os.listdir():
    # Comprobacion de la extension del archivo
    if file.endswith(".wav"):
        nombre = f"{path_origen}\{file}"
        audionamePNG = namefilePNG(nombre)
        audionameWAV= namefileWAV(nombre)
        # Llamada a la funcion de resample
        BandaSonora(nombre, audionamePNG, audionameWAV)
        ContadorArchivos += 1
    print(ContadorArchivos)
