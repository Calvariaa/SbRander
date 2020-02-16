import os
import sqlite3

conn = sqlite3.connect(os.getcwd() + "\sb.db",check_same_thread = False)
c = conn.cursor()

def write(str) :
    try :
        lir = c.execute("select sqlite_sequence.seq from \
            sqlite_sequence");
        lir = lir.fetchall()[0][0] + 1
        print(lir)
        cursor = c.execute("insert into sba (id,content,info) \
            values (NULL,'%s','%s') " % (str,'None'));
        result = 'Write ' + str + ' Success in %d'%lir
        conn.commit()
    except :
        result = 'Write ' + str + ' Failed in %d'%lir
    return result