import sqlite3
con=sqlite3.connect('db6.sqlite3')
c=con.cursor()
def create():
    c.execute('create table student( regno text,name text)')
    print("tabel created sucessfully")
def insert():
    c.execute("insert into student values ('001','saniya')")
    c.execute("insert into student values ('002','ali')")
    c.execute("insert into student values ('003','reena')")
    c.execute("insert into student values ('004','meena')")
    print("values inserted into a tabel")
    con.commit()
def select():
    c.execute('select * from student')
    data=c.fetchall()
    for row in data:
        print(row)
#c.execute('update student set regno="100" where name="saniya"')
    c.close()
    con.close()
#create()
#insert()
select()
