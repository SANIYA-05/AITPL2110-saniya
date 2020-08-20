import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table saniya(regno varchar(10),name varchar(20))")
def insert_table():
    c.execute("insert into student values('AITPL211','dhanush')")
    con.commit()
def select_table():
    c.execute('select * from student')
    data=c.fetchall()
    for row in data:
        print(row)
#create_table()
#insert_table()
select_table()
c.close()
con.close()
# 1. create table employee( with column emp id,emp name,salary)
  #enter 5 rows,perform select,update,del operations
#2. create person table (with col name,dob,address,pan number)
#enter 5 rows,perform select,update,del operations
# 3. create table cars (with col car model numb,manufaturer,car name,price)
#enter 5 rows,perform select,update,del operations
# 4. create product table(with col product id,prod_name,prod_description,prod_price)
#enter 5 rows,perform select,update,del operations