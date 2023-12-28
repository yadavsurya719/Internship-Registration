from xhtml2pdf import pisa
import mysql.connector
import pymysql

mydb = mysql.connector.connect(host='localhost', user='root', password='surya7993290146', database='data')
mycursor = mydb.cursor()
print("Database is connected")


def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
        
    return not pisa_status.err
def certificate(user_id,full_name, job_role, start_date, salary):

    # HTML content
    html_content = '''
    <html>
        <head>
            <style type='text/css'>
                body, html {
                    margin: 0;
                    padding: 0;
                }
                body {
                    color: black;
                    display: table;
                    font-family: Georgia, serif;
                    font-size: 24px;
                    text-align: center;
                }
                .container {
                    border: 20px solid tan;
                    width: 750px;
                    height: 563px;
                    display: table-cell;
                    vertical-align: middle;
                }
                .logo {
                    color: tan;
                }

                .marquee {
                    color: tan;
                    font-size: 48px;
                    margin: 20px;
                }
                .assignment {
                    margin: 20px;
                }
                .person {
                    border-bottom: 2px solid black;
                    font-size: 32px;
                    font-style: italic;
                    margin: 20px auto;
                    width: 400px;
                }
                .reason {
                    margin: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">
                    An Organization
                </div>

                <div class="marquee">
                    Certificate of Completion
                </div>

                <div class="assignment">
                    This certificate is presented to
                </div>

                <div class="person">
                    name
                </div>

                <div class="reason">
                    For deftly defying the laws of gravity<br/>
                    and flying high
                </div>
            </div>
        </body>
    </html>
    '''

    x = html_content.replace("name", full_name)
    # Generate PDF
    pdf_path = f"certificate_{full_name}.pdf"
    if convert_html_to_pdf(x, pdf_path):
        print(f"PDF generated and saved at {pdf_path}")
    else:
        print("PDF generation failed")

mycursor.execute("SELECT * FROM data.internship")
results = mycursor.fetchall()

for result in results:
    certificate(str(result[0]), result[1], result[2], result[3], result[4])
     

mydb.close()