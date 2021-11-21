from flask import Flask , render_template
 
app=Flask(__name__)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# @app.errorhandler(302)
# def methods_not_allowed(error):
#     return render_template('302.html'), 302

@app.errorhandler(500)
def handled_exception(error):
    return render_template('500.html'), 500




