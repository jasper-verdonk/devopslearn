from flask_blog import app, db
from flask import render_template, redirect, url_for, flash
from author.form import RegisterForm
from author.models import Author

@app.route('/login')
def login():
    return "Hello, User!"

@app.route("/debug-templates")
def debug_templates():
    from flask import current_app
    templates = current_app.jinja_env.list_templates()
    return "<br>".join(templates)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        # Create new Author object
        new_author = Author(
            fullname=form.fullname.data,
            email=form.email.data
        )
        
        # Add to DB and commit
        db.session.add(new_author)
        db.session.commit()
        
        flash("Author registered successfully!", "success")
        return redirect(url_for('register'))
    
    return render_template('author/register.html', form=form)