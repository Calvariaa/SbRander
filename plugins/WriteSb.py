import os
import sqlite3

conn = sqlite3.connect(os.getcwd() + "\sb.db",check_same_thread = False)
c = conn.cursor()

#def search(str) :
if 1 :
    try :
        cursor = c.execute("select * from sensor where order by id desc limit 0,1;");

        count = cursor.fetchall()
        result = count #输出
    except :
        result = 'caonimabi'

    #return result
    print(result)