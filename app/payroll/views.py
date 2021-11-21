from . import pb
from flask import render_template

###########################################################
####### PayRoll View
###########################################################

@pb.route('/payroll_apps',methods=['GET'])
def payroll_apps():
    return render_template('payroll_apps.html')