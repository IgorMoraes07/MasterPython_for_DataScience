import sqlite3

connection = sqlite3.connect('movie.db')

cursor = connection.cursor()

#|| Criando tabela no SQL Lite ||
# cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)''')

#|| Inserindo primeiro registro na tabela do SQL Lite ||
# cursor.execute('''INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)''')

#|| Inserindo registros na tabela do SQL Lite utilizando Tuplas ||
# famousFilms = [('Pulp Fiction', 'Quntin Tarantino', 1994), 
#                ('Back to the Future', 'Robert Zemeckis', 1985), 
#                ('Moonrise Kingdom', 'Wes Anderson', 2012)]

# cursor.executemany('INSERT INTO Movies VALUES (?, ?, ?)', famousFilms)

#|| Exibindo os registros da tabela do SQL Lite ||
# cursor.execute('''SELECT * FROM Movies''')

#|| Trazendo um registro da tabela do SQL Lite ||
# print(cursor.fetchone())

release_year = (1985, )

#|| Exibindo os registros filtrados da tabela do SQL Lite ||
cursor.execute('SELECT * FROM Movies WHERE year = (?)', release_year)

#|| Trazendo um registro da tabela do SQL Lite ||
print(cursor.fetchall())

connection.commit()
connection.close()
