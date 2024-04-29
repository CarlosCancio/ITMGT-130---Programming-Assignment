@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("user",None)
    session.pop("cart",None)
    return redirect('/')