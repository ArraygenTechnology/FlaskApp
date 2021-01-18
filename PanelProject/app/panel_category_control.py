from . import *
from .models import panels

@app.route('/panel_category_<id>', defaults={'category_id':0}, methods = ['GET', 'POST'])
@app.route('/panel_category_<id>_<category_id>')
def panel_category(id, category_id):
    if "login_id" in session:
        panel_info = panels.Panels.query.get(id)
        categories = panels.Category.query.filter(panels.Category.panel_id ==id)
        if category_id == 0:
            return render_template('panel_category.html', panel_info=panel_info, categories=categories)
        else:
            category = panels.Category.query.get(category_id)
            return render_template('panel_category.html', panel_info = panel_info, categories = categories, category= category)
    else:
        return redirect("/bad_request")

# Add or Update Users
@csrf.exempt
@app.route('/category_add_update', defaults={'id':0}, methods = ['GET', 'POST'])
@app.route('/category_add_update_<int:id>', methods = ['GET', 'POST'])
def category_add_update(id):
    if request.method == 'POST':
        data = request.form

        all_data = data.to_dict()
        del all_data['csrf_token']
        # update patient information
        if id != 0:
            category = panels.Category.query.get(id)
            print(category)
            for attr_name, new_value in all_data.items():
                setattr(category, attr_name, new_value)

            db.session.commit()
            flash("Category Updated Successfully".title(), "info")
        else:
        # add new category details
            # creating object
            category = panels.Category(**all_data)
            db.session.add(category)
            db.session.commit()
            flash("Category Added Successfully".title(), "info")

    return redirect('/panel_category_'+all_data['panel_id'])

@app.route('/category_delete_<panel_id>/<id>')
def category_delete(panel_id, id):
    if "login_id" in session:
        category = panels.Category.query.get(id)
        if category != None:
            db.session.delete(category)
            db.session.commit()
            flash("Category Deleted Successfully".title(), "info")
        return redirect('/panel_category_'+str(panel_id))
    else:
        return redirect("/bad_request")

@app.route('/view_traits')
def view_traits():
    if "login_id" in session:
        traits = panels.Traits.query.all()
        return render_template('view_traits.html', traits = traits)
    else:
        return redirect("/bad_request")


# Add or Update Users
@csrf.exempt
@app.route('/trait_add_update', defaults={'id':0}, methods = ['GET', 'POST'])
@app.route('/trait_add_update_<int:id>', methods = ['GET', 'POST'])
def trait_add_update(id):
    if request.method == 'POST':
        data = request.form
        all_data = data.to_dict()

        file = request.files['icon_img']
        last_index = len(file.filename) - 1 - file.filename[::-1].index('.')
        filename = os.path.join("trait_images", secure_filename(all_data['name'].replace("_","") + file.filename[last_index:]))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        all_data['icon_img'] = filename

        del all_data['csrf_token']
        del all_data['panel_id']
        # update patient information
        if id != 0:
            category = panels.Category.query.get(id)
            print(category)
            for attr_name, new_value in all_data.items():
                setattr(category, attr_name, new_value)

            db.session.commit()
            flash("Category Updated Successfully".title(), "info")
        else:
            # add new category details
            # creating object
            traits = panels.Traits(**all_data)
            db.session.add(traits)
            db.session.commit()
            flash("Trait Added Successfully".title(), "info")

    return redirect('/panel_category_'+data['panel_id'])
