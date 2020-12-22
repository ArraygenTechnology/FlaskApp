from . import *
from .Models import sys_users

@app.route('/sys_users_add_update', methods = ['GET', 'POST'])
def sys_users_add_update():
    if request.method == 'POST':
        f_name= request.form['f_name']
        l_name= request.form['l_name']
        gender=request.form['gender']
        dob=request.form['dob']
        email = request.form['email']
        contact_no=request.form['contact_no']
        password=request.form['password']
        address=request.form['address']
        role=request.form['role']
        exists = sys_users.Users.query.filter_by(email=email).first()
        #print(exists)
        if exists == None:
            user = sys_users.Users(f_name, l_name, gender, dob, email, contact_no, password, address, role)
            db.session.add(user)
            db.session.commit()
            flash("User Added Successfully".title(),"info")
        else:
            flash("User Already Exists".title(), "error")
    return redirect('/sys_users')

@app.route("/sys_user_login", methods = ['POST'])
def sys_user_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = sys_users.Users.query.filter(sys_users.Users.email == email).first()
        if user != None:
            user = sys_users.Users.query.filter(sys_users.Users.email == email, sys_users.Users.password == password).first()
            if user != None:
                session['login_id'] = user.email
                session['role'] = user.role
                flash("Logged in Successfully".title(), "info")
                return redirect("/dashboard")
            else:
                flash("Email Or Password Is Wrong".title(), "error")
        else:
            flash("Email Is Not Registered".title(), "error")
    else:
        flash("Bad Request 404".title(),"error")
    return redirect("/")

@app.route("/sys_user_logout")
def sys_user_logout():
    session.pop('login_id',None)
    session.pop('role',None)
    flash("Logged out successfully".title(), "info")
    return redirect("/")