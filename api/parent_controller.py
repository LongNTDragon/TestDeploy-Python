from flask import request
from .service import validateInfo, reportPdf, drawHexagon, drawScatterPlot, drawHeartRatePlot, drawGrowthPlot

def parent01():
    messageArr = []
    validateInfo('institution', request.json, messageArr)
    validateInfo('date', request.json, messageArr)
    validateInfo('name', request.json, messageArr)
    validateInfo('age', request.json, messageArr)
    validateInfo('gender', request.json, messageArr)
    
    if(len(messageArr) > 0):
        return {
            'status': False,
            'messages':messageArr
        }
    data = request.json
    drawGrowthPlot(50, 'parent01_growth.png')
    return reportPdf('parent_01.html', data)

# def parent02():
#     messageArr = []
#     validateInfo('date', request.json, messageArr)
#     validateInfo('name', request.json, messageArr)
#     validateInfo('age', request.json, messageArr)
    
#     if(len(messageArr) > 0):
#         return {
#             'status': False,
#             'messages':messageArr
#         }
    
#     data = request.json
#     drawHexagon(data)
#     return reportPdf('parent_02.html', data)

def parent03():
    messageArr = []
    validateInfo('factor1', request.json, messageArr)
    validateInfo('factor2', request.json, messageArr)
    validateInfo('factor3', request.json, messageArr)
    validateInfo('factor4', request.json, messageArr)
    validateInfo('factor5', request.json, messageArr)
    validateInfo('factor6', request.json, messageArr)
    
    validateInfo('date', request.json, messageArr)
    validateInfo('name', request.json, messageArr)
    validateInfo('age', request.json, messageArr)
    validateInfo('gender', request.json, messageArr)
    
    if(len(messageArr) > 0):
        return {
            'status': False,
            'messages':messageArr
        }
    
    data = request.json
    drawHexagon(data, 'hexagon_parent.png')
    return reportPdf('parent_03.html', data)

def parent04():
    messageArr = []
    validateInfo('date', request.json, messageArr)
    validateInfo('name', request.json, messageArr)
    validateInfo('age', request.json, messageArr)
    
    if(len(messageArr) > 0):
        return {
            'status': False,
            'messages':messageArr
        }
    
    data = request.json
    drawHeartRatePlot(data)
    return reportPdf('parent_04.html', data)

def parent05():
    messageArr = []
    validateInfo('date', request.json, messageArr)
    validateInfo('name', request.json, messageArr)
    validateInfo('age', request.json, messageArr)
    
    if(len(messageArr) > 0):
        return {
            'status': False,
            'messages':messageArr
        }
    
    data = request.json
    drawScatterPlot(data)
    return reportPdf('parent_05.html', data)

def parent06():
    messageArr = []
    validateInfo('date', request.json, messageArr)
    validateInfo('name', request.json, messageArr)
    validateInfo('age', request.json, messageArr)
    
    if(len(messageArr) > 0):
        return {
            'status': False,
            'messages':messageArr
        }
    
    data = request.json
    drawHeartRatePlot(data)
    return reportPdf('parent_06.html', data)

def parent07():
    messageArr = []
    validateInfo('date', request.json, messageArr)
    validateInfo('name', request.json, messageArr)
    validateInfo('age', request.json, messageArr)
    
    if(len(messageArr) > 0):
        return {
            'status': False,
            'messages':messageArr
        }
    
    data = request.json
    drawScatterPlot(data)
    return reportPdf('parent_07.html', data)

def parent08():
    messageArr = []
    validateInfo('date', request.json, messageArr)
    validateInfo('name', request.json, messageArr)
    validateInfo('age', request.json, messageArr)
    
    if(len(messageArr) > 0):
        return {
            'status': False,
            'messages':messageArr
        }
    
    data = request.json
    drawHeartRatePlot(data)
    return reportPdf('parent_08.html', data)

def parent09():
    messageArr = []
    validateInfo('date', request.json, messageArr)
    validateInfo('name', request.json, messageArr)
    validateInfo('age', request.json, messageArr)
    
    if(len(messageArr) > 0):
        return {
            'status': False,
            'messages':messageArr
        }
    
    data = request.json
    drawScatterPlot(data)
    return reportPdf('parent_09.html', data)
