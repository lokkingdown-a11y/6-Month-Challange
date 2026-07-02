import pandas as pd
df = pd.read_csv('ar.csv')
import matplotlib.pyplot as plt
df['Customer Id'].hist()
plt.show()
df.plot(kind='scatter', x='বয়স', y='জন্ম_বছর')
plt.show()

import pandas as pd
data = {
    'Name' : ['Antu','chondon','dipto','joy'],
    'age' : [23,36,25,14],
    'Status' : ['Student','Student','Student','Student']
}
df = pd.DataFrame(data)
print(df)

import pandas as pd 
df = pd.read_excel('ar.xlsx')
print(df['Project Name'])
try:
    df = df['Project Name']
    print(df)
except KeyError:
    print('Please Check Code Again')
finally:
    print('Check Again')
