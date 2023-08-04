
@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True)