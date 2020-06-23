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

'''2.2)Substitua as classificaçoes indicativas vazias por 10 anos'''
print('\n')
print('2.2 --------------- Classificaçoes indicativas atualizadas -----------------')

'''1)Adiciona a tabela a nota media das series*(NotaFinal), ou seja nota do (rotten tomatoes + 10*(nota do IMDB))/2'''
print('\n')
print('1 --------------- Tabela com as notas medias -----------------')

'''3)Substitua os valores da classificação indicativa para o seguinte:
    7: Criança
    16: Adolescente
    18: Adulto'''
print('\n')
print('3 --------------- Classificaçoes indicativas atualizadas com o tipo-----------------')

'''4)Crie uma nova coluna(Avaliação) que irá categorizar as notas da coluna NotaFinal da seguinte forma:
    entre 0 e 50: ruim
    acima 50 até 70: ok
    acima 70 até 80: bom
    acima 80 até 90: muito bom
    acima de 90: excelente'''
print('\n')
print('4 --------------- Tabela atualizada com a coluna Avaliação -----------------')

'''6.1)Exibir a tabela de frequência de series por serviço de streaming'''
print('\n')
print('6.1 --------------- Tabela frequecia dos serviços de streaming-----------------')

'''6.2)Exibir a tabela de frequência de series por numero de temporadas'''
print('\n')
print('6.2 ------ Tabela frequecia de series por numero de temporadas--------')

'''7.1) Grafico em barras da quantidade de series para cada tipo de publico (coluna Classificação indicativa)'''
print('\n')
print('7.1 --------------- Grafico dos tipos de público -----------------')

'''7.2) Grafico em pizza da quantidade de series para cada tipo de avaliação (coluna Avaliação) '''
print('\n')
print('7.2 --------------- Grafico dos Avaliações -----------------')

'''5.1) Quais series Netflix tem mais de 3 temporadas?'''
print('\n')
print('5.1 --------------- series Netflix com mais de 3 temporadas -----------------')

'''5.2) Quantas series classificadas como “Muito bom” a amazon prime tem?'''
print('\n')
print('5.2 --------------- numero de series Muito boas da amazon prime -----------------')

'''5.3) Quantas series para Adolescentes a HBOGo tem?'''
print('\n')
print('5.3 --------------- Series Adolescentes da Netflix -----------------')

'''8.1) Maior nota do IMDB'''
print('\n')
print('8.1 --------------- Serie com maior nota do IMDB -----------------')

'''8.2) Série com maior número de temporadas da HBOGo'''
print('\n')
print('8.2 ---------------  Série com maior número de temporadas da HBOGo -----------------')

'''8.3) Menor nota para cada plataforma'''
print('\n')
print('8.3 --------------- Menor nota para cada plataforma -----------------')

'''9.1) Faça um cruzamento Classificação indicativa X Plataforma'''
print('\n')
print('9.1 --------------- Crosstab Classificação indicativa X Plataforma -----------------')

'''9.2) Faça um cruzamento número de temporadas X Plataforma'''
print('\n')
print('9.2 --------------- Crosstab Numero de temp X Plataforma -----------------')

'''9.3) '''
print('\n')
print('9.3 --------------- Crosstab ... -----------------')

'''9.4) '''
print('\n')
print('9.4 --------------- Crosstab ... -----------------')