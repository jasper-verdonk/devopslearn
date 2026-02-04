from flask import Flask, request, render_template, redirect, url_for, flash, make_response
import os

app = Flask(__name__)   # create an instance of the Flask class. The parameter __name__ that is given will make the application unique. 

# stores the flash message into a session cookie 
# after succesfull page, reload the page. 

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = False    
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Succesfully logged in")
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('username', request.form.get('username'))
            return response
        else:
            error = 'Incorrect username and password'
    return render_template('login_2.html', error=error)
    
def valid_login(username, password):
    if username == password:
        return True
    else:
        return False
    


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0)
    return response

@app.route('/')
def welcome():
    username = request.cookies.get('username')
    if username:
        return render_template('welcome_2.html', username=username)
    else:
        return redirect(url_for('login'))
    

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5001)) 
    app.debug = True        # debug not in the production server. 
    app.secret_key = 'SuperKeySecret'   
    app.run(host=host, port=port)