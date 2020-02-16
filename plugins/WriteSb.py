import os
import sqlite3

conn = sqlite3.connect(os.getcwd() + "\sb.db",check_same_thread = False)
c = conn.cursor()

def write(str) :
    try :
        cursor = c.execute("insert into sba (id,content,info) \
            values (NULL,'%s','%s') " % (str,'None'));
        conn.commit()
        conn.close()
        result = 'Write ' + str + ' Success'
    except :
        result = 'Write ' + str + ' Failed'

    return result