import sqlite3
conn=sqlite3.connect('univ.db')
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS new (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
for i in range(3):
    id=int(input("Enter ID: "))
    name=str(input("Enter Name: "))
    age=int(input("Enter Age: "))  
    cursor.execute('INSERT INTO new VALUES (?, ?, ?)', (id, name, age))
    rows=cursor.execute('SELECT * FROM new')
conn.commit()
cursor.close()
conn.close()