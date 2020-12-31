from . import *

@app.route('/analysis_view')
def analysis_view():
    if "login_id" in session:
        #users = sys_users.Users.query.all()
        users=''
        return render_template('analysis.html', Users= users)
    else:
        return redirect("/bad_request")