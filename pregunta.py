"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import numpy as np
import re


def ingest_data():

    #
    # Inserte su código aquí
    #
    
    with open("clusters_report.txt",'r') as file:
        Datos= file.readlines()
    listado = list()
    titulos = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    Datos = Datos[4:]
    
    for line in Datos:
        Palabras = line.split()
        if len(Palabras) != 0:
            if Palabras[0].isdigit():
                listado.append(Palabras[0:3])
                listado[-1].append(' '.join(Palabras[4:]))
                listado[-1][-1] += ' '
            elif Palabras[0].isdigit():
                listado[-1][-1] += ' '.join(Palabras)
                listado[-1][-1] += ' '
        
    for line in listado:
        line[-1] = line[-1].rstrip('. ')
        line[0] = int(line[0])
        line[1] = int(line[1])
        line[2] = line[2].replace(',','.')
        line[2] = float(line[2])

    
    df = pd.DataFrame(listado,columns=titulos)

    return df
