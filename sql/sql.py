
# %%
# Caso não esteja usando o Colab, instale na sua maquina
# pip install sqlite3

# Biblioteca
import sqlite3


# %%
from platform import python_version

print(python_version())

# %%
# Criar um banco de dados
Conexao = sqlite3.connect('Banco_Dados')

# %%
# Apontar para o banco
Cursor = Conexao.cursor()

# %%
# Criar tabela --------------------------------------------------

# Criando uma tabela
Cursor.execute(
    'CREATE TABLE Minha_Tabela ( Data text, Nome text, Idade real ) '
)

# FAzer um commit
Conexao.commit()

# %%
# Inserindo valores
Cursor.execute(' INSERT INTO Minha_Tabela VALUES ( "01/01/2021", "Odemir", "30" ) ')

# %%
Cursor.execute(' INSERT INTO Minha_Tabela VALUES ( "05/01/2021", "Lucas", "30" ) ')

# %%
# Importar Numeros aleatorios
import random

# Loop
for Loop in range(10):
  
  # Gernado um numero aleatorio
  Numero = random.randint(10, 20)
  
  # Inserir informação na minha tabela  
  Cursor.execute( f' INSERT INTO Minha_Tabela VALUES ( "05/01/2021", "Lucas", {Numero} ) ')

# %%
# Query de consulta - Todas as Colunas
Consulta = Cursor.execute('SELECT * FROM Minha_Tabela').fetchall()
print( Consulta )

# %%
# Query de consulta - Colunas Especificas
Consulta = Cursor.execute('SELECT Nome, Idade FROM Minha_Tabela').fetchall()

# Loop
for Linha in Consulta:
  print( Linha )

# %%
# Query usando o Igual "="
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Nome = 'Odemir'
    '''
).fetchall()

print( Consulta )

# %%
# Query usando o Igual ">"
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Idade > 25
    '''
).fetchall()

print( Consulta )

# %%
# Query usando o Igual "<>"
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Nome <> 'Odemir'
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


# %%
  # Query usando o BetWeen
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE idade BETWEEN 15 AND 20
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


# %%
# Query procurando algo que começe 
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Nome LIKE 'O%'
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


# %%
# Query procurando algo que termine com
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Nome LIKE '%s'
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


  
# %%
# Query procurando algo que tenha o padrão
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Nome LIKE '%uc%'
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


# %%
# Query procurando algo com o IN
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Idade IN (18, 20, 30)
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


# %%
# Query procurando algo com o IN
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    WHERE Nome IN ('Odemir')
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


# %%
# ANd
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    WHERE Idade = 15 AND Nome = 'Lucas'
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# OR
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    WHERE Idade = 15 OR Nome = 'Odemir'
    '''
).fetchall()


for Linha in Consulta:
  print( Linha )


# %%
# NOT
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    WHERE NOT Nome = 'Lucas'
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Combinação de Parametros AND OR NOT
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    WHERE Nome = 'Lucas' AND ( Idade > 15 AND Idade < 20 ) AND NOT Idade = 15
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Ordenando os valore
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    ORDER BY Idade, Nome
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Ordenando os valores decrecente
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    ORDER BY Idade DESC
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )



# %%
# Preenchendo valores nulos
Cursor.execute('INSERT INTO Minha_Tabela VALUES ("ABC", null, 30 ) ')
Cursor.execute('INSERT INTO Minha_Tabela VALUES ("ABC", null, null ) ')

# %%
# Verificando valores nulos
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    WHERE Nome IS NULL
    '''
).fetchall()

print( Consulta )

# %%
# Verificando valores não nulos
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    WHERE Nome IS NOT NULL
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


# %%
# Verificando valores não nulos
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Verificando valores não nulos
Consulta = Cursor.execute(
    ''' 
    UPDATE Minha_Tabela
    SET Nome = 'Preenchido'
    WHERE Nome IS NULL
    '''
).fetchall()

# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


# %%
# Verificando valores não nulos
Consulta = Cursor.execute(
    ''' 
    UPDATE Minha_Tabela
    SET Idade = 29
    WHERE Idade IS NULL
    '''
).fetchall()

# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Verificando valores não nulos
Consulta = Cursor.execute(
    ''' 
    DELETE from Minha_Tabela
    WHERE Nome = 'Preenchido'
    '''
).fetchall()

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Verificando valores não nulos
Consulta = Cursor.execute(
    ''' 
    DELETE from Minha_Tabela
    WHERE Nome = 'Lucas' AND Idade = 15
    '''
).fetchall()

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Minha_Tabela
    LIMIT 5
    '''
).fetchall()

# Mostrando o retorno
for Linha in Consulta:
  print( Linha )

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT MIN (Idade) FROM Minha_Tabela
    '''
).fetchall()

# Mostrando o retorno
print( Consulta )

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT MAX (Idade) FROM Minha_Tabela
    '''
).fetchall()

# Mostrando o retorno
print( Consulta )

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT COUNT (Idade) FROM Minha_Tabela
    '''
).fetchall()

# Mostrando o retorno
print( Consulta )

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT AVG (Idade) FROM Minha_Tabela
    '''
).fetchall()

# Mostrando o retorno
print( Consulta )

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT SUM (Idade) FROM Minha_Tabela
    '''
).fetchall()

# Mostrando o retorno
print( Consulta )

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT Idade AS Cadastro_clientes FROM Minha_Tabela
    '''
).fetchall()

# Mostrando o retorno
for Linha in Consulta:
  print( Linha )






# %%
# Verificando

#### --- ID do Vendedor e valor de venda dele
Consulta = Cursor.execute(
    ''' 
    CREATE TABLE Tab_Vendas (id real, valor real)
    '''
)

# Criando a tabela
Conexao.commit()

# %%
# Verificando

#### --- Dados Cadastrais dos vendedores
Consulta = Cursor.execute(
    ''' 
    CREATE TABLE Tab_Cadastro_Vendedor (id real, nome text)
    '''
)

# Criando a tabela
Conexao.commit()

# %%
# Vendas dos vendedores
Cursor.execute( 'INSERT INTO Tab_Vendas VALUES (1, 100) ' )
Cursor.execute( 'INSERT INTO Tab_Vendas VALUES (1, 200) ' )
Cursor.execute( 'INSERT INTO Tab_Vendas VALUES (1, 150) ' )

Cursor.execute( 'INSERT INTO Tab_Vendas VALUES (2, 50) ' )
Cursor.execute( 'INSERT INTO Tab_Vendas VALUES (2, 200) ' )
Cursor.execute( 'INSERT INTO Tab_Vendas VALUES (2, 900) ' )

# %%
# Vendas dos vendedores
Cursor.execute( 'INSERT INTO Tab_Cadastro_Vendedor VALUES (1, "Odemir Depieri Jr") ' )
Cursor.execute( 'INSERT INTO Tab_Cadastro_Vendedor VALUES (2, "Lucas Calmon") ' )

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Tab_Vendas
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Tab_Cadastro_Vendedor
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )




# %%
# Verificando INNER JOIN
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Tab_Vendas
    INNER JOIN Tab_Cadastro_Vendedor
    ON Tab_Vendas.id = Tab_Cadastro_Vendedor.id
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


# %%
Cursor.execute( 'INSERT INTO Tab_Vendas VALUES (3, 9999) ' )

# %%

# Verificando
Consulta = Cursor.execute(
    ''' 
    SELECT * FROM Tab_Vendas
    LEFT JOIN Tab_Cadastro_Vendedor
    ON Tab_Vendas.id = Tab_Cadastro_Vendedor.id
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )



# %%
# Criar tabelas
Cursor.execute(' CREATE TABLE Tabela_X ( Id real, Nome text )')
Conexao.commit()

Cursor.execute(' CREATE TABLE Tabela_Y ( Id real, Nome text )')
Conexao.commit()

# %%

# Inserir valores
Cursor.execute(' INSERT INTO Tabela_X VALUES ( 1, "Odemir" )')
Cursor.execute(' INSERT INTO Tabela_X VALUES ( 2, "Maria" )')
Cursor.execute(' INSERT INTO Tabela_X VALUES ( 3, "Joao" )')

Cursor.execute(' INSERT INTO Tabela_Y VALUES ( 1, "Mario" )')
Cursor.execute(' INSERT INTO Tabela_Y VALUES ( 2, "Luigui" )')
Cursor.execute(' INSERT INTO Tabela_Y VALUES ( 3, "Mariana" )')

# %%
# Consulta
Consulta = Cursor.execute(
    '''
    SELECT * FROM Tabela_X
    '''
).fetchall()

print( Consulta )

# %%
# Consulta
Consulta = Cursor.execute(
    '''
    SELECT * FROM Tabela_Y
    '''
).fetchall()

print( Consulta )

# %%
# Consulta
Consulta = Cursor.execute(
    '''
    SELECT * FROM Tabela_Y
    UNION ALL
    SELECT * FROM Tabela_X
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )


# %%
# Consulta
Consulta = Cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Consulta
Consulta = Cursor.execute(
    '''
    SELECT SUM (Idade) FROM Minha_Tabela
    WHERE Nome = 'Lucas'
    GROUP BY Nome
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Consulta
Consulta = Cursor.execute(
    '''
    SELECT COUNT (Idade) FROM Minha_Tabela
    GROUP BY Nome
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Consulta
Consulta = Cursor.execute(
    '''
    SELECT MAX (Idade) FROM Minha_Tabela
    GROUP BY Nome
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Consulta
Consulta = Cursor.execute(
    '''
    SELECT MIN (Idade) FROM Minha_Tabela
    GROUP BY Nome
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Consulta
Consulta = Cursor.execute(
    '''
    SELECT AVG (Idade) FROM Minha_Tabela
    GROUP BY Nome
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )

# %%
# Consulta
Consulta = Cursor.execute(
    '''
    -- Selecionado a tabela x
    SELECT * FROM Minha_Tabela
    '''
).fetchall()

for Linha in Consulta:
  print( Linha )




# %%
Query = '''
CREATE TABLE Clientes (
    ID int NOT NULL,
    Nome varchar(255) NOT NULL,
    Sobrenome varchar(255),
    Idade int,
    PRIMARY KEY (ID)
) 
'''
# %%
# Fazendo consulta
Consulta = Cursor.execute( Query )

# Salvar as alterações no banco de dados
Conexao.commit()


# Inserindo valores
Cursor.execute("INSERT INTO Clientes VALUES (1, 'Odemir', 'Depieri',  30)")

Cursor.execute("INSERT INTO Clientes VALUES (2, 'Ronisson', 'Lucas',  30)")

# %%
Cursor.execute( "SELECT * FROM Clientes").fetchall()


# %%
Query = '''
CREATE TABLE Servicos (
    ID int NOT NULL,
    Numero int NOT NULL,
    IDCliente int,
    PRIMARY KEY (ID),
    FOREIGN KEY (IDCliente) REFERENCES Persons(IDCliente)
)
'''

# Fazendo consulta
Consulta = Cursor.execute( Query )

# Salvar as alterações no banco de dados
Conexao.commit()

# %%
Cursor.execute("INSERT INTO Servicos VALUES (1, 1000, 1)")

# %%
Cursor.execute( "SELECT * FROM Servicos").fetchall()

# %%

# %%
# Projeto prático ----------------------------------------------------------------

# Loja de Sapatos

# Gerando dados de vendas
# ID Vendedor, Valor de Bruto, Desconto, Valor Líquido

Query_01 = '''
CREATE TABLE Vendas (
    ID INT NOT NULL,
    ID_Vendedor INT NOT NULL,
    ValorVenda INT NOT NULL,
    Desconto INT NOT NULL,
    PRIMARY KEY (ID)
) 
'''

Query_02 = '''
CREATE TABLE Vendedor (
    ID_Vendedor INT NOT NULL,
    Nome varchar(255) NOT NULL,
    PRIMARY KEY (ID_Vendedor)
)
'''

Consulta = Cursor.execute( Query_01 )
Conexao.commit()

Consulta = Cursor.execute( Query_02 )
Conexao.commit()

# %%
Cursor.execute("INSERT INTO Vendedor VALUES (1, 'Odemir Depieri Jr')")
Cursor.execute("INSERT INTO Vendedor VALUES (2, 'Jose Almeida')")
Cursor.execute("INSERT INTO Vendedor VALUES (3, 'Maria Silva')")
Cursor.execute("INSERT INTO Vendedor VALUES (4, 'Julia Pereira')")

# %%
Query = '''
SELECT * FROM Vendedor
'''

# Fazendo consulta
Consulta = Cursor.execute( Query ).fetchall()

# Mostrando o retorno
print( Consulta )

# %%
import random

for Input in range(100):

  Id = Input
  Vendedor = random.randint(1, 4)
  Valor_Venda = random.randint( 30, 599 )
  Desconto = round( random.random() * 100, 2 )

  #print( Id, Vendedor, Valor_Venda, Desconto )
  Cursor.execute( f"INSERT INTO Vendas VALUES ( {Id}, {Vendedor}, {Valor_Venda}, {Desconto} )" )

# %%
Query = '''
SELECT * FROM Vendas
'''

# Fazendo consulta
Consulta = Cursor.execute( Query ).fetchall()

# Mostrando o retorno
for Linha in Consulta[0:10]:
  print( Linha )

# %%
Query = '''

-- Seleção das Tabelas e Join
SELECT Nome, SUM(Vendas.ValorVenda) as TopVendas, COUNT(Vendas.ValorVenda), AVG(Vendas.ValorVenda)
FROM Vendas
INNER JOIN Vendedor
ON Vendedor.ID_Vendedor = Vendas.ID_Vendedor

-- Filtro
WHERE Nome = 'Odemir Depieri Jr' or Nome = 'Maria Silva'

-- Agrupamento
GROUP BY Nome
ORDER BY TopVendas DESC
'''

# Fazendo consulta
Consulta = Cursor.execute( Query ).fetchall()

# Mostrando o retorno
for Linha in Consulta:
  print( Linha )
# %%
