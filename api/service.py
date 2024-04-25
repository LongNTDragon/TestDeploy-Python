import os
import pdfkit
import matplotlib.pyplot as plt # type: ignore
from matplotlib.patches import Polygon, Circle # type: ignore
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
        'page-width': '25in',
        'page-height': '36in',
        
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

def drawHexagon(data):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    factor1 = (50 - data['factor1']) / 100 if data['factor1'] < 50 else 0
    factor2 = (50 - data['factor2']) / 100 if data['factor2'] < 50 else 0
    factor3 = (50 - data['factor3']) / 100 if data['factor3'] < 50 else 0
    factor4 = (50 - data['factor4']) / 100 if data['factor4'] < 50 else 0
    factor5 = (50 - data['factor5']) / 100 if data['factor5'] < 50 else 0
    factor6 = (50 - data['factor6']) / 100 if data['factor6'] < 50 else 0
    print(factor5)
    
    vertices = [
        (0 + factor5, 0 + factor5),
        (1, -0.5 + factor4),
        (2 - factor3, 0 + factor3),
        (2 - factor2, 1.2 - factor2),
        (1, 1.8 - factor1),
        (0 + factor6, 1.2 - factor6)
    ] 
    polygon = Polygon(vertices, closed=True, fill=None, edgecolor='black')
    ax.add_patch(polygon)

    for vertex in vertices:
        circle = Circle(vertex, radius=0.05, color='black', zorder=2)
        ax.add_patch(circle)

    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.6, 1.9)
    ax.set_axis_off()

    image_path = os.path.join(os.path.abspath('static/assets/images'), 'hexagon.png')
    plt.savefig(image_path, bbox_inches='tight', transparent=True)

def drawScatterPlot(x, y, image_name):
    x_coordinate = x
    y_coordinate = y

    plt.figure(figsize=(5, 5))

    plt.scatter(x_coordinate, y_coordinate, color='green', zorder=2)
    plt.plot([x_coordinate, x_coordinate], [-x_coordinate, y_coordinate], color='green', linestyle='--', zorder=2)
    plt.plot([0, x_coordinate], [y_coordinate, y_coordinate], color='green', linestyle='--', zorder=2)

    plt.grid(True)

    plt.xticks(range(72, 145, 6))
    plt.xlim(68, 148)
    plt.ylim(-1.1, 1.1) 

    image_path = os.path.join(os.path.abspath('static/assets/images'), image_name)
    plt.savefig(image_path, bbox_inches='tight', transparent=True)