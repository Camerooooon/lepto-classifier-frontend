from fpdf import FPDF
from result import Result


#this is to test 
def gen_pdf(data, result: Result, temp_link: str):
    #this will convert json into txt, thus we use txt file to convert it into pdf format
    pdf = FPDF('P', 'mm', (100, 150))
    
    
    # variable pdf
    pdf = FPDF(format='letter')
    
    # Add a page
    pdf.add_page()
    pdf.set_font("Times", 'B', size = 15)
    #this will make print the color in red 
    pdf.set_text_color(0, 40, 85) 
    pdf.ln(.15)
    pdf.set_author("Dr.Reagan")
    pdf.cell(200, 0, txt = "Here is the result of the Leptospirosis Machine Learning Algorithym: ",ln = 1, align = 'L')
    
    pdf.set_font("Times", 'BI', size = 30)
    pdf.cell(200, 100, txt = "Result: " + Result.fmt(result), ln = 1, align='C')
    pdf.set_font("Times", size = 15)
    # add another cell
    
    # the user emails 
    #pdf.cell(200, 0, txt = "This is the user email + " , ln = 2, align = 'C')
    
    # emails 
    pdf.cell(200, 10, border = 1, txt = "If you have any question or would like to make an inquery please visit our website: ", ln = 2, align = 'C')
    pdf.cell(200, 10, border = 1, txt= "https://drkrystlereagan.com/", ln= 1, align = 'C')
    pdf.set_y(-40)
    pdf.cell(200, 10, border = 1, txt = "(Copyright © 2022 UC DAVIS VETERINARY MEDICINE. All rights resereved)", ln =1, align = 'C')
    pdf.set_text_color(179, 163, 105) 
    
    # save the pdf with name .pdf
    print("Process completed")
    pdf.footer()
    
    # additional link 
    #pdf image fix/position needs to be fixed
    #TODO: add image to repo pdf.image('vm2.png', 110, 250, 100)
    #pdf.image('vm.png', 100, 150, 100)
    pdf.output("./generated_pdfs/" + temp_link + ".pdf")
    #return pdf.output(dest = "S").encode('latin-1')
    
    #will change the formatting of the fpdf
    
    # Here is the result of the Lepto-Classifier   [logo of vm office]
    
    # display the result 
    
    # credential by uc davis 

