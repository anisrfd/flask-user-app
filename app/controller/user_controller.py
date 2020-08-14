from flask import render_template, request, redirect, flash
from app import app, db
from app.model.user_model import User
from app.model.sub_user_model import subUser

error_msg= "Page Not Found"

@app.route('/')
@app.route('/index')
def index():

    entries = User.query.all()
    sub_entries=subUser.query.all()
    return render_template('index.html', entries=entries,sub_entries=sub_entries,entry=None)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':

        form = request.form
        id = request.form.get('id')
        f_name = form.get('fname')
        l_name = form.get('lname')
        street = form.get('street')
        city = form.get('city')
        state = form.get('state')
        zip = form.get('zip')

        if (id is not None):
            id = id
            User.query.filter_by(id=id).update(
                dict(f_name=f_name,l_name=l_name,street=street, city=city, state=state,zip=zip))
            db.session.commit()
            flash('Successfully Updated User Info')
            return redirect('/')
        else:
            entry = User(f_name=f_name,l_name=l_name,street=street, city=city, state=state,zip=zip)
            db.session.add(entry)
            db.session.commit()
            flash('Successfully Added User')
            return redirect('/')

    return error_msg

@app.route('/update/<int:id>')
def updateRoute(id):
    entries = User.query.all()
    if not id or id != 0:
        entry = User.query.get_or_404(id)
        if entry:
            return render_template('index.html', entry=entry, entries=entries, title="User Edit")

    return error_msg

@app.route('/update', methods=['POST'])
def update():
    if not id or id != 0:
        entry = User.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return error_msg


@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = User.query.get_or_404(id)
        sub_entries = subUser.query.filter_by(parent_id=id).all()

        if entry:
            if sub_entries:
                for sub_id in sub_entries:
                    db.session.delete(sub_id)

            db.session.delete(entry)
            db.session.commit()

        return redirect('/')

    return error_msg



@app.route('/sub_user/<int:id>')
def sub_User_index(id):
    # entries = User.query.all()
    parent_id=id
    return render_template('user/sub_user_form.html', parent_id=parent_id, entry=None)


@app.route('/sub_user_add', methods=['POST'])
def sub_user_add():
    if request.method == 'POST':
        form = request.form
        parent_id = request.form.get('parentId')
        id = request.form.get('id')
        f_name = form.get('fname')
        l_name = form.get('lname')

        if (id is not None):
            id = id
            subUser.query.filter_by(id=id).update(
                dict(parent_id=parent_id,f_name=f_name,l_name=l_name))
            db.session.commit()
            flash('Successfully Updated User Info')
            return redirect('/')
        else:
            entry = subUser(parent_id=parent_id,f_name=f_name,l_name=l_name)
            db.session.add(entry)
            db.session.commit()
            flash('Successfully Added User')
            return redirect('/')

    return error_msg


@app.route('/sub_user_update/<int:parent_id>/<int:id>')
def sub_user_update(parent_id,id):
    if not id or id != 0:
        entry = subUser.query.get_or_404(id)
        print(id)
        if entry:
            return render_template('user/sub_user_form.html', parent_id=parent_id, entry=entry,title="Sub User Edit")

    return error_msg


@app.route('/sub_user_delete/<int:id>')
def sub_user_delete(id):
    if not id or id != 0:
        entry = subUser.query.get_or_404(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return error_msg

@app.errorhandler(Exception)
def error_page(e):
    return error_msg