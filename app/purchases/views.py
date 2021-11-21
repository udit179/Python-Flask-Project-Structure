from . import pob
from flask import ( render_template )


###########################################################
####### Purchase Orders Apps
###########################################################

@pob.route('/po_apps',methods=['GET'])
def po_apps():
    return render_template('po_apps.html')
   