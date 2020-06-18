import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 30)
dfSeries = pd.read_excel('series.xlsx',header=0)
dfSeries = pd.DataFrame(dfSeries)
#print(dfSeries)

#2)Substitua as notas inexistentes no rotten tomatoes pela nota do IMDB * 10
dfSeries['Rotten Tomatoes (%)'].fillna(dfSeries['nota (imdb)']*10, inplace=True)
#print(dfSeries)

#2)Substitua as classificaçoes indicativas vazias por 10 anos
dfSeries['Classificação indicativa'].fillna(7, inplace=True)
#print(dfSeries)

#1)Calcule a media das notas das series, ou seja nota do (rotten tomatoes + nota do IMDB)/2
imdb = dfSeries['nota (imdb)']
rotten = dfSeries['Rotten Tomatoes (%)']
colunas = [imdb*10, rotten]
print(pd.concat(colunas, axis=1, sort=False).reindex(imdb.index))

'''
3)Substitua os valores da classificação indicativa para o seguinte:
    7: Criançã
    16: Adolescente
    18: Adulto
'''
dfSeries['Classificação indicativa'].replace({7:'Criançã',16:'Adolescente', 18:'Adulto'}, inplace=True)
print(dfSeries)

