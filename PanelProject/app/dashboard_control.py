from . import *
from .models import patients, panels, sys_users

@app.route('/', defaults={'user_type':'Admin'})
@app.route('/<user_type>')
def login(user_type):
    if "login_id" in session:
        return redirect("/dashboard")
    else:
        return render_template('login.html' , user_type = user_type)

@app.route('/dashboard')
def dashboard():
    if "login_id" in session:
        sys_users_cnt = db.session.query(sys_users.Users).count()
        patients_cnt = db.session.query(sys_users.Users).count()
        return render_template('dashboard.html', sys_users_cnt=sys_users_cnt, patients_cnt= patients_cnt)
    else:
        return redirect("/bad_request")

@app.route("/bad_request")
def bad_request():
    if "login_id" in session:
        return render_template("bad_request_internal.html", img=("dist/img/HTTP-Error-404.png", "dist/img/HTTP-Error-404-mobile.png"))
    else:
        return render_template("bad_request.html", img=("dist/img/HTTP-Error-404.png", "dist/img/HTTP-Error-404-mobile.png"))


