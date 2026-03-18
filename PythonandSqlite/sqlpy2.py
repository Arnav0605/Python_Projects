import sqlite3
conn=sqlite3.connect('univ.db')
cursor=conn.cursor()
rows=cursor.execute('select * from new')
tuples=rows.fetchall()
print(tuples)
cursor.close()
conn.close()