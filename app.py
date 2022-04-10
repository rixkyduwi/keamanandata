from flask import Flask, flash, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect
from form import RegistrationForm

app=Flask(__name__)
csrf=CSRFProtect()
app.config['SECRET_KEY']="blabla"
SERVER_NAME = '127.0.0.1:5000'
app.config['SERVER_NAME']=SERVER_NAME
app.config.update(
    DEBUG=True,
    SECRET_KEY="secret_sauce",
)
csrf.init_app(app)

@app.route("/")
def index():
    form = RegistrationForm()
    return render_template('home.html', form=form)
@app.route("/post",methods=['POST'])
def post():
    print('------ {0}'.format(request.form))
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('data dengan aman telah terkirim')
        return redirect(url_for('index'))
    return render_template('home.html', form=form)
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8000)