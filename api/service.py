import os
import pdfkit
from flask import render_template_string, send_file, make_response

def validateInfo(attribute, object, messageArr):
    if attribute not in object:
        messageArr.append(attribute + ' is required.')

def reportPdf(template_name, data):
    html_path = os.path.join(os.path.abspath('api/templates'), template_name) 
    with open(html_path, 'r', encoding='utf-8') as f:
        html_template = f.read()
    html_content = render_template_string(html_template, **data)
    
    options = {
        'page-size': 'A4',
        "page-width": "20.55in",
        "page-height": "30in",
        'margin-top': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'margin-right': '0mm'
    }   
    config = pdfkit.configuration(wkhtmltopdf = os.path.abspath('wkhtmltox/bin/wkhtmltopdf.exe'))
    pdf = pdfkit.from_string(html_content, False, options=options, configuration=config)

    pdf_path = os.path.join(os.path.abspath('api'), 'report.pdf') 
    with open(pdf_path, 'wb') as f:
        f.write(pdf)

    return send_file(pdf_path, as_attachment=True)