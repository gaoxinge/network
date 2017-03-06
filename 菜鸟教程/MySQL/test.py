import MySQLdb

db = MySQLdb.connect('localhost','root','******')
cursor = db.cursor()

sql = 'show databases'
cursor.execute(sql)
results = cursor.fetchall()
print results

sql = 'use runoob'
cursor.execute(sql)

sql = 'show tables'
cursor.execute(sql)
results = cursor.fetchall()
print results

sql = '''create table employee(
         first_name char(20) not null,
         last_name char(20),
         age int,  
         sex char(1),
         income float)'''
cursor.execute(sql)

sql = """insert into employee(first_name, last_name, age, sex, income) values ('Mac', 'Mohan', 20, 'M', 2000), ('xinge', 'gao', '26', '10000')"""
cursor.execute(sql)
db.commit()

sql = 'delete from emplyee where age > 20'
cursor.execute(sql)
db.commit()

sql = 'select * from employee'
cursor.execute(sql)
results = cursor.fetchall()
print results

db.close()