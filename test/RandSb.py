import os
import sqlite3
import random

conn = sqlite3.connect(os.getcwd() + "\sb.db",check_same_thread = False)
c = conn.cursor()


try :
    cursor = c.execute("SELECT content FROM sba");
    count = cursor.fetchall()
    num = len(count)
#    print(num) #输出总项数
    randnum = random.randint(1,num) #随机一个sb
#    print(randnum) #输出随机到的项数
    print(count[randnum][0]) #输出sb
except :
    print('没这一项啊')