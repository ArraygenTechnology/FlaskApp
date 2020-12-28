from . import *
from .models import sys_users

@app.route('/patient/', defaults={'id': 0})
@app.route('/patient/<id>')
def patient(id):
    if "login_id" in session:
        if id == 0:
            return render_template('patients.html')
        else:
            #exists = sys_users.Users.query.get(id)
            #if exists == None:
                return redirect("/bad_request")
            #else:
            #    return render_template('patients.html', user = exists)
    else:
        return redirect("/bad_request")

# Add or Update Users
@app.route('/patients_add_update', defaults={'id':0}, methods = ['GET', 'POST'])
@app.route('/patients_add_update/<int:id>', methods = ['GET', 'POST'])
def patients_add_update(id):
    if request.method == 'POST':
        flash("Testing".title(), "error")
    return redirect('/patients_view')


@app.route('/patients_view')
def patients_view():
    if "login_id" in session:
        users = sys_users.Users.query.all()
        return render_template('patients_view.html', Users= users)
    else:
        return redirect("/bad_request")
