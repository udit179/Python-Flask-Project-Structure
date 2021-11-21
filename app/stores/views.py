from . import ssb
from flask import render_template

###########################################################
####### Stores View
###########################################################

@ssb.route('/store_apps',methods=['GET'])
def store_apps():
    return render_template('store_apps.html')