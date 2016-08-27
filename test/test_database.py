#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","199306","gov" )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# ### 获取数据库版本号
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取一条数据库。
# data = cursor.fetchone()
# print "Database version : %s " % data

### 创建数据库表
# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("drop table if exists employee")
# 创建数据表SQL语句
sql = 'create table employee (first_name char(20) not null, last_name char(20), age int, sex char(1), income float)'
cursor.execute(sql)

# ### 数据库插入操作
# # SQL 插入语句
# # sql = """insert into employee (first_name, last_name, age, sex, income) values ('Mac', 'Mohan', 20, 'M', 2000)"""
# sql = "insert into employee (first_name, last_name, age, sex, income) values ('%s', '%s','%d','%c','%d')" % ('Mac', 'Mohan', 20, 'M', 20002)
# try:
    # # 执行sql语句
    # cursor.execute(sql)
    # # 提交到数据库执行
    # db.commit()
# except:
    # # Rollback in case there is any error
    # db.rollback()

# ### 数据库查询语句
# # 查询EMPLOYEE表中salary（工资）字段大于1000的所有数据
# sql = "select * from employee where income > '%d'" % (1000)
# try:
    # # 执行SQL语句
    # cursor.execute(sql)
    # # 获取所有记录列表
    # results = cursor.fetchall()
    # for row in results:
        # fname = row[0]
        # lname = row[1]
        # age = row[2]
        # sex = row[3]
        # income = row[4]
        # # 打印结果
        # print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             # (fname, lname, age, sex, income )
# except:
   # print "Error: unable to fecth data"

# ### 数据库更新语句
# # 更新操作用于更新数据表的的数据，以下实例将 TESTDB表中的 SEX 字段全部修改为 'M'，AGE 字段递增1：
# sql = "update employee set age = age + 1 where sex = '%c'" % ('M')
# try:
    # # 执行SQL语句
    # cursor.execute(sql)
    # # 提交到数据库执行
    # db.commit()
# except:
    # # 发生错误时回滚
    # db.rollback()

### 数据库删除语句
# 更新操作用于更新数据表的的数据，以下实例将 TESTDB表中的 SEX 字段全部修改为 'M'，AGE 字段递增1：
sql = "delete from employee where age > '%d'" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
    
# 关闭数据库连接
db.close()