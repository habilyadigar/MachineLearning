import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

first = pd.read_excel('data-end.xlsx',sheet_name='non-encode')

after = pd.read_excel('data-end.xlsx',sheet_name='encoded')

first = first.iloc[:, 0:]
after = after.iloc[:, 0:]

GerekenKolonlar = ['MODELLER','RENKLER','YILLAR','KM','FİYAT']

print(first)
print(after)

first = first[GerekenKolonlar]
after = after[GerekenKolonlar]

print(first.head(5))
print(after.head(5))

bagimliDegisken = 'FİYAT'

X = after[after.columns.difference([bagimliDegisken])]
y = after[[bagimliDegisken]]

print(X)
print(y)

LinearRegression = LinearRegression()
LinearRegression.fit(X,y)

joblib.dump(LinearRegression, 'car-model.pkl')
print("Model Oluşturuldu.")

LinearRegression = joblib.load("car-model.pkl")
modelKolonlari = list(X.columns)
joblib.dump(modelKolonlari,'car-model-kolonlari.pkl')
print("model Kolonları Oluşturuldu")
