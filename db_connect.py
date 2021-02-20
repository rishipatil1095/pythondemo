import mysql.connector as data

db = data.connect(host= 'localhost',user='Rishi',passwd= 'rishi123',database = 'telusko')
mycursor = db.cursor()
mycursor.execute("select * from fighter")

for i in mycursor:
    print(type(i))