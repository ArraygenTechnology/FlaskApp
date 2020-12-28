from . import *

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