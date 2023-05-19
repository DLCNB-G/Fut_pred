
import numpy as np
import pandas as pd
import math

data = pd.read_excel('Info_clean_2.xlsx')
data.head(5)

#revision de nulos
data.info()

#borrando columna llena de nulos 
del data['Unnamed: 10']