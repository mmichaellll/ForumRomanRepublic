from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__, static_folder='static', template_folder='static/templates') 
app.secret_key = 'secret key' 

app.permanent_session_lifetime = timedelta(minutes=60)  # Set session timeout 

@app.route('/', methods=['GET', 'POST']) 
def index(): 
    return render_template('home.html')

if __name__ == '__main__': 
    app.run(debug=True) 