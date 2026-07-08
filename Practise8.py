import pandas as pd
data = {
    'name' : ['antu','chondon','dipto','joy'],
    'age' : [22,55,67,90],
    'status' : ['student','student','student','student']
}

df = pd.DataFrame(data)
df['birthyear'] = 2026 - df['age']
mlt_clm = df[['age','birthyear']]
print(mlt_clm)
young = df[df['age']<90]
print(age_clm)
check = df.isnull().sum()
drop = df.dropna
print(drop)
print(check)
fill = df.fillna(0)
print(fill)
fill = df['age'].fillna(df['age'].mean())
print(fill)

import pandas as fh
data = {
    'name' : ['antu','antu','chondon','joy','Opu','Dipto'],
    'age' : [23,23,24,35,34,56],
    'status' : ['Student','Student','Student','Student','Student','Student']
}
fd = fh.DataFrame(data)
real_value = fd.drop_duplicates(subset='status')
print(real_value)
fd['Birth_year'] = 2026 - fd['age'] 
fd['age'] = fd['age'].astype(float)
fd['Birth_year'] = fh.to_datetime(fd['Birth_year'])
fd['name'] = fd['name'].str.capitalize()
fd['name'] = fd['name'].str.replace('o','a')
fd['name'] = fd['name'].str.strip()
fd['name'] = fd['name'].str.upper()
print(fd)

def age_check(age):
    if age < 24:
        return 'child'
    elif age < 34:
        return 'medium'
    else:
        return 'higher age'
fd['age_class'] = fd['age'].apply(age_check)

print(fd)
