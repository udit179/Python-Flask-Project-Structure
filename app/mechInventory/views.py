from . import mb
from flask import render_template

###########################################################
####### Mechnical Inventory View
###########################################################

@mb.route('/mech_apps',methods=['GET'])
def mech_apps():
        return render_template('mech_inventory.html')