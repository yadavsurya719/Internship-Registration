from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

# Replace the following with your MySQL database connection details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:surya7993290146@localhost/data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model for internship registration
class internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email_id = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    mode_of_internship = db.Column(db.String(10), nullable=False)
    skills = db.Column(db.String(255), nullable=False)
    months = db.Column(db.Integer, nullable=False)
    domain = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(255), nullable=False)
    college_name = db.Column(db.String(255), nullable=False)
    job_role = db.Column(db.String(200))
    salary = db.Column(db.Integer)
    experience = db.Column(db.String(255))
    recipient_name = db.Column(db.String(255))
    recipients_title = db.Column(db.String(255))
    recipients_compy_name = db.Column(db.String(255))
    recipient_company_address = db.Column(db.String(300))
    recommended_person_name = db.Column(db.String(250))

# Route for internship registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':  
        full_name  = request.form['full_name']
        email_id = request.form['email_id']
        date_of_birth  = request.form['dob']
        phone_number = request.form['phone']
        mode_of_internship= request.form['internshipMode']
        skills =request.form['skills']
        months=request.form['Duration']
        domain=request.form['domain']
        department=request.form['department']
        college_name = request.form['college_name']

        # Create a new registration entry
        registration = internship(
            full_name= full_name,
            email_id= email_id,
            date_of_birth= date_of_birth,
            phone_number=phone_number,
            mode_of_internship= mode_of_internship,
            skills=skills,
           months= months,
           domain=domain,
           department= department,     
          college_name =college_name,
        )

        db.session.add(registration)
        db.session.commit()

        return redirect(url_for('registration_success'))

    return render_template('register.html')

# Route for displaying registration success
@app.route('/success')
def registration_success():
    return "Registration Successful!"




if __name__== '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
