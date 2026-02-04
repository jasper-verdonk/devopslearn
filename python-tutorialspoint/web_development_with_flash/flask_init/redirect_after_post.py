from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)   # create an instance of the Flask class. The parameter __name__ that is given will make the application unique. 

# after successfull login reload the page now. Compare with the login_function.py

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = False    
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return redirect(url_for('welcome', username=request.form.get('username')))
        else:
            error = 'Incorrect username and password'
    return render_template('login.html', error=error)
    
def valid_login(username, password):
    if username == password:
        return True
    else:
        return False
    
@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5001)) 
    app.debug = True        # debug not in the production server.    
    app.run(host=host, port=port)