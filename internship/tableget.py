from flask import Flask, render_template, request, redirect, url_for,jsonify
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
    offer_letter = db.Column(db.String(255))
    letter_of_recommendation = db.Column(db.String(300))
    certificate= db.Column(db.String(250))


# Route for internship registration form
@app.route('/getall', methods=['GET'])
def getall():
   
    data = internship.query.with_entities(internship.id, internship.full_name, internship.email_id ,internship.phone_number,internship.mode_of_internship, internship.months ,internship.college_name, internship.offer_letter,internship.letter_of_recommendation,internship.certificate).all()

    # Convert the data to a dictionary or a list of dictionaries
    #data_dict_list = [{'id': item.id, 'full_name': item.full_name,'email_id': item.email_id,} for item in data]


    # Convert the data to a list of dictionaries
    data_dict_list = [{'id': item.id, 'full_name': item.full_name, 'email_id': item.email_id,'phone_number': item.phone_number,'mode_of_internship': item.mode_of_internship,'months': item.months,'college_name': item.college_name,'offer_letter': item.offer_letter,'Letter_of_recommendation': item.letter_of_recommendation,'Certificate': item.certificate} for item in data]

    return render_template('table.html', data=data_dict_list)
    
    #return render_template('table.html', data=data)





if __name__== '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
