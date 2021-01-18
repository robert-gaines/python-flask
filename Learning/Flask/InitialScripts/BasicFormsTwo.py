from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,DateTimeField,RadioField,SelectField,TextField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'THE_SECRET_KEY'

class InformationForm(FlaskForm):
    #
    role = StringField("What is the user's role?",validators=[DataRequired()])
    #
    isemployee = BooleanField("Is the user an employee?",validators=[DataRequired()])
    #
    site_role = RadioField("Please identify the user's role on the site",choices=[('administrator','administrator'),('standard user','standard user')])
    #
    account_status = SelectField(u'Account Active/Inactive?', choices=[('active','active'),('inactive','inactive')])
    #
    feedback = TextAreaField()
    #
    submit = SubmitField('Party!')


@app.route('/',methods=['GET','POST'])

def index():

    form = InformationForm()

    if(form.validate_on_submit()):
        session['role'] = form.role.data
        session['isemployee'] = form.isemployee.data
        session['site_role'] = form.site_role.data
        session['account_status'] = form.account_status.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('submission_confirmation'))

    return render_template('index.html',form=form)

@app.route('/submission_confirmation')

def submission_confirmation():
    return render_template('submission_confirmation.html')

if(__name__ == '__main__'):
    app.run(debug=True)
