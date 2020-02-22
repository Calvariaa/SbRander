import os
from flask import Flask, request
from plugins import SearchSb
from plugins import SearchId
from plugins import WriteSb
from plugins import WriteId

app = Flask("Search_Sb")

sytle_help = '<br>使用方法就是直接localhost:5000/?search=&type=<br>写入的话换成?write='
@app.route('/')
def Search_Sb():
    params = request.args
    r_str = ''
    w_str = ''

    if 'search' in params :
        r_str = params['search']
        print(r_str)
        if 'type' in params :
            if params['type'] == '1' :
                result = SearchSb.search(r_str)
                print(result)
                return result
            if params['type'] == '2' :
                result = SearchId.search(r_str)
                print(result)
                return result
            else :
                return 'Error in type ' + params['type']
        else :
            result = SearchSb.search(r_str)
            print(result)
            return result

    elif 'write' in params :
        w_str = params['write']
        print(w_str)
        if not w_str is None :
            if 'id' in params :
                result = WriteId.write(w_str,params['id'])
                return result
            else :
                result = WriteSb.write(w_str)
                return result

        if w_str is None :
            return 'Null'
 
 
if __name__ == '__main__':
    app.run(port=5000, debug=False)