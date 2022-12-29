import pandas as pd

#df_csv = pd.read_csv('pokemon_data.csv')

df = pd.read_csv("C:/Users/user667/PycharmProjects/pythonProject1/capstone/pokemon_data.csv")
print(df)

# Attack, Defense, Speed
df['total']= df['Attack']+df['Defense']+df['Speed']
print(df)

# Interchange(Type 1,Type 2)

df['Type 1'],df['Type 2'] =df['Type 2'],df['Type 1']
#print(df[['Type 1','Type 2']])
print(df.to_string())






