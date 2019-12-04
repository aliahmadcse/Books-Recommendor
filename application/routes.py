from application import app
from flask import render_template,request

@app.route('/',methods=['GET','POST'])
def index():
    searchItem=request.form.get('searchItem')
    if searchItem:
        return render_template('index.html',searchItem=searchItem)
    return render_template('index.html')