import pandas as pd

df = pd.DataFrame({'1':[['miguel', 'eustaquio', 'silva'], 'eu'], '2':['sora', 'nao sou eu'], '3':['roxas', 'tbm n sou eu']}, index=['nome', 'informacao'])

df.to_csv('utilities/teste.csv')