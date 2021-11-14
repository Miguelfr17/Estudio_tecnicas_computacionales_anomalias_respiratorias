import splitfolders

path_origen = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\ICHBI\DATASETS\CICLOS_SINFILTRO\Balanceado_2_clases\dataset"
path_destino = r"C:\Users\Miguel\OneDrive - Universidad de Oviedo\TFG\Bases de datos\datasetJetson\datasetB2"

#Divide un dataset en Entrenamiento y Validación
splitfolders.ratio(path_origen, output=path_destino, seed=123,
                   ratio=(.80, .20,), group_prefix=None)  # default values
