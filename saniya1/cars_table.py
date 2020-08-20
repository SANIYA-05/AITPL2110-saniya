import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table cars_saniya(model_num varchar(20),manufacturer varchar(20),car_name varchar(40),price varchar(20))")
def insert_table():
    c.execute("insert into cars_saniya values('911','Porsche','Porsche 911 speedster','$274,500')")
    c.execute("insert into cars_saniya values('1800TU','Bently','Bently Continental GT','$236,100')")
    c.execute("insert into cars_saniya values('HPE 800','Ford','Ford Mustang','$99,500')")
    c.execute("insert into cars_saniya values('xj220','Jaguar','Jaguar XJ','$89,870')")
    c.execute("insert into cars_saniya values('1774hj','Tesla','Tesla Roadster','$200,000')")
    con.commit()
def update_table():
    c.execute("update cars_saniya set model_num='174hj' where price='$200,000'")
    con.commit()
def del_table():
    c.execute("delete from cars_saniya where car_name='Ford Mustang'")
def select_table():
    c.execute('select * from cars_saniya')
    data=c.fetchall()
    for row in data:
        print(row)

#create_table()
#insert_table()
update_table()
del_table()
select_table()
c.close()
con.close()