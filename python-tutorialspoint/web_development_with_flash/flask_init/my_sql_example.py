from flask import Flask, request, render_template, redirect, url_for, flash, session
import os
import logging 
from logging.handlers import RotatingFileHandler
import pymysql

app = Flask(__name__)   # create an instance of the Flask class. The parameter __name__ that is given will make the application unique. 

# stores the flash message into a session cookie 
# after succesfull page, reload the page. 



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = False    
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Succesfully logged in")
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = 'Incorrect username and password'
            app.logger.warning("Incorrect username and password for user (%s)", 
            request.form.get('username'))
    return render_template('login_2.html', error=error)
    
def valid_login(username, password):
    MYSQL_DATABASE_HOST = os.getenv('IP', '127.0.0.1')
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'WPheOOma1cmPetsKgLxr'
    MYSQL_DATABASE_DB = 'my_flask_app'

    conn = pymysql.connect(
        host=MYSQL_DATABASE_HOST,
        user=MYSQL_DATABASE_USER,
        password=MYSQL_DATABASE_PASSWORD,
        database=MYSQL_DATABASE_DB
    )

    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM user WHERE username=%s AND password=%s",
        (username, password)
    )

    data = cursor.fetchone()
    return data is not None

    if data:
        return True
    else:
        return False
    


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome_2.html', username=session['username'])
    else:
        return redirect(url_for('login'))
    

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5002)) 
    app.debug = True        # debug not in the production server. 
    app.secret_key = 'P9n\xd0\x83\xe2\xa6=\xa2\xa9\xacG\x088\x9d\x82\x93\x83\xa2"\x01\xdb#\xb0'  
    
    #logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1) 
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    
    app.run(host=host, port=port)
    
# from python interpreter
# import os
# os.urandom(24)