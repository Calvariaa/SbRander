import os
import sqlite3
import random

conn = sqlite3.connect(os.getcwd() + "\sb.db",check_same_thread = False)
c = conn.cursor()

#str = input();
def search(str) :
    try :
        cursor = c.execute("SELECT * \
            FROM sba \
            WHERE content LIKE '%%%s%%'" % str);

        count = cursor.fetchall()
        num = len(count)
    #    print(num) #输出查找到的总项数
        randnum = random.randint(1,num) - 1 #随机到的项数
        result = count[randnum][1] #输出随机到的sb
    except :
        result = '喔唷，出现了一点点问题'

    return result