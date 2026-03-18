import sqlite3
conn=sqlite3.connect("PythonandSqlite/univ.db")
cursor=conn.cursor()
#cursor.execute('''insert into dept values(50,'Chemistry')''')
#cursor.execute(''' update dept set dname='IT' where deptno=50 ''')
cursor.execute(''' delete from dept where deptno=50 ''')
conn.commit()
cursor.close()
conn.close()
