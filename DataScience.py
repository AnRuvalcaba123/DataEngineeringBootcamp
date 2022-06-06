#Use this dictionary to store your answers in the correct format in the cells below , do not modify the keys
answer_dict =  {"Q1" : None,
                "Q2" : None,
                "Q3" : None,
                "Q4" : None,
                "Q5" : None,
                "Q6" : None,
                "Q7" : None}

import pandas as pd
import numpy as np
url='https://drive.google.com/file/d/1PCJ7ltluquoXKi6MYTPMfwZQNI_-MIFP/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)                
df.head()
df.info()
######### Q1 
answer_dict.update({"Q1" : df.loc[df['Make'] == 'Volkswagen','CO2 Emission Grams/Mile'].mean()})
######### Q2 
df1 = df.sort_values("Model",ascending=False)
dfunique = df.drop_duplicates("Model")
dfunique = dfunique.head(n=5)
df1 = df1[['Make','Model']]
df1 = df1.merge(dfunique,on='Model',how='inner')
df1.drop(['Make_y'], axis = 'columns', inplace=True)
df1 = df1[['Make_x','Model']]
list = df1.values.tolist()
answer_dict.update({"Q2" : list})
######### Q3
List = df['Fuel Type'].unique()
List.sort()
answer_dict.update({"Q3" : List })
######### Q4
######### Q5
######### Q6
df2 = df.sort_values("CO2 Emission Grams/Mile",ascending=True)
Toyota = df2.loc[df2['Make'] == 'Toyota','CO2 Emission Grams/Mile'].head(n=5).values.tolist()
Volkswagen = df2.loc[df2['Make'] == 'Volkswagen','CO2 Emission Grams/Mile'].head(n=5).values.tolist()
Nissan = df2.loc[df2['Make'] == 'Nissan,','CO2 Emission Grams/Mile'].head(n=5).values.tolist()
Honda = df2.loc[df2['Make'] == 'Honda','CO2 Emission Grams/Mile'].head(n=5).values.tolist()
Ford = df2.loc[df2['Make'] == 'Ford','CO2 Emission Grams/Mile'].head(n=5).values.tolist()
Toyota.insert(0,'Toyota')
Volkswagen.insert(0,'Volkswagen')
Nissan.insert(0,'Nissan')
Honda.insert(0,'Honda')
Ford.insert(0,'Ford')
List2 = [Toyota,Volkswagen,Nissan,Honda,Ford]
print(List2)
answer_dict.update({"Q6" : List2 })
######### Q7


