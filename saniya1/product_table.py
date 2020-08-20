import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table prod_saniya(prod_id integer,prod_name varchar(40),prod_description varchar(40),price integer)")
def insert_table():
    c.execute("insert into prod_saniya values(4111,'One plus nord','the most hyped phone of 2020',29999)")
    c.execute("insert into prod_saniya values(3426,'Motorola fusion','the best midrange for indians',27999)")
    c.execute("insert into prod_saniya values(6845,'Samsung A30','the phone which left us confusing',45799)")
    c.execute("insert into prod_saniya values(1354,'Samsung galaxy X31','A new entry in  A series',32399)")
    c.execute("insert into prod_saniya values(8874,'Vivo x 50 pro','a phone which left us confusing',37499)")
    con.commit()
def update_table():
    c.execute("update prod_saniya set prod_id='8574' where price='37499'")
    con.commit()
def del_table():
    c.execute("delete from prod_saniya where prod_name='Samsung A30'")
def select_table():
    c.execute('select * from prod_saniya')
    data=c.fetchall()
    for row in data:
        print(row)

#create_table()
insert_table()
update_table()
del_table()
select_table()
c.close()
con.close()