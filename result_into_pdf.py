import pandas as pd
from fpdf import FPDF

#this will convert json into txt, thus we use txt file to convert it into pdf format
df = pd.read_json ('result.json')
df.to_csv ('result.txt', index = False)
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
pdf.cell(100, 10, txt = "Here is the result of the Lepto-Classifier: ",ln = 1, align = 'C')

f = open("result.txt", "r")

pdf.set_font("Times", 'BI', size = 30)
for x in f: 
    print(x)

pdf.cell(200, 100, txt = "result: " + x, ln = 1, align='C')
print(x)
pdf.set_font("Times", size = 15)
# add another cell

# the user emails 
#pdf.cell(200, 0, txt = "This is the user email + " , ln = 2, align = 'C')

# emails 
pdf.cell(200, 0, txt = "If you have any question or would like to make an inquery please visit our website: ", ln = 2, align = 'C')
pdf.set_text_color(179, 163, 105) 
pdf.cell(200, 100, txt = "(Copyright Â© 2022 UC DAVIS VETERINARY MEDICINE. All rights resereved)", ln = 2, align = 'C')

# save the pdf with name .pdf
print("Process completed")
pdf.footer()

# additional link 
#pdf image fix/position needs to be fixed
pdf.image('vm2.png', 110, 250, 100)
#pdf.image('vm.png', 100, 150, 100)
pdf.output("result.pdf") 

#will change the formatting of the fpdf

# Here is the result of the Lepto-Classifier   [logo of vm office]

# display the result 

# credential by uc davis 
# all rights given to UC DAVIS VM.. 
