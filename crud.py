# import mysql.connector

# try:
#     conn=mysql.connector.connect(
#         user='',
#         password='',
#         host='localhost',
#         port=3306

#     )
#     if (conn.is_connected()):
#         print("Connected")

# except:
#     print("Unable to connect")


# conn.close()


# create database
# import mysql.connector

# Conn=mysql.connector.connect(
#     user="",
#     password='',
#     host='localhost',
#     port=3306
# )

# sql="CREATE DATABASE p3"
# mys=Conn.cursor()
# mys.execute(sql)

# mys.close()
# Conn.close()


# create table

# import mysql.connector

# try:
#     conn=mysql.connector.connect(
#     user='',
#     password='',
#     host='localhost',
#     port=3306,
#     database='p3'
# )   
#     print("Connected")

# except:
#     print("Unable to connect")   


# sql="CREATE TABLE student1(id INT AUTO_INCREMENT PRIMARY KEY ,name VARCHAR(10) ,age INT(2), course VARCHAR(10),fees Float(5))"
# mys=conn.cursor()
# mys.execute(sql)


# mys.close()
# conn.close()



# insert table


# import mysql.connector

# try:
#     conn=mysql.connector.connect(
#     user='',
#     password='',
#     host='localhost',
#     port=3306,
#     database='p3'
# )   
#     print("Connected")

# except:
#     print("Unable to connect")   


# sql='INSERT INTO student1(name,age,course,fees) VALUES("ram",18,"bca",22000),("sita",22,"btech",33000)'
# mys=conn.cursor()


# try:
#     mys.execute(sql)
#     conn.commit()
#     print("data inserted")
# except:
#     conn.rollback()
#     print("data is not inserted")


# delete data in database

# import mysql.connector

# try:
#     conn=mysql.connector.connect(
#     user='',
#     password='',
#     host='localhost',
#     port=3306,
#     database='p3'
# )   
#     print("Connected")

# except:
#     print("Unable to connect")   

# sql='DELETE FROM student1 WHERE id=1'
# mys=conn.cursor()


# try:
#     mys.execute(sql)
#     conn.commit()
#     print(mys.rowcount,"data deleted in row") # this told me how row is insert in mysql  number row is inserted

# except:
#     conn.rollback()
#     print("data is not deleted")

# mys.close()
# conn.close()

# retrive data

# import mysql.connector

# try:
#     conn=mysql.connector.connect(
#     user='',
#     password='',
#     host='localhost',
#     port=3306,
#     database='p3'
# )   
#     print("Connected")

# except:
#     print("Unable to connect")   


# sql='select id,name,age from student1'
# mys=conn.cursor()


# try:
#     mys.execute(sql)
#     row= mys.fetchone()
#     while row is not None:
#         print(row)
#         row=mys.fetchone()

        
#     print(mys.rowcount,"total row") 

# except:
#     conn.rollback()
#     print("data is not retrive")

# mys.close()
# conn.close()


# using fatchall(),fatchmany() method

# updata data in mysql

# import mysql.connector

# try:
#     conn=mysql.connector.connect(
#     user='',
#     password='',
#     host='localhost',
#     port=3306,
#     database='p3'
# )   
#     print("Connected")

# except:
#     print("Unable to connect")   


# sql='UPDATE student1 set age=127 where id =2'
# mys=conn.cursor()


# try:
#     mys.execute(sql)
#     conn.commit()
#     print(mys.rowcount,"data update in row") # this told me how row is insert in mysql  number row is inserted

# except:
#     conn.rollback()
#     print("data is not update")

# mys.close()
# conn.close()

# crud using user
import mysql.connector
conn=mysql.connector.connect(
    user='',
    password='',
    host='',
    port='', 
    database='s1'
)

if conn.is_connected:
    print("connected")
else:
    print("not connected")

# sql='create database s1'
# myc=conn.cursor()
# myc.execute(sql)





# sql='create table s1(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30),age INT(3))'
# myc=conn.cursor()
# myc.execute(sql)

# sql="insert into s1(name,age)value('mohan',24)"
# myc=conn.cursor()

# try:
#     myc.execute(sql)
#     conn.commit()
# except:
#     conn.rollback()
#     print('data is not inserted')


# sql="update s1 set name='govind' where id=4"
# myc=conn.cursor()

# try:
#     myc.execute(sql)
#     conn.commit()
#     print("data is update")
# except:
#     conn.rollback()
#     print('data is not update')

# sql='delete from s1 where id=4'
# myc=conn.cursor()
# try:
#     myc.execute(sql)
#     conn.commit()
#     print('data is deleted')
# except:
#     conn.rollback()
#     print('data is not deleted')
    
# myc.close()
# conn.close()

# sql='select name,age from s1'
# myc=conn.cursor()
# try:
#     myc.execute(sql)
#     row=myc.fetchone()
#     while row is not None:
#         print(row)
#         row=myc.fetchone()
# except:
#     conn.rollback()
#     print('data is not retrieve')

# myc.close()
# conn.close()


# sql='select id,name,age from s1'
# mys=conn.cursor()


# try:
#     mys.execute(sql)
#     row= mys.fetchone()
#     while row is not None:
#         print(row)
#         row=mys.fetchone()

        
#     print(mys.rowcount,"total row") 

# except:
#     conn.rollback()
#     print("data is not retrive")

# mys.close()
# conn.close()