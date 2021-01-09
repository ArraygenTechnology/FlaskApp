from . import *
from .models import patients, panels

@app.route('/analysis_view')
def analysis_view():
    if "login_id" in session:
        technician_status = "Rejected"
        patients_panels_refid_rejected = db.session.query(patients.Patients, panels.Panels, patients.Patient_panels).filter(patients.Patient_panels.panel_id == panels.Panels.id,
            patients.Patient_panels.patient_id == patients.Patients.id,
            patients.Patient_panels.technician_status == technician_status).order_by(patients.Patients.id).all()
        #print(patients_panels_refid_rejected)
        patients_panels_refid_not_rejected = db.session.query(patients.Patients, panels.Panels, patients.Patient_panels).filter(
            patients.Patient_panels.panel_id == panels.Panels.id,
            patients.Patient_panels.patient_id == patients.Patients.id,
            ( (patients.Patient_panels.technician_status  == None) | (patients.Patient_panels.technician_status != technician_status))
        ).order_by(patients.Patients.id).all()

        return render_template('analysis.html',
                               patients_panels_refid_not_rejected = patients_panels_refid_not_rejected,
                               patients_panels_refid_rejected = patients_panels_refid_rejected)
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

@csrf.exempt
@app.route('/submitReport', methods=['POST'])
def submitReport():
    if "login_id" in session:
        all_data = request.form
        id = all_data.get('id')
        patient_id = all_data.get('patient_id')
        panel_id = all_data.get('panel_id')
        report_type = all_data.get('report_type')
        file_name = ""
        if report_type == "Blood":
            file_name = os.path.join("analysis_data",id+"_blood_results.csv")
        elif report_type == "Allergy":
            file_name = os.path.join("analysis_data",id+"_allergy_results.csv")

        if file_name != "":
            fw = open(os.path.join(app.config['UPLOAD_FOLDER'],file_name), "w")
            for k, v in all_data.items():
                if k != "csrf_token" and k != "id" and k != "patient_id" and k != 'panel_id' and k != 'report_type':
                    print(k+"\t"+v, file= fw)
            fw.close()
            update_patient_panels = patients.Patient_panels.query.get((id, patient_id, panel_id))

            if report_type == "Blood":
                setattr(update_patient_panels, 'blood_results',file_name)
            elif report_type == "Allergy":
                setattr(update_patient_panels, 'allergy_results', file_name)
            setattr(update_patient_panels, 'submitted_date', datetime.datetime.now())
            db.session.commit()
        return redirect("/analysis_view")
    else:
        return redirect("/bad_request")

# For Ajax
@csrf.exempt
@app.route('/getReportFields', methods=['POST'])
def getReportFields():
    if "login_id" in session:
        get_patient_panels = patients.Patient_panels.query.get((request.form['id'], request.form['patient_id'], request.form['panel_id']))
        patient_panel_schema = patients.Patient_panelsSchema()
        op = patient_panel_schema.dumps(get_patient_panels)
        d = json.loads(op)
        with open(os.path.join(app.config['UPLOAD_FOLDER'],"report_form_fields/"+request.form['report_type']+".txt")) as json_file:
            data = json.load(json_file)
            d['formData'] = data['formData']
        #print(type(d), json.dumps(d))
        return json.dumps(d)
    else:
        return redirect("/bad_request")