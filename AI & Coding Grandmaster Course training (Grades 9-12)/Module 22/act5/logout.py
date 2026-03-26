@app.route('/logout')
def logout():
    name = ''
    id = ''
    msg = 'Logged out succesfully'
    return render_template('login.html',msg=msg, name=name, id=id)