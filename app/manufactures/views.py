from . import mfb
from flask import render_template

###########################################################
####### Electonic Inventory
###########################################################

@mfb.route('/manf_apps',methods=['GET'])
def manf_apps():
    return render_template('manuf_apps.html')

