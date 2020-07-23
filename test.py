import pymysql

db = pymysql.connect("localhost","root","","python" )

cursor = db.cursor()

sql = """DROP TABLE PEOPLE"""
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()