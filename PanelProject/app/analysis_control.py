from . import *
from .models import patients, panels

@app.route('/analysis_view')
def analysis_view():
    if "login_id" in session:
        patients_panels_refid = db.session.query(patients.Patients, panels.Panels, patients.Patient_panels).filter(patients.Patient_panels.panel_id == panels.Panels.id,
            patients.Patient_panels.patient_id == patients.Patients.id).order_by(patients.Patients.id).all()
        return render_template('analysis.html', patients_panels_refid= patients_panels_refid )
    else:
        return redirect("/bad_request")

@csrf.exempt
@app.route('/submit_analysis_data', methods = ['POST'])
def submit_analysis_data():
    if "login_id" in session:
        if request.form.get("analysis_result",None) != None:
            ref_id = request.form['ref_id']
            update_patient_panels = patients.Patient_panels.query.get((int(ref_id), request.form['patient_id'], request.form['panel_id']))# patients.Patient_panels.query.get(int(ref_id))
            files_dict = {'dna_results': request.files['dna_result'] , 'blood_results':request.files['blood_result'], 'allergy_results':request.files['allergy_result']}
            for name, file in files_dict.items():
                if file and allowed_file(file.filename):
                    last_index = len(file.filename) - 1 - file.filename[::-1].index('.')
                    filename = os.path.join("analysis_data", secure_filename(ref_id+"_"+name+file.filename[last_index:]))
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                    setattr(update_patient_panels, name , filename)
            setattr(update_patient_panels, 'submitted_date' , datetime.datetime.now())
            setattr(update_patient_panels, 'first_result', 'bad_request.html')
            setattr(update_patient_panels, 'result_status', 'Done')
            db.session.commit()
            flash("Files Uploaded Successfully", "info")
        return redirect("/analysis_view")
    else:
        return redirect("/bad_request")

@app.route('/download_analysis_data/<path:filename>')
def download_analysis_data(filename):
    #return redirect("/analysis_view")
    return send_from_directory(directory=os.path.join("/".join(app.root_path.split("/")[:-1]), app.config['UPLOAD_FOLDER'], "/".join(filename.split("/")[:-1])), filename=filename.split("/")[-1])

@app.route('/delete_analysis_data_file/<int:id>-<int:patient_id>-<int:panel_id>-<name>')
def delete_analysis_data_file(id, patient_id, panel_id, name):
    update_patient_panels = patients.Patient_panels.query.get((id, patient_id, panel_id))
    os.remove(os.path.join("/".join(app.root_path.split("/")[:-1]), app.config['UPLOAD_FOLDER'], getattr(update_patient_panels,name)))
    setattr(update_patient_panels , name, None)
    db.session.commit()
    return redirect("/analysis_view")

# For Ajax
@csrf.exempt
@app.route('/getReportFields', methods=['POST'])
def getReportFields():
    if "login_id" in session:
        get_patient_panels = patients.Patient_panels.query.get((request.form['id'], request.form['patient_id'], request.form['panel_id']))
        patient_panel_schema = patients.Patient_panelsSchema()
        op = patient_panel_schema.dumps(get_patient_panels)
        f = open(os.path.join(app.config['UPLOAD_FOLDER'],"r"
                                                          "eport_form_fields/Blood.txt"))
        data = f.read()
        d = json.loads(op)
        print(type(d))
        print(data)
        f.close()
        return jsonify(op) #, jsonify(data)
    else:
        return redirect("/bad_request")