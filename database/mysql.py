import pymysql

# con = pymysql.connect(host="localhost", user="root", password="")
con = pymysql.connect(host="localhost", user="root",password="", database="aaaa")

cur = con.cursor()

# cur.execute("show databases")
cur.execute("select * from tbl_products")


# print(cur)
# for i in cur:
#   print(i)


# result = cur.fetchall()
# for i in result:
#   print(i)


result = cur.fetchone()
# print(result)
for i in result:
  print(i)














