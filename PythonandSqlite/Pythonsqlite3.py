import sqlite3
conn=sqlite3.connect("PythonandSqlite/univ.db")
cursor=conn.cursor()
#rows=cursor.execute('SELECT name from students s,dept d where s.deptno=d.deptno and dname="CSE"')
#rows=cursor.execute('select * from students where deptno=30 except select * from students where city!="MUM"')
#rows=cursor.execute('select city,count(name) from students where deptno=20 group by city'))
rows=cursor.execute('''select deptno,count(*)
                     from students
                     group by deptno
                     having count(*)>
                     (select count(*)
                        from students
                        where deptno=20)'''
                      )
                    
tuples=rows.fetchall()
for t in tuples:
    print(t)
cursor.close()
conn.close()