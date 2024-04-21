import os
import pdfkit
import base64
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
        'margin-right': '0mm',
        'enable-local-file-access':True
    }   
    #config for production
    #config = pdfkit.configuration(wkhtmltopdf = os.path.join(os.path.splitdrive(os.path.abspath('.'))[0], '/usr/bin/wkhtmltopdf'))
    config = pdfkit.configuration(wkhtmltopdf = r"C:\Users\Admin\Downloads\Korean\wkhtmltox\bin\wkhtmltopdf.exe")
    css = [
        os.path.join(os.path.abspath('static/css'), 'expert_01.css'),
        os.path.join(os.path.abspath('static/css'), 'pretendard-font.css')
    ]
    pdf = pdfkit.from_string(html_content, options=options, css = css, configuration=config)
    
    #path = os.path.join(os.path.abspath('templates'), template_name) 
    #pdf_path = os.path.join(os.path.abspath('api'), 'report.pdf') 
    #pdf = pdfkit.from_file(path, pdf_path, options=options, configuration=config)
    # with open(pdf_path, 'wb') as f:
    #     f.write(pdf)

    # pdf_data = pdfkit.from_string(html_content, False)

    # Encode PDF to Base64
    pdf_base64 = base64.b64encode(pdf).decode('utf-8')
    
    return pdf_base64
    
    # return send_file(pdf_path, as_attachment=True)