from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', '__name__')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password1')
        password_conf = request.form.get('password2')

        if len(email) < 4:
            flash('Ungültige E-Mail Adresse.', category='error')
        elif len(firstName) < 2:
            flash('Name muss eingegeben werden.', category='error')
        elif len(password) < 8:
            flash('Ungültiges Passwort, min. 8 Zeichen.', category='error')
        elif password != password_conf:
            flash('Passwörter stimmen nicht überein.', category='error')
        else:
            # add User
            flash('Gratulation, du hast dich erfolgreich registiert.', category='success')



    return render_template('sign_up.html')
