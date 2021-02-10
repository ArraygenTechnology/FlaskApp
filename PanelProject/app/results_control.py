from . import *
from .models import patients, panels, sys_users
from .analysis_control import pdf_genration_genetics
@app.route('/results_view', methods = ['GET', 'POST'])
def results_view():
    if "login_id" in session and (session.get("role") == "Admin" or session.get("role") == "Physician"):
        from_to_date_input = ""
        technician_status = "Approved"
        if request.args.get("from_to_date_input") != None:
            from_to_date_input = request.args.get("from_to_date_input")
            date = request.args.get("from_to_date_input").split(" - ")
            patients_panels_refid = db.session.query(patients.Patients, panels.Panels,
                                                     patients.Patient_panels).filter(
                patients.Patient_panels.panel_id == panels.Panels.id,
                patients.Patient_panels.patient_id == patients.Patients.id ,
                patients.Patient_panels.technician_status == technician_status ).filter(
                patients.Patients.date <= date[1]).filter(patients.Patients.date >= date[0]).order_by(patients.Patients.id).all()
            get_method = True
        else:
            patients_panels_refid = db.session.query(patients.Patients, panels.Panels, patients.Patient_panels).filter(
                patients.Patient_panels.panel_id == panels.Panels.id,
                patients.Patient_panels.patient_id == patients.Patients.id,
                patients.Patient_panels.technician_status == technician_status).order_by(patients.Patients.id).all()
            get_method = False
        return render_template('results_view.html', patients_panels_refid= patients_panels_refid, get_method = get_method , from_to_date_input = from_to_date_input )
    else:
        return redirect("/bad_request")

@csrf.exempt
@app.route('/updatePatientPhisicianDetails', methods=['POST'])
def updatePatientPhisicianDetails():
    if "login_id" in session and (session.get("role") == "Admin" or session.get("role") == "Physician"):
        #print(request.form.get('id'), request.form.get('patient_id'), request.form.get('panel_id'))
        update_patient_panels = patients.Patient_panels.query.get((request.form.get('id'), request.form.get('patient_id'), request.form.get('panel_id')))
        #print(update_patient_panels)
        setattr(update_patient_panels , "physician_status" , request.form.get('physician_status'))
        setattr(update_patient_panels, "physician_note", request.form.get('physician_note'))
        setattr(update_patient_panels, "include_note", request.form.get('include_note'))
        setattr(update_patient_panels , "physician_status_date" , datetime.datetime.now())
        db.session.commit()

        user = patients.Patients.query.get(request.form['patient_id'])
        user_algo = patients.Patient_panels.query.get(
            (request.form['id'], request.form['patient_id'], request.form['panel_id']))
        pdf_genration_genetics(user, user_algo ,"2_")
        setattr(user_algo, 'second_result', os.path.join("analysis_data", "2_"+user.f_name + user.l_name + ".pdf"))
        db.session.commit()

        flash("Details Updated Successfully")
        return redirect("/results_view")
    else:
        return redirect("/bad_request")

# for pdf
@app.route('/hello_pdf')
def hello_pdf():
    os_path = os.getcwd()
    user = patients.Patients.query.get(2)
    user_algo = patients.Patient_panels.query.get((1,2,1))
    categories = panels.Category.query.filter(panels.Category.panel_id == user_algo.panel_id).order_by(panels.Category.id.asc()).all()
    all_traits = [panels.Traits.query.filter(panels.Traits.category_id == category.id).all() for category in categories ]
    f = open(os.path.join(app.config['UPLOAD_FOLDER'], user_algo.dna_results))
    user_rs_id_dict = {}
    for line in f:
        splitted = line.strip().split("\t")
        user_rs_id_dict[splitted[0]] = splitted[-1]
    algorithm_info=[]
    for traits in all_traits:
        for trait in traits:
            algo_list = []
            algo = panels.TraitAlgorithmInfo.query.filter(panels.TraitAlgorithmInfo.trait_id==trait.id).all()
            for data in algo:
                if data.rs_id in user_rs_id_dict.keys():
                    user_genotype = user_rs_id_dict[data.rs_id]
                    if user_genotype == data.genotype:
                        algo_list.append(data)
            algorithm_info.append(algo_list)

    f = open(os.path.join(app.config['UPLOAD_FOLDER'], user_algo.blood_results))
    blood_dict = {}
    for line in f:
        splitted = line.strip().split("\t")
        blood_data = panels.BloodAlgorithmInfo.query.filter(panels.BloodAlgorithmInfo.trait_id == splitted[0]).all()
        blood_data = blood_data[0]
        if blood_data.typical_min.isnumeric() and blood_data.typical_max.isnumeric() and blood_data.slightly_enhanced_min.isnumeric() and blood_data.slightly_enhanced_max.isnumeric() and blood_data.enhanced_min.isnumeric() and blood_data.enhanced_max.isnumeric():
            blood_dict[int(splitted[0])] = (int(splitted[1]), (
            int(blood_data.typical_min), int(blood_data.typical_max), int(blood_data.slightly_enhanced_min),
            int(blood_data.slightly_enhanced_max), int(blood_data.enhanced_min), int(blood_data.enhanced_max)))
    f.close()
    #print(blood_dict)

    html= render_template('genetics_pdf.html', blood_data = blood_dict, os_path=os_path, categories= categories, all_traits=all_traits, algorithm_info = algorithm_info, user = user, patient_panel = user_algo)
    options = {
        'page-size': 'A4',
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    pdf = pdfkit.from_string(html,False , options=options)
    response = make_response(pdf)
    response.headers['Content-Type'] ="application/pdf"
    response.headers['Content-Disposition'] ="inline; filename=op.pdf"
    return response

