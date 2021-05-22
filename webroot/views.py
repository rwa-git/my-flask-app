import json

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User
from . import db

views = Blueprint('views', '__name__')


@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) <2:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added.', category='success')

    return render_template('home.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteID']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted!', category='success')

    return jsonify({})


@views.route('/service', methods=['GET','POST'])
@login_required
def service():

    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')

        if email != current_user.email:
            user = User.query.filter_by(email=email).first()
            if user:
                flash('E-Mail Adresse existiert bereits.', category='error')
            elif len(email) < 4:
                flash('Ungültige E-Mail Adresse.', category='error')
            else:
                flash('Daten wurden gespeichert.', category='success')

    return render_template('service.html', user=current_user)