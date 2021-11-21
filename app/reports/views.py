from . import rb
from flask import ( render_template )


###########################################################
####### Reprot View File
###########################################################

@rb.route('/report_apps',methods=['GET'])
def report_apps():
    return render_template('reports_app.html')
   