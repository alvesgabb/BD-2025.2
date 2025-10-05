import sqlite3

conn = sqlite3.connect('meu_banco.db')
cursor= conn.cursor()

cursor.execute ("""CREATE TABLE IF NOT EXISTS agencia
                (id_agencia INTERGER PRIMARY KEY,
                nome TEXT NOT NULL,cidade TEXT NOT NULL)""")

print("======Agência Bancaria=======")