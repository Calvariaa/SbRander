import os
import sqlite3
import random

conn = sqlite3.connect(os.getcwd() + "\sb.db",check_same_thread = False)
c = conn.cursor()

#if True :
#    id = input();
def search(id) :
    try :
        cursor = c.execute("SELECT \
	        id,content \
            FROM sba \
            where id='%s'" % id);
        count = cursor.fetchall()
    #    print(num) #输出查找到的总项数
        result =  '{"id"="%d","content"="'%count[0][0]+count[0][1]+'"}' #输出
    except :
        result = '喔唷，出现了一点点问题 \n' + 'Read id ' + id + ' Failed'

    #print(result)
    return result