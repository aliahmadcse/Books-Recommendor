from application import app
from flask import render_template, request
import pandas as pd


@app.route('/', methods=['GET', 'POST'])
def index():
    # searchItem=request.form.get('searchItem')
    # if searchItem:
    #     return render_template('index.html',searchItem=searchItem)
    books = pd.read_csv('BX-Books.csv', sep=';',error_bad_lines=False, encoding="latin-1")
    books.columns = ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication","Publisher", "Image-URL-S", "Image-URL-M", "Image-URL-L"]
    return render_template('index.html',books=books)
