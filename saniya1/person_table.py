import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table pers_saniya(name varchar(20),dob varchar(10),address varchar(20),pan_num integer)")
def insert_table():
    c.execute("insert into pers_saniya values('shaik saniya','1999-5-24','12-345',32728)")
    c.execute("insert into pers_saniya values('sana','1999-8-24','12-385',32628)")
    c.execute("insert into pers_saniya values('Afiya','1899-5-24','13-345',92728)")
    c.execute("insert into pers_saniya values('sony','1999-6-14','12-545',328908)")
    c.execute("insert into pers_saniya values('Reeha','2000-5-24','82-345',32568)")
    con.commit()
def update_table():
    c.execute("update pers_saniya set name='ali',address='12-545' where dob='199-6-14'")
    con.commit()
def del_table():
    c.execute("delete from pers_saniya where name='Afiya'")
def select_table():
    c.execute('select * from pers_saniya')
    data=c.fetchall()
    for row in data:
        print(row)
#c.execute('show tables')
#create_table()
#insert_table()
#del_table()
#update_table()
select_table()
c.close()
con.close()