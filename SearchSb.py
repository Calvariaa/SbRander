import os
import sqlite3
import random

current_path = os.path.dirname(__file__)
conn = sqlite3.connect(current_path + "\sb.db",check_same_thread = False)
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
        randnum = random.randint(1,num) #随机到的项数
        result = count[randnum][1] #输出随机到的sb
    except :
        result = 'caonimabi'

    return result