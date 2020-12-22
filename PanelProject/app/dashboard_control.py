from . import *

@app.route('/', defaults={'user_type':'Admin'})
@app.route('/<user_type>')
def login(user_type):
    return render_template('login.html' , user_type = user_type)

@app.route('/dashboard')
def dashboard():
    if "login_id" in session:
        return render_template('dashboard.html')
    else:
        return redirect("/bad_request")

@app.route("/bad_request")
def bad_request():
    return render_template("bad_request.html")

