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

@csrf.exempt
@app.route('/updatePatientPhisicianDetails', methods=['POST'])
def updatePatientPhisicianDetails():
    if "login_id" in session:
        update_patient_panels = patients.Patient_panels.query.get((request.form['id'], request.form['patient_id'], request.form['panel_id']))
        setattr(update_patient_panels , "physician_status" , request.form['physician_status'])
        setattr(update_patient_panels, "physician_note", request.form['physician_note'])
        setattr(update_patient_panels, "include_note", request.form['include_note'])
        setattr(update_patient_panels , "physician_status_date" , datetime.datetime.now())
        db.session.commit()
        flash("Details Updated Successfully")
        return redirect("/results_view")
    else:
        return redirect("/bad_request")