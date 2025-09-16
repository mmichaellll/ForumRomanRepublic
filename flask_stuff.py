from flask import Flask, session, redirect, url_for, request, render_template
from functools import wraps
from datetime import timedelta
from user import User

app = Flask(__name__, static_folder='static', template_folder='static/templates') 
app.secret_key = 'secret key' 

app.permanent_session_lifetime = timedelta(minutes=60)  # Set session timeout 




def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") == None:
            return redirect("/register")
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET', 'POST']) 
@login_required
def index(): 
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email'].lower()
        pwd = request.form['password']
        fname = request.form['firstname']
        lname = request.form['lastname']
        year, month, day = request.form['birthday'].split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        session['user'] = User(email, pwd, fname, lname, year, month, day)
        return redirect('/')
    return render_template('register.html')

@app.route('/forum/<id>', methods=['GET', 'POST'])
@login_required
def forum(id):
    return render_template('forum.html', id, title, threads)

@app.route('/thread/<id>', methods=['GET', 'POST'])
@login_required
def thread(id):
    return render_template('thread.html', id, title, posts)

if __name__ == '__main__': 
    app.run(debug=True) 