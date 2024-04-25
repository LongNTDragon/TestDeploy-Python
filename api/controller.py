from flask import request
from .service import validateInfo, reportPdf, drawHexagon, drawScatterPlot

def expert01():
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
    return reportPdf('expert_01.html', data)

def expert02():
    messageArr = []
    validateInfo('factor1', request.json, messageArr)
    validateInfo('factor2', request.json, messageArr)
    validateInfo('factor3', request.json, messageArr)
    validateInfo('factor4', request.json, messageArr)
    validateInfo('factor5', request.json, messageArr)
    validateInfo('factor6', request.json, messageArr)

    validateInfo('prompted', request.json, messageArr)
    validateInfo('unprompted', request.json, messageArr)
    validateInfo('comprehensive', request.json, messageArr)
    validateInfo('prompted_percentile', request.json, messageArr)
    validateInfo('unprompted_percentile', request.json, messageArr)
    validateInfo('comprehensive_percentile', request.json, messageArr)

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
    drawHexagon(data)
    return reportPdf('expert_02.html', data)

def expert03():
    drawScatterPlot(138, 1, 'graph_scatter_plot_task-relevant.png')
    drawScatterPlot(132, 1, 'graph_scatter_plot_unprompted.png')