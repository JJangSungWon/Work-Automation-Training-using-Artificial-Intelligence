import pandas as pd
import numpy as np

series = pd.Series([1, 3, 5, np.nan, 7, 9])
print(series)
print(series[series > 3.0]) #true만 반환

data = {'Name': 'DongSoo',
           'Age' : 21,
           'Height' : 180.2,
           'Weight' : 58.5,
           'Job' : 'student'}

columns = ['Name', 'Age', 'Height', 'Weight', 'Job']

df = pd.DataFrame(data=data, index=[0], columns=columns)

print(df)

#Excel
excel_path = 'dataset\\wine_dataset.xlsx'
'''
df = pd.read_excel(excel_path)

#Excel로 저장 가능
df.to_csv('test.csv')
df.head()
df.tail(3)
df.describe()
df.info()
df.columns
df.columns[2:4]
df.index
df.values
df['alcohol'].unique()
df.cov()
df.corr()
df.T
df.mean()
df.median()
df.apply(lambda x: x.max() - x.min())
print(df['alcohol'] > 14)

# 두  dataframe 합치기
pd.concat([first_group, sec_group])

#Nan이 있는 Row 없애기
df = df.dropna()

#Nan의 값을 사용자가 지정한 값으로 치환하기
df.fillna(value=0, inplace=True)

#Nan의 값을 mean으로 치환하기
mean = df['alcohol'].mean()
mean_filled = df.fillna(value=mean)

#Column명 바꾸기
renamed = df.rename(columns={'alcohol' : 'ALCOHOL'})
renamed.head()

#DataFrame을 Row를 기준으로 Random 하게 섞기
df = df.sample(frac=1)
df.head()

#섞인 DataFrame을 다시 순서대로 재배열하기
df = df.sort_index()
df.head()
'''