from flask import Flask, session, redirect, url_for, request, render_template
from user import User

app = Flask(__name__, static_folder='static', template_folder='static/templates') 
app.secret_key = 'secret key' 

app.permanent_session_lifetime = timedelta(minutes=60)  # Set session timeout 

@app.route('/', methods=['GET', 'POST']) 
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

if __name__ == '__main__': 
    app.run(debug=True) 