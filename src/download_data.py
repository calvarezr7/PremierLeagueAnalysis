import kaggle
import os

#Setting the download path
DATA_PATH = r"C:\Users\camilo.alvarez\Documents\TrainingDE\PremierLeague\data\raw"
os.makedirs(DATA_PATH, exist_ok= True)

# Descargar el dataset en el directorio actual
dataset = 'panaaaaa/english-premier-league-and-championship-full-dataset'
kaggle.api.dataset_download_files(dataset, path= DATA_PATH, unzip=True)

print ("✅ Datos descargados en:", DATA_PATH)
