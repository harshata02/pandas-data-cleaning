


import pandas as pd

file_path =r'C:/Users/Welcome/Desktop/powerbi/sales_2015-2016.csv'

df = pd.read_csv(file_path)
print(df.head())

df['order_date']=pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])


df['order_date'] = df['order_date'].dt.strftime('%d-%m-%Y')
df['ship_date'] = df['ship_date'].dt.strftime('%d-%m-%Y')
print(df.head())

null_values=df.isnull().sum()
print(null_values)

df_clean =df.dropna(subset=['order_line','order_id','order_date','ship_date'])

print(df_clean)

df_clean1=df.dropna(subset=['ship_mode','customer_id','product_id','sales','quantity','discount','profit'])
print(df_clean1)

df_cleaned1 = df.fillna('nodata')
print(df_cleaned1)

df_sorted = df.sort_values(by=['order_line' ])
print(df_sorted.head())





df.to_csv('data_cleans.csv')

