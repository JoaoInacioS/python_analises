# %%
import pandas as pd
import numpy as np

cereal = pd.read_csv("cereal.csv",index_col=0)
cereal.head()

# %%
import statsmodels.api as sm
y = 'rating'

# %%
cereal.drop(['type','mfr','fat','sugars'], axis=1,inplace=True)
cereal.head()

# %%
modelo = sm.OLS(cereal[y], cereal.drop([y], axis=1))
res = modelo.fit()
print(res.summary())

# %%
