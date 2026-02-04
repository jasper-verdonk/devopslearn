from flask import Flask, url_for
import os

app = Flask(__name__)   # create an instance of the Flask class. The parameter __name__ that is given will make the application unique. 


@app.route('/')
def index():
    return url_for('show_user_profile', username='richard')

@app.route('/username/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return "User %s" % username 

@app.route('/hello')   # This is called the route. The access point of that function. 
def hello_world():    
    return "Hello World!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id must be an integer
    return "Post %d" % post_id

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5001)) 
    app.debug = True        # debug not in the production server.    
    app.run(host=host, port=port)