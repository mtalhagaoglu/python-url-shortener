from flask import Flask, render_template, flash, request,redirect,url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import string
import random
import shortener

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class AddingForm(Form):
    link = TextField('Link:', validators=[validators.required()])
    password = TextField('Password:', validators=[validators.required()])

class DeletingForm(Form):
    shorten = TextField('Shorten:', validators=[validators.required()])
    password = TextField('Password:', validators=[validators.required()])


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def addLink(link, shorten):
    print(link)
    print(shorten)
    shortener.addLink(link,shorten)

def removeLink(shorten):
    print(shorten)
    shortener.removeLink(shorten)

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddingForm(request.form)
    if request.method == 'POST':
        link=request.form['link']
        shorten=request.form['shorten']
        password=request.form['password']

        if form.validate():
            if(password == "123"):
                if (shorten == ""):
                    shorten = id_generator()
                addLink(link, shorten)
                flash('Link created: domain.com/{}'.format(shorten))
            else:
                flash("Error: Password is wrong")
        else:
            flash('Error: All Fields are Required')

    return render_template('add.html', form=form)

@app.route("/remove", methods=['GET', 'POST'])
def remove():
    form = DeletingForm(request.form)
    if request.method == 'POST':
        shorten=request.form['shorten']
        password=request.form['password']

        if form.validate():
            if(password == "123"):
                removeLink(shorten)
                flash('Link removed: domain.com/{}'.format(shorten))
            else:
                flash("Error: Password is wrong")
        else:
            flash('Error: All Fields are Required')

    return render_template('remove.html', form=form)

@app.route('/<hash>/')
def redirect_url(hash):
    url = shortener.getLink(hash)
    if(url):
        print(True)
        return redirect(url)
    else:
        print(False)
        flash("Error: Shortened url does not exist.")
        return redirect(url_for('add'))

@app.route("/<hash>/stat")
def stat(hash):
    count = shortener.getCount(hash)
    return render_template("stat.html",data=count)

if __name__ == "__main__":
    app.run()