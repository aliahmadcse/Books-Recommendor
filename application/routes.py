from application import app
from flask import render_template, request
import pandas as pd


@app.route('/', methods=['GET', 'POST'])
def index():
    #reading the search csv dataset
    books = pd.read_csv('BX-Books.csv', sep=';',error_bad_lines=False, encoding="latin-1")
    books.columns = ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication","Publisher", "Image-URL-S", "Image-URL-M", "Image-URL-L"]
    ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';', error_bad_lines=False, encoding="latin-1")
    ratings.columns = ["User-ID","ISBN","Book-Rating"]
    #getting the search query
    searchQuery=request.form.get('searchItem')
    if searchQuery:
        #searching the query in books data, it returns the rows matching with value
        for index, row in books.iterrows():
            if row['Book-Title']==searchQuery:
                bookTitle=row['Book-Title']
                break
        return render_template('index.html',searchItem=bookTitle)
    return render_template('index.html',books=books.sample(n=20))
    
