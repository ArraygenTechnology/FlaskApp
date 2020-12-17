from . import db, app, redirect, request, flash
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
        #print(f_name, l_name, gender, dob, email, contact_no, password, address, role)
        exists = sys_users.Users.query.filter_by(email=email).first()
        print(exists)
        if exists == None:
            user = sys_users.Users(f_name, l_name, gender, dob, email, contact_no, password, address, role)
            db.session.add(user)
            db.session.commit()
            flash("User Added Successfully","info")
        else:
            flash("User Email Already exists", "error")
    return redirect('/sys_users')