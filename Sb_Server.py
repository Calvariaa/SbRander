import os
from flask import Flask, request
import SearchSb

app = Flask("Search_Sb")

@app.route('/')
def Search_Sb():
    str = request.args.get('search')
    result = SearchSb.search(str)
    print(str)
    print(result)
    return SearchSb.search(str)
 
 
if __name__ == '__main__':
    app.run(port=5000, debug=True)