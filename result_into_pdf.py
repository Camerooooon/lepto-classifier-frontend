import pandas as pd
from fpdf import FPDF
from result import Result

def gen_pdf(data, result: Result):
    s = ""
    #this will convert json into txt, thus we use txt file to convert it into pdf format
    df = pd.read_json ('result.json')
    df.to_csv ('result.txt', index = False)

    df = pd.read_json ('user.json')
    df.to_csv ('user_data.txt', index = False)
    pdf = FPDF('P', 'mm', (100, 150))

    # variable pdf
    pdf = FPDF(format='letter')

    # Add a page
    pdf.add_page()

    pdf.set_font("Times", 'B', size = 15)
    #this will make print the color in red 
    pdf.set_text_color(0, 40, 85) 
    pdf.cell(50, 10, txt = "Lepto-Classifier", ln = 1, align = 'C')
    pdf.set_font("Times", 'B', size = 12)
    pdf.cell(100, 10, txt = "This is the entered information:", ln = 1, align = 'C')

    #open reult txt
    f = open("result.txt", "r")
    #open user data txt
    p = open("user_data.txt", "r")

    z = open("info.txt", "r")
    user = ""
    patient = ""

    pdf.set_font("Times", 'BI', size = 10)
    #user data 
    for x in z: 
        pdf.cell(200, 5, txt = x, border = 0, ln = 1, align='C')
    # print users name 
        if (x.split(':',1)[0] == 'Client'):
            user +=  x 
        if (x.split(':',1)[1] == 'Patient Number'):
            patient +=  x 
            print(patient)

    pdf.set_font("Times", 'B', size = 12)
    pdf.cell(103, 10, txt = "User: " + user, ln = 1, align = 'C')
    pdf.cell(135, 2, txt = "This is the patient #: " + patient, ln = 1, align = 'C')

    pdf.set_font("Times", 'B', size = 10)
    for x in f: 
        #pdf.cell(200, 10, txt = x, ln = 1, align='C')
        s += x
    pdf.set_font("Times", 'B', size = 12)
    pdf.cell(200, 10, txt = "result: " + x, ln = 1, align='C')
    print(s)
    print(s[0:1])
    # add another cell
    pdf.cell(200, 0, txt = "Your result is: " + s[7:15], ln = 2, align = 'C')

    # the user emails 
    #pdf.cell(200, 0, txt = "This is the user email + " , ln = 2, align = 'C')
    pdf.set_font("Times", size = 12)

    # fix this into one string 
    pdf.cell(200, 10, txt = "If you have any question or would like to make an inquery please visit our website: ", ln = 2, align = 'C')
    pdf.cell(200, 10, txt = "this will be the link to the webpage....", ln = 2, align = 'C')

    pdf.set_text_color(0, 40, 85) 
    pdf.cell(200, 10, txt = "To reference visit this website", ln = 2, align = 'C')
    pdf.cell(200, 0, txt = "https://journals.sagepub.com/doi/full/10.1177/10406387221096781", link="https://journals.sagepub.com/doi/full/10.1177/10406387221096781", align = 'C')

    pdf.set_text_color(179, 163, 105) 
    pdf.cell(200, 5, txt = "(Copyright © 2022 UC DAVIS VETERINARY MEDICINE. All rights resereved)", ln = 2, align = 'C')

    # save the pdf with name .pdf
    print("Process completed")

    pdf.image('vm2.png', 110, 250, 100, link="https://journals.sagepub.com/doi/full/10.1177/10406387221096781")

    #pdf.output("result.pdf") 

    return pdf.output(dest = "S").encode('latin-1')
