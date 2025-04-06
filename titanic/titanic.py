import pandas as pd
import numpy as np
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

train.head()

from sklearn.ensemble import RandomForestClassifier

# random_state <=> semente para o modelo
modelo = RandomForestClassifier(n_estimators=100,n_jobs=-1,random_state=0)

train['Sex'].value_counts()

variabeis = ['Sex_binario','Age']

def tranformar_sexo(valor):
    if valor == 'female':
        return 1
    else:
        return 0

train['Sex_binario'] = train['Sex'].map(tranformar_sexo)

X = train[variabeis]
y = train['Survived']
X = X.fillna(-1)


modelo.fit(X, y)


test['Sex_binario'] = test['Sex'].map(tranformar_sexo)
X_prev = test[variabeis]
X_prev = X_prev.fillna(-1)
X_prev.head()

p = modelo.predict(X_prev)
sub = pd.Series(p, index=test['PassengerId'], name='Survived')
sub.shape

sub.to_csv("primeiro_modelo.csv",header=True)

# ----------------------------------------------------------

from sklearn.model_selection import train_test_split

np.random.seed(0)
train_test_split(np.arange(10),test_size=0.5)

np.random.seed(0)
X_treino, X_valid, y_treino, y_valid = train_test_split(X, y,test_size=0.5)
X_treino.shape

modelo.fit(X_treino,y_treino)
p = modelo.predict(X_valid)
np.mean(y_valid == p)

p1=(X_valid['Sex_binario'] == 1).astype(np.int64)
np.mean(y_valid == p1)

# ----------------------------------------------------------

## Validação cruzada:

from sklearn.model_selection import KFold

X_falso = np.arange(10)

kf = KFold(2,shuffle=True,random_state=0)
for linhas_treino, linhas_valid in kf.split(X_falso):
    print("Treino:",linhas_treino)
    print("Valid:",linhas_valid)
    print()

# ---------- #

kf = KFold(2,shuffle=True,random_state=0)

resultados = []

for linhas_treino, linhas_valid in kf.split(X):
    print("Treino:",linhas_treino.shape[0])
    print("Valid:",linhas_valid.shape[0])
    print()

    X_treino, X_valid = X.iloc[linhas_treino], X.iloc[linhas_valid]
    y_treino, y_valid = y.iloc[linhas_treino], y.iloc[linhas_valid]

    modelo = RandomForestClassifier(n_estimators=100,n_jobs=-1,random_state=0)
    modelo.fit(X_treino,y_treino)

    p = modelo.predict(X_valid)
    acc = np.mean(y_valid == p)

    resultados.append(acc)
    print("Acc:",acc)
    print()
    #print(X_treino.head())
    #print()

np.mean(resultados)

# ----------------------------------------------------------

from sklearn.model_selection import RepeatedKFold

kf = RepeatedKFold(n_splits= 2,n_repeats=10,random_state=10)

resultados = []

for linhas_treino, linhas_valid in kf.split(X):
    print("Treino:",linhas_treino.shape[0])
    print("Valid:",linhas_valid.shape[0])
    print()

    X_treino, X_valid = X.iloc[linhas_treino], X.iloc[linhas_valid]
    y_treino, y_valid = y.iloc[linhas_treino], y.iloc[linhas_valid]

    modelo = RandomForestClassifier(n_estimators=100,n_jobs=-1,random_state=0)
    modelo.fit(X_treino,y_treino)

    p = modelo.predict(X_valid)
    acc = np.mean(y_valid == p)

    resultados.append(acc)
    print("Acc:",acc)
    print()
    #print(X_treino.head())
    #print()

np.mean(resultados)

%matplotlib inline
%pylab inline

pylab.hist(resultados)

# ------------------------#

variabeis=['Sex_binario', 'Age','Pclass','SibSp','Parch','Fare']

X = train[variabeis].fillna(-1)
y = train['Survived']

kf = RepeatedKFold(n_splits= 2,n_repeats=10,random_state=10)

resultados = []

for linhas_treino, linhas_valid in kf.split(X):
    print("Treino:",linhas_treino.shape[0])
    print("Valid:",linhas_valid.shape[0])
    print()

    X_treino, X_valid = X.iloc[linhas_treino], X.iloc[linhas_valid]
    y_treino, y_valid = y.iloc[linhas_treino], y.iloc[linhas_valid]

    modelo = RandomForestClassifier(n_estimators=100,n_jobs=-1,random_state=0)
    modelo.fit(X_treino,y_treino)

    p = modelo.predict(X_valid)
    acc = np.mean(y_valid == p)

    resultados.append(acc)
    print("Acc:",acc)
    print()
    #print(X_treino.head())
    #print()

np.mean(resultados)

%matplotlib inline
%pylab inline

pylab.hist(resultados)

# Retreinar: (Todos os dados)

X.head()
y.head()
test[variabeis].head()

modelo = RandomForestClassifier(n_estimators=100,n_jobs=-1,random_state=0)
modelo.fit(X,y)
p = modelo.predict(test[variabeis].fillna(-1))

# ----------------------------------------------------------

X_valid_check = train.iloc[linhas_valid].copy()
X_valid_check['p'] = p
train.head()

erros = X_valid_check[X_valid_check['Survived'] != X_valid_check['p']]
list(erros.columns)
erros = erros[['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch','Ticket', 'Fare', 'Cabin', 'Embarked', 'Sex_binario', 'Survived', 'p']]
erros.head()

mulheres = erros[erros['Sex'] == 'female']
homens = erros[erros['Sex'] == 'male']

mulheres.sort_values("Survived")
homens.sort_values("Survived")

# novas variáveis analisadas (ideias): ---------------------------------------

train['Embarked_S'] = (train['Embarked'] == 'S').astype(int)
train['Embarked_C'] = (train['Embarked'] == 'C').astype(int)
#train['Embarked_Q'] = (train['Embarked'] == 'Q').astype(int)

train['Cabine_nula'] = train["Cabin"].isnull().astype(int)

train['Nome_contem_Miss'] = train['Name'].str.contains("Miss").astype(int)
train['Nome_contem_Mrs'] = train['Name'].str.contains("Mrs").astype(int)

train['Nome_contem_Master'] = train['Name'].str.contains("Master").astype(int)
train['Nome_contem_Col'] = train['Name'].str.contains("Col").astype(int)
train['Nome_contem_Major'] = train['Name'].str.contains("Major").astype(int)
train['Nome_contem_Mr'] = train['Name'].str.contains("Mr").astype(int)

train.head()
list(train.columns)

variabeis = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_binario', 'Embarked_S', 'Embarked_C', 'Cabine_nula', 'Nome_contem_Miss', 'Nome_contem_Mrs', 'Nome_contem_Master', 'Nome_contem_Col', 'Nome_contem_Major', 'Nome_contem_Mr']

X = train[variabeis].fillna(-1)
y = train['Survived']

kf = RepeatedKFold(n_splits= 2,n_repeats=10,random_state=0)

resultados2 = []
for linhas_treino, linhas_valid in kf.split(X):
    print("Treino:",linhas_treino.shape[0])
    print("Valid:",linhas_valid.shape[0])
    print()

    X_treino, X_valid = X.iloc[linhas_treino], X.iloc[linhas_valid]
    y_treino, y_valid = y.iloc[linhas_treino], y.iloc[linhas_valid]

    modelo = RandomForestClassifier(n_estimators=100,n_jobs=-1,random_state=0)
    modelo.fit(X_treino,y_treino)

    p = modelo.predict(X_valid)
    acc = np.mean(y_valid == p)

    resultados2.append(acc)
    print("Acc:",acc)
    print()
    #print(X_treino.head())
    #print()

np.mean(resultados2)

#%matplotlib inline
#%pylab inline

pylab.hist(resultados2), pylab.hist(resultados,alpha=0.8)


# Regressão logistica -----------------------------------------------------

from sklearn.linear_model import LogisticRegression

resultados3 = []
kf = RepeatedKFold(n_splits= 2,n_repeats=10,random_state=10)

for linhas_treino, linhas_valid in kf.split(X):
    print("Treino:",linhas_treino.shape[0])
    print("Valid:",linhas_valid.shape[0])
    print()

    X_treino, X_valid = X.iloc[linhas_treino], X.iloc[linhas_valid]
    y_treino, y_valid = y.iloc[linhas_treino], y.iloc[linhas_valid]

    modelo = LogisticRegression()
    modelo.fit(X_treino,y_treino)

    p = modelo.predict(X_valid)
    acc = np.mean(y_valid == p)

    resultados3.append(acc)
    print("Acc:",acc)
    print()
    #print(X_treino.head())
    #print()

np.mean(resultados3)

pylab.hist(resultados3), pylab.hist(resultados,alpha=0.8)