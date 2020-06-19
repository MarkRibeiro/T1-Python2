import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 30)
dfSeries = pd.read_excel('series.xlsx',index_col=0 ,header=0)
dfSeries = pd.DataFrame(dfSeries)
#print(dfSeries)

'''2i)Substitua as notas inexistentes no rotten tomatoes pela nota do IMDB * 10'''
print('\n')
print('--------------- Notas do Rotten Tomatoes atualizadas -----------------')
dfSeries['Rotten Tomatoes'].fillna(dfSeries['IMDB']*10, inplace=True)
print(dfSeries)

'''2ii)Substitua as classificaçoes indicativas vazias por 10 anos'''
print('\n')
print('--------------- Classificaçoes indicativas atualizadas -----------------')
dfSeries['Classificação indicativa'].fillna(7, inplace=True)
print(dfSeries)

'''1)Adiciona a tabela a nota media das series, ou seja nota do (rotten tomatoes + 10*(nota do IMDB))/2'''
print('\n')
print('--------------- Tabela com as notas medias -----------------')
colunas = (dfSeries['IMDB']*10 + dfSeries['Rotten Tomatoes'])/2
colunas.rename('NotaFinal', inplace = True)
dfSeries=pd.concat([dfSeries,colunas], axis=1).reindex(dfSeries.index)
print(dfSeries)
#print(pd.concat(colunas, axis=1, sort=False).reindex(imdb.index))

'''
3)Substitua os valores da classificação indicativa para o seguinte:
    7: Criança
    16: Adolescente
    18: Adulto
'''
print('\n')
print('--------------- Classificaçoes indicativas atualizadas com o tipo-----------------')
dfSeries['Classificação indicativa'].replace({7:'Criança',16:'Adolescente', 18:'Adulto'}, inplace=True)
print(dfSeries)
'''
4)Crie uma nova coluna(Avaliação) que irá categorizar as notas da coluna NotaFinal da
seguinte forma:
    entre 0 e 50: ruim
    acima 50 até 70: ok
    acima 70 até 80: bom
    acima 80 até 90: muito bom
    acima de 90: excelente

'''
print('\n')
print('--------------- Tabela atualizada com as Avaliações-----------------')
dfSeries["Avaliação"]=pd.cut(dfSeries["NotaFinal"],bins=[0,50,70,80,90,100],labels=['Ruim','Ok','Bom', 'Muito bom', 'Excelente'])
print(dfSeries)

'''
6i)Exibir a tabela de frequência de series por serviço de streaming
'''
print('\n')
print('--------------- Tabela frequecia dos serviços de streaming-----------------')
print(dfSeries['Plataforma'].value_counts())


'''
6ii)Exibir a tabela de frequência de series com mais de 3 temporadas por serviço de streaming

'''
print('\n')
print('------ Tabela frequecia de series com mais de 3 temporadas por serviço de streaming--------')
d=dfSeries['Numero de temp']>2
#print(d)

'''
7) Grafico em barras da quantidade de series para cada tipo de publico (coluna Classificação indicativa)

'''
print('\n')
print('--------------- Grafico dos tipos de público -----------------')
dfSeries['Classificação indicativa'].value_counts().plot.barh(figsize=(8,8),title = 'Titulos por publico')
plt.show()

'''
7) Grafico em pizza da quantidade de series para cada tipo de avaliação (coluna
Avaliação)
    
'''
print('\n')
print('--------------- Grafico dos Avaliações -----------------')
dfSeries['Avaliação'].value_counts().plot.pie(figsize=(8,8),title = 'Avaliações')
plt.show()