import pandas as pd

pd.DataFrame({ 'Yes': [50,21,5] ,'No': [131,2,21] })

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
'Sue': ['Pretty good.', 'Bland.']},index=['Product A', 'Product B'])



pd.Series([1, 2, 3, 4, 5])
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'],
name='Product A')

# -----------------------------------------------------------------------------------------

cereal = pd.read_csv("cereal.csv",index_col=0)

cereal.head()

cereal.rating
cereal["rating"]
cereal[["rating","sugars"]]
cereal["rating"][0:3]

cereal.iloc[0]
cereal.iloc[:,0]
cereal.iloc[0:3,0]
cereal.iloc[[0,3,5],0]
cereal.iloc[-5:]

cereal.loc['100% Bran','rating']
cereal.loc['100% Bran',['rating','sugars']]
cereal.loc[:,['rating','sugars']]
cereal.loc['100% Bran','sugars':'rating']

cereal.set_index('mfr') # referenciar para salvar alteração

cereal.loc[cereal['type']=='C']

cereal.loc[(cereal['mfr']=='K') & (cereal['rating']>50)]
cereal.loc[(cereal['mfr']=='K') | (cereal['rating']>50)]

cereal.loc[cereal.mfr.isin(['K',"N"])]


testna=pd.DataFrame({ 'Yes': [50,21,5,None] ,'No': [131,2,21,2] })
testna.loc[testna.Yes.notnull()]

cereal['index_backwards'] = range(len(cereal), 0, -1)
cereal['index_backwards']

# --------------------------------------------------------------------------------------

cereal.sugars.describe()
cereal.sugars.mean()
cereal.sugars.median()
cereal.mfr.unique()
cereal.mfr.value_counts()

cereal_sugars_mean = cereal.sugars.mean()
cereal.sugars.map(lambda p: p - cereal_sugars_mean)
# Elemento menos a média

def remean_sugars(row):
    row.sugars= row.sugars - cereal_sugars_mean
    return row

cereal.apply(remean_sugars,axis='columns')

cereal.sugars - cereal_sugars_mean


cereal.mfr + "_" + cereal.type
cereal.mfr + cereal.type

(cereal.sugars / cereal.carbo).idxmax()
cereal['mfr'].str.contains("K").sum()

# -------------------------------------------------------------

cereal.groupby('mfr').mfr.count()
cereal.groupby('mfr').sugars.mean()
cereal.groupby('mfr').sugars.max()
cereal.groupby('mfr').sugars.min()
cereal.groupby('mfr').sugars.describe()

cereal.groupby(['mfr','type']).sugars.mean()
cereal.groupby(['mfr','type']).size()

cereal.groupby(['mfr',"type"]).rating.agg([len,min,max])
cereal.groupby(['mfr',"type"]).rating.agg([len,min,max]).reset_index()
cereal.groupby(['mfr',"type"]).rating.agg([len,min,max]).sort_values(by='len',ascending=False)

cereal.groupby(['mfr',"type"])['rating','sugars'].mean()

# ---------------------------------------------------------------------------------------

cereal.dtypes

cereal['calories'].astype('float64')

testna[pd.isnull(testna.Yes)]

testna.Yes.fillna(testna.Yes.mean()) # acrescentar valor para nulo

cereal.mfr.replace('K',"K2")
cereal.sugars.replace(-1,0).min()

# -------------------------------------------------------------------------------------

cereal.rename(columns={'rating':'nota','type':'tipo'})
cereal.rename(index={'100% Bran':'Bran 100%'})

banco1=pd.DataFrame({ 'Yes': [50,21,5,2] ,'No': [131,2,21,2] ,"tipo":['a','a','b','b']})
banco2=pd.DataFrame({ 'Yes': [40,2,4,7] ,'No': [150,3,5,1] ,"tipo":['a','c','b','c']})

pd.concat([banco1,banco2],axis=0)

pd.merge(banco1,banco2,on=['tipo'])

banco1.tipo.drop_duplicates()

# ----------------------------------------------------------------------------------------

cereal.columns
cereal.index
cereal=cereal.replace(-1,None)
cereal=cereal.dropna(axis=0)




