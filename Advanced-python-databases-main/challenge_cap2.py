import sqlite3

connection = sqlite3.connect('users-sqllite.db')

cursor = connection.cursor()

#|| Criando tabela no SQL Lite ||
cursor.execute('''CREATE TABLE IF NOT EXISTS Users 
               (UserId INTEGER PRIMARY KEY AUTOINCREMENT,
               FirstName TEXT,
               LastName TEXT,
               EmailAddress INT)''')

#|| Inserindo registros na tabela do SQL Lite utilizando Tuplas ||
AddUsers = [('Tony', 'Stark', 'tstark@gmail.com'), 
               ('Steve', 'Rodgers', 'steverodgers@gmail.com'), 
               ('Thor', 'Almighty', 'almightythor@gmail.com'), 
               ('Bruce', 'Banner', 'bbanner@gmail.com'), 
               ('Natasha', 'Romanova', 'blackwidow@gmail.com')]

print(AddUsers)

cursor.executemany('INSERT INTO Users (FirstName, LastName, EmailAddress) VALUES (?, ?, ?)', AddUsers)

#|| Exibindo os registros da tabela do SQL Lite ||
cursor.execute('SELECT * FROM Users')

#|| Trazendo um registro da tabela do SQL Lite ||
print(cursor.fetchall())

connection.commit()
connection.close()
