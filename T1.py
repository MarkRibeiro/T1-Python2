import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 30)
dfSeries = pd.read_excel('series.xlsx', sheet_name='SeriesInfo', index_col=0 ,header=0)
dfSeries = pd.DataFrame(dfSeries)
dfGeneros = pd.read_excel('series.xlsx', sheet_name='Generos', index_col=0 ,header=0)
dfGeneros = pd.DataFrame(dfGeneros)

'''2.1)Substitua as notas inexistentes no rotten tomatoes pela nota do IMDB * 10'''
print('\n')
print('2.1 --------------- Notas do Rotten Tomatoes atualizadas -----------------')
dfSeries['Rotten Tomatoes'].fillna(dfSeries['IMDB']*10, inplace=True)
print(dfSeries)

'''2.2)Substitua as classificaçoes indicativas vazias por 10 anos'''
print('\n')
print('2.2 --------------- Classificaçoes indicativas atualizadas -----------------')
dfSeries['Classificação indicativa'].fillna(7, inplace=True)
print(dfSeries)

'''1)Adiciona a tabela a nota media das series, ou seja nota do (rotten tomatoes + 10*(nota do IMDB))/2'''
print('\n')
print('1 --------------- Tabela com as notas medias -----------------')
colunas = (dfSeries['IMDB']*10 + dfSeries['Rotten Tomatoes'])/2
colunas.rename('NotaFinal', inplace = True)
dfSeries=pd.concat([dfSeries,colunas], axis=1).reindex(dfSeries.index)
print(dfSeries)

'''3)Substitua os valores da classificação indicativa para o seguinte:
    7: Criança
    16: Adolescente
    18: Adulto'''
print('\n')
print('3 --------------- Classificaçoes indicativas atualizadas com o tipo-----------------')
dfSeries['Classificação indicativa'].replace({7:'Criança',16:'Adolescente', 18:'Adulto'}, inplace=True)
print(dfSeries)

'''4)Crie uma nova coluna(Avaliação) que irá categorizar as notas da coluna NotaFinal da seguinte forma:
    entre 0 e 50: ruim
    acima 50 até 70: ok
    acima 70 até 80: bom
    acima 80 até 90: muito bom
    acima de 90: excelente'''
print('\n')
print('4 --------------- Tabela atualizada com a coluna Avaliação -----------------')
dfSeries["Avaliação"]=pd.cut(dfSeries["NotaFinal"],bins=[0,50,70,80,90,100],labels=['Ruim','Ok','Bom', 'Muito bom', 'Excelente'])
print(dfSeries)

'''6.1)Exibir a tabela de frequência de series por serviço de streaming'''
print('\n')
print('6.1 --------------- Tabela frequecia dos serviços de streaming-----------------')
print(dfSeries['Plataforma'].value_counts())

'''6.2)Exibir a tabela de frequência de series por numero de temporadas'''
print('\n')
print('6.2 ------ Tabela frequecia de series por numero de temporadas--------')
print(dfSeries['Numero de temp'].value_counts())

'''7.1) Grafico em barras da quantidade de series para cada tipo de publico (coluna Classificação indicativa)'''
print('\n')
print('7.1 --------------- Grafico dos tipos de público -----------------')
dfSeries['Classificação indicativa'].value_counts().plot.barh(figsize=(8,8),title = 'Titulos por publico')
plt.show()

'''7.2) Grafico em pizza da quantidade de series para cada tipo de avaliação (coluna
Avaliação)'''
print('\n')
print('7.2 --------------- Grafico dos Avaliações -----------------')
dfSeries['Avaliação'].value_counts().plot.pie(figsize=(8,8),title = 'Avaliações')
plt.show()

'''5.1) Quais series Netflix tem mais de 3 temporadas?'''
print('\n')
print('5.1 --------------- series Netflix com mais de 3 temporadas -----------------')
print(dfSeries[dfSeries['Numero de temp'] > 3].index.values)

'''5.2) Quantas series classificadas como “Muito bom” a amazon prime tem?'''
print('\n')
print('5.2 --------------- numero de series Muito boas da amazon prime -----------------')
print(dfSeries[dfSeries['Avaliação'] == 'Muito bom']['Avaliação'].size)

'''5.3) Quantas series para Adolescentes a HBOGo tem?'''
print('\n')
print('5.3 --------------- Series Adolescentes da Netflix -----------------')
print(dfSeries[(dfSeries['Classificação indicativa'] == 'Adolescente') & (dfSeries['Plataforma'] == 'Netflix')].index.values)

'''8.1) Maior nota do IMDB'''
print('\n')
print('8.1 --------------- Serie com maior nota do IMDB -----------------')
print(dfSeries['IMDB'].idxmax())

'''8.2) Série com maior número de temporadas da HBOGo'''
print('\n')
print('8.2 ---------------  Série com maior número de temporadas da HBOGo -----------------')
print(dfSeries.groupby(['Plataforma']).idxmax()['Numero de temp']['HBOGo'])

'''8.3) Menor nota para cada plataforma'''
print('\n')
print('8.3 --------------- Menor nota para cada plataforma -----------------')
print(dfSeries.groupby(['Plataforma']).min()['NotaFinal'])

'''9.1) Faça um cruzamento Classificação indicativa X Plataforma'''
print('\n')
print('9.1 --------------- Crosstab Classificação indicativa X Plataforma -----------------')
print(pd.crosstab(dfSeries['Classificação indicativa'], dfSeries['Plataforma']))

'''9.2) Faça um cruzamento número de temporadas X Plataforma'''
print('\n')
print('9.2 --------------- Crosstab Numero de temp X Plataforma -----------------')
print(pd.crosstab(dfSeries['Numero de temp'], dfSeries['Plataforma']))

'''9.3) '''
print('\n')
print('9.3 --------------- Crosstab ... -----------------')

'''9.4) '''
print('\n')
print('9.4 --------------- Crosstab ... -----------------')
