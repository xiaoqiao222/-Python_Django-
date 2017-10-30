# -*- coding: utf-8 -*-
import cgi,cgitb,json
cgitb.enable()

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers  



fs = cgi.FieldStorage()

uid = fs["id"].value

# 链接数据库,在数据库中删除当前这个用户的数据



print(0)