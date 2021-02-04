from . import *
from .models import patients, panels

@app.route('/user_index')
def user_index():
    if "login_id" in session:
        user = patients.Patients.query.get(session['login_id'])
        return render_template('patient_user/index.html', user= user)
    else:
        return redirect("/bad_request")

# Login
@csrf.exempt
@app.route("/user_login", methods = ['POST'])
def user_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = patients.Patients.query.filter(patients.Patients.email == email).first()
        if user != None:
            user = patients.Patients.query.filter(patients.Patients.email == email, patients.Patients.password == password).first()
            if user != None:

                session['login_id'] = user.id
                session['l_name'] = user.l_name
                session['f_name'] = user.f_name

                flash("Logged in Successfully".title(), "info")
                return redirect("/user_index")
            else:
                flash("Email Or Password Is Wrong".title(), "error")
        else:
            flash("Email Is Not Registered".title(), "error")
    else:
        flash("Bad Request 404".title(),"error")
    return redirect("/")

# Logout
@app.route("/user_logout")
def user_logout():
    session.pop('login_id',None)
    session.pop('f_name',None)
    session.pop('l_name',None)
    flash("Logged out successfully".title(), "info")
    return redirect("/")
