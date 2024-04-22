import os
import pdfkit
from flask import render_template_string, send_file

def validateInfo(attribute, object, messageArr):
    if attribute not in object:
        messageArr.append(attribute + ' is required.')

def reportPdf(template_name, data):
    absolute_path = '/app'

    #production
    # html_path = os.path.join(os.path.abspath('api/templates'), template_name)
    html_path = os.path.join(os.path.abspath('api/templates_dev'), template_name) 
    with open(html_path, 'r', encoding='utf-8') as f:
        html_template = f.read()
    html_content = render_template_string(html_template, **data, absolute_path=absolute_path)
    
    options = {
        #local
        'page-width': '25.83in',
        'page-height': '36.54in',
        
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'margin-right': '0mm',
        'enable-local-file-access': None
    }

    #production
    #config = pdfkit.configuration(wkhtmltopdf = os.path.join(os.path.splitdrive(os.path.abspath('.'))[0], '/usr/bin/wkhtmltopdf'))
    config = pdfkit.configuration(wkhtmltopdf = r"C:\Users\Admin\Downloads\Korean\wkhtmltox\bin\wkhtmltopdf.exe")
    
    pdf = pdfkit.from_string(html_content, options=options, configuration=config)
     
    pdf_path = os.path.join(os.path.abspath('api'), 'report.pdf') 
    with open(pdf_path, 'wb') as f:
        f.write(pdf)
    
    return send_file(pdf_path, as_attachment=True)