from flask import Flask , render_template , jsonify
 
app=Flask(__name__)

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404





