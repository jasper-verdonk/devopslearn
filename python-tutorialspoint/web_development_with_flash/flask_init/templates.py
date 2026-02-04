from flask import Flask, request, render_template
import os

app = Flask(__name__)   # create an instance of the Flask class. The parameter __name__ that is given will make the application unique. 

# methodology MVC - Model View Controller - MVC separates data base operations from presentation layer from the logic or controllers. 


@app.route('/hello')

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5002)) 
    app.debug = True        # debug not in the production server.    
    app.run(host=host, port=port)