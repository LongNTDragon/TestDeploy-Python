import os
import pdfkit
import matplotlib.pyplot as plt # type: ignore
from matplotlib.patches import Polygon, Circle # type: ignore
from flask import render_template_string, send_file
import pandas as pd # type: ignore
from scipy.signal import butter, filtfilt # type: ignore
import numpy as np # type: ignore
plt.rcParams['font.family'] = 'Malgun Gothic'

def validateInfo(attribute, object, messageArr):
    if attribute not in object:
        messageArr.append(attribute + ' is required.')

def reportPdf(template_name, data):
    absolute_path = '/app'

    #production
    #html_path = os.path.join(os.path.abspath('api/templates'), template_name)
    html_path = os.path.join(os.path.abspath('api/templates_dev'), template_name) 
    with open(html_path, 'r', encoding='utf-8') as f:
        html_template = f.read()
    html_content = render_template_string(html_template, **data, absolute_path=absolute_path)
    
    options = {
        #local
        'zoom': 0.6,

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

def drawHexagon(data, image_name):
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

    image_path = os.path.join(os.path.abspath('static/assets/images'), image_name)
    plt.savefig(image_path, bbox_inches='tight', transparent=True)

def drawScatterPlot(x, y, image_name, name):
    x_coordinate = x
    y_coordinate = y

    plt.figure(figsize=(9, 9))

    extraX = 9 if x < 85 else -9
    extraY = 0.1 if y < -0.95 else -0.1
    
    plt.scatter(x_coordinate, y_coordinate, color='green', zorder=2)
    plt.plot([x_coordinate, x_coordinate], [-x_coordinate, y_coordinate], color='green', linestyle='--', zorder=2)
    plt.plot([0, x_coordinate], [y_coordinate, y_coordinate], color='green', linestyle='--', zorder=2)
    plt.text(x + extraX, y + extraY, name + ' 어린이', color='#45b480', fontsize=12, ha='center', va='center', bbox=dict(boxstyle='round', facecolor='#fff', edgecolor='none'))


    plt.grid(True)

    plt.xticks(range(72, 145, 6))
    plt.xlim(68, 148)
    plt.ylim(-1.1, 1.1)

    image_path = os.path.join(os.path.abspath('static/assets/images'), image_name)
    plt.savefig(image_path, bbox_inches='tight', transparent=True)

def drawHeartRatePlot(axis_value, column, color, image_name):
    df = pd.DataFrame(axis_value, columns=[column])
    df = df.reset_index(drop=True)

    percentile = {}
    percentile[column] = pd.read_csv(f"api/percentile.csv")
    percentile[column] = percentile[column].reset_index(drop=True)

    width = 2015 / 100
    height = 680 / 100
    plt.figure(figsize=(width, height))

    plt.plot(df, color=color, label=column)

    fs = 10 
    nyq = 0.5 * fs
    cutoff = 2 
    normal_cutoff = cutoff / nyq
    order = 2
    b, a = butter(order, normal_cutoff, btype='low', analog=False)

    smooth_min = filtfilt(b, a, percentile[column]['Min'].iloc[:len(df)])
    smooth_max = filtfilt(b, a, percentile[column]['Max'].iloc[:len(df)])

    plt.fill_between(df.index, smooth_min, smooth_max, color=color, alpha=0.3, linewidth=0)

    plt.ylabel(column + '-axis \n Movement Velocity')
    plt.xlim(10, len(df)-10)
    plt.ylim(-1.5, 1.5)
    plt.xticks([])
    plt.grid(True)
    plt.legend()
    image_path = os.path.join(os.path.abspath('static/assets/images'), image_name)
    plt.savefig(image_path, bbox_inches='tight')

def drawScatterPlotNoAxis(x, y, image_name, name):
    extraX = 9 if x < 35 else -9
    extraY = 5 if y < 25 else -5

    plt.figure(figsize=(12.7, 9.5))
    plt.scatter(x, y, color='green')
    plt.text(x + extraX, y + extraY, name + ' 어린이', color='#45b480', fontsize=12, ha='center', va='center', bbox=dict(boxstyle='round', facecolor='#fff', edgecolor='none'))


    plt.axhline(y=y, linestyle='--', color='green')
    plt.axvline(x=x, linestyle='--', color='green')

    plt.xlim(0, 100)
    plt.ylim(0, 100)
    
    plt.xlabel('Prompted Movement')
    plt.ylabel('Unprompted Movement')
    plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)

    image_path = os.path.join(os.path.abspath('static/assets/images'), image_name)
    plt.savefig(image_path, bbox_inches='tight', transparent=True)

def drawGrowthPlot(percent, image_name):
    percentiles = np.linspace(0, 100, 1001)
    values = np.sin(percentiles * np.pi / 200) * 100 

    plt.figure(figsize=(29.4, 5))
    plt.plot(percentiles, values, marker='o', markersize=10, markevery=[percent*10], color='#0c4999')
    
    extra = 0
    if(percent > 10 and percent <= 34):
        extra += 10
    if(percent > 34 and percent <= 75):
        extra += 20
    if(percent > 75 and percent <= 95):
        extra += 5
    plt.plot([percent, percent], [percent + extra, 0], linestyle='dashed', color='#0c4999')
    plt.text(percent, percent-extra+15, percent, fontsize=20, ha='right')

    plt.gca().axes.get_yaxis().set_visible(False)
    plt.xticks(range(0, 101, 100))
    plt.xlim(0, 101)
    plt.xlabel('(percentile)')
    image_path = os.path.join(os.path.abspath('static/assets/images'), image_name)
    plt.savefig(image_path, bbox_inches='tight')