import configparser
import os
import sqlite3


#读取ini方法
def read_ini(inikey,inivaluse):
        config = configparser.RawConfigParser()
        config.read("sb.ini", encoding='UTF-8')
        convaluse=config.get(inikey,inivaluse)
        return convaluse

conn = sqlite3.connect("sb.db")
c = conn.cursor()
key = 1
while key <= 3000 :
    if __name__ == '__main__':
        try :
            cont=read_ini("傻逼语录",str(key))
            print(cont)
            c.execute("insert into sba (id,content,info) \
                values ('%s','%s','%s') " % (key,cont,'None'));
            conn.commit()
        except :
            key += 1
        else :
            key += 1


conn.close()