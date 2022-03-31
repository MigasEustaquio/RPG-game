import pandas as pd

data = pd.read_csv('utilities/teste.csv')

teste = data['1'].values.tolist()

teste[0] = teste[0].replace("['", '')
teste[0] = teste[0].replace("']", '')

teste[0] = teste[0].split("', '")
print(teste[0])
