from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint('auth', '__name__')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        passwd = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, passwd):
                flash(f'Sali {user.first_name}, du bist angemeldet.', category='succsess')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
        else:
            flash('Sorry, aber die stimmt was nicht.', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    # return render_template('logout.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password1')
        password_conf = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('E-Mail Adresse existiert bereits.', category='error')
        elif len(email) < 4:
            flash('Ungültige E-Mail Adresse.', category='error')
        elif len(firstName) < 2:
            flash('Name muss eingegeben werden.', category='error')
        elif len(password) < 8:
            flash('Ungültiges Passwort, min. 8 Zeichen.', category='error')
        elif password != password_conf:
            flash('Passwörter stimmen nicht überein.', category='error')
        else:
            # add User
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(
                password=password, method='sha256'
            ))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Gratulation, du hast dich erfolgreich registiert.', category='success')
            return redirect(url_for('views.home'))



    return render_template('sign_up.html', user=current_user)

