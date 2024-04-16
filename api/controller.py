from flask import Blueprint, request
from .service import validateInfo, reportPdf

controller = Blueprint("controller", __name__)

@controller.route("/expert_01", methods=['POST'])
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