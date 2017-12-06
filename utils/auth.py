from flask import redirect, url_for, request, session, flash
import database, hashlib

# scrits for logging in


# Logs user in (from form)
def login():
    users = database.getUsers()
    # checks credentials for login
    if request.form.get('username') in users:
        hash_object = hashlib.sha224(request.form.get('password'))
        hashed_pass = hash_object.hexdigest()
        if hashed_pass == users[request.form.get('username')]:
            session['username'] = request.form.get('username')
            return redirect(url_for('profile'))
        else:
            flash("Your password is incorrect.")
            return redirect(url_for('authentication'))
    else:
        flash("Your username is incorrect.")
        return redirect(url_for('authentication'))

if __name__ == '__main__':
    pass
print database.getUsers()
