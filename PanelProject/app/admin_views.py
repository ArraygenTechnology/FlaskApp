from . import *

@app.route('/', defaults={'user_type':'Admin'})
@app.route('/<user_type>')
def login(user_type):
    return render_template('login.html' , user_type = user_type)

@app.route('/dashboard',methods = ['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/sys_users')
def sys_users():
    return render_template('sys_users.html')