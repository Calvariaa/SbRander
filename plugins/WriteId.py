import os
import sqlite3

conn = sqlite3.connect(os.getcwd() + "\sb.db",check_same_thread = False)
c = conn.cursor()
#if True :
#    str = input()
#    id = input()
def write(str,id) :
    try :
        cursor = c.execute("update sba set content='%s' \
            where id=%d " % (str,int(id)));
        result = 'Write ' + str + ' Success in %d'%int(id)
        conn.commit()
    except :
        result = 'Write ' + str + ' Failed in %d'%int(id)
    
    #print(result)
    return result