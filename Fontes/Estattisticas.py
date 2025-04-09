import pandas as pd #pip install pandas "PARA LER AS PLANILHAS DO EXCEL"
import matplotlib #pip instal matplotlib "PARA FAZER AS VISUALIZAÇÕES DE DADOS"

#pip install openpyxl

arquivo_e = 'campeonatos_futebol_H.xlsx'

df_arquivos = pd.read_excel(arquivo_e)

print(df_arquivos)