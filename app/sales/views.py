from . import sb
from flask import render_template

@sb.route('/sales_apps',methods=['GET'])
def sales_apps():
    return render_template('sales_apps.html')