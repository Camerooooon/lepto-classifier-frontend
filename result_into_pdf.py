from fpdf import FPDF
from result import Result

def gen_pdf(data, result: Result, temp_link: str):
    #this will convert json into txt, thus we use txt file to convert it into pdf format
    pdf = FPDF('P', 'mm', (100, 150))
    
    # variable pdf
    pdf = FPDF(format='letter')
    
    # Add a page
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', size = 17)
    #this will make print the color in red 
    pdf.set_text_color(0, 40, 85) 
    pdf.ln(.15)
    pdf.set_author("Dr.Reagan")
    pdf.cell(200, 0, txt = "Here is the result of the Leptospirosis Machine Learning Algorithm: ",ln = 0, align = 'L')
    #result moved to new location 
    pdf.cell(200, 20, txt = "Result: " + Result.fmt(result), ln = 0, align='C')
    print(Result.fmt(result))
    pdf.set_font("Helvetica", 'BI', size = 18)
    pdf.set_font("Helvetica", size = 12)
    pdf.set_text_color(179, 163, 105) 
    pdf.cell(200, 45, ln=1)
    i = 1;
    #how to make coulmns go side by side 
    for data_point in data:
        if (i == 42):
            break 
        elif (i >= 20): 
            pdf.cell(100,-50)
            pdf.cell(50, -8.6, border = 0, txt= str(data_point), align = 'C')
            pdf.cell(50, -8.6, border = 0, txt= str(data[data_point][0]), ln= 1, align = 'C')
            i += 1
        else: 
            pdf.cell(50, 10, border = 0, txt= str(data_point), align = 'C')
            pdf.cell(50, 10, border = 0, txt= str(data[data_point][0]), ln= 1, align = 'C')
            i += 1 
        #does not work to send this side 

    print(i)
    
    pdf.set_font("Helvetica", 'BI', size = 20)
    pdf.set_text_color(0, 40, 85) 
    pdf.cell(200, -20, ln=1)
    pdf.cell(200, -1, txt = "Result: " + Result.fmt(result), ln = 0, align='C')
    #pdf.cell(200, 200, border = 0, txt = "If you have any question or would like to make an inquiry please visit our website: ", ln = 1, align = 'C')
   
   #cant print the bottom parts for some reason 
    pdf.cell(200, 100, border = 0, txt= "https://drkrystlereagan.com/", ln= 1, align = 'C')
    #pdf.set_font("Helvetica", 'B', size = 8)
    #pdf.cell(200, 146, border = 0, txt = "(Copyright © 2022 UC DAVIS VETERINARY MEDICINE. All rights reserved)", ln = 1, align = 'C')
    # save the pdf with name .pdf
    print("Process completed")
    pdf.footer()
    
    pdf.output("./generated_pdfs/" + temp_link + ".pdf")


