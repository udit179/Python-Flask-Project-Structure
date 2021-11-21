from . import eb
from flask import render_template


###########################################################
####### Electonic Inventory
###########################################################

@eb.route('/elec_apps',methods=['GET'])
def elec_apps():
    return render_template('elec_inven.html')

