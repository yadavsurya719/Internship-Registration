from flask import Flask
app = Flask(__name__)
# Route for displaying registration success
@app.route('/')
def registration_success():
    return "Registration Successful!"




if __name__== '__main__':
    app.run(debug=True)