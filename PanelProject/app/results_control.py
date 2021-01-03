from . import *
from .models import patients, panels

@app.route('/results_view', methods = ['GET', 'POST'])
def results_view():
    if "login_id" in session:

        if request.args.get("from_to_date_input") != None:
            date = request.args.get("from_to_date_input").split(" - ")
            print(date)
            patients_panels_refid = db.session.query(patients.Patients, panels.Panels,
                                                     patients.Patient_panels.id).filter(
                patients.Patient_panels.panel_id == panels.Panels.id,
                patients.Patient_panels.patient_id == patients.Patients.id).filter(
                patients.Patients.date <= date[1]).filter(patients.Patients.date >= date[0]).order_by(patients.Patients.id).all()

            print(db.session.query(patients.Patients, panels.Panels,
                                                     patients.Patient_panels.id).filter(
                patients.Patient_panels.panel_id == panels.Panels.id,
                patients.Patient_panels.patient_id == patients.Patients.id).filter(
                patients.Patients.date <= date[1]).filter(patients.Patients.date >= date[0]).order_by(patients.Patients.id))
        else:
            patients_panels_refid = db.session.query(patients.Patients, panels.Panels, patients.Patient_panels.id).filter(
                patients.Patient_panels.panel_id == panels.Panels.id,
                patients.Patient_panels.patient_id == patients.Patients.id).order_by(patients.Patients.id).all()
        return render_template('results_view.html', patients_panels_refid= patients_panels_refid)
    else:
        return redirect("/bad_request")