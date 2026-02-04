from flask import Flask, request
import os

app = Flask(__name__)   # create an instance of the Flask class. The parameter __name__ that is given will make the application unique. 


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'username is ' + request.values["username"]
    else:
        return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5001)) 
    app.debug = True        # debug not in the production server.    
    app.run(host=host, port=port)