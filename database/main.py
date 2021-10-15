import cgi
import pymysql
con = pymysql.connect(host="localhost", user="root",password="", database="meanapp")
cursor = con.cursor()

a="admin"
b="admin"

sql = "select id,email,username,password from users where username='"+a+"' AND password='"+b+"'"
cursor.execute(sql)
table = cursor.fetchall()
#print(table[0][2])

try:
 if(table):
   #print("Content-type: text/html")
   print("Successfully login")
   print(table[0][2])
 else:
   print("Fail")
except:
    cursor.close()
    con.close()