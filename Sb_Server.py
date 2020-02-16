import os
from flask import Flask, request
from plugins import SearchSb

app = Flask("Search_Sb")

sytle_help = '<br>使用方法就是直接localhost:5000/?search=<br>写入的话换成?write='
@app.route('/')
def Search_Sb():
    params = request.args
    r_str = ''
    w_str = ''

    if 'search' in params :
        r_str = params['search']
        result = SearchSb.search(r_str)
        print(r_str)
        print(result)
        return SearchSb.search(r_str)

    elif 'write' in params :
        w_str = params['write']
        print(w_str)
        return 'Read' + w_str + 'Success'
 
 
if __name__ == '__main__':
    app.run(port=5000, debug=False)