from application import app
from flask import render_template, request
import pandas as pd

# reading the search csv dataset
books = pd.read_csv('BX-Books.csv', sep=';',error_bad_lines=False, encoding="latin-1")
books.columns = ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication","Publisher", "Image-URL-S", "Image-URL-M", "Image-URL-L"]
ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';',error_bad_lines=False, encoding="latin-1")
ratings.columns = ["User-ID", "ISBN", "Book-Rating"]

@app.route('/', methods=['GET', 'POST'])
def index():
    # getting the search query
    searchQuery = request.form.get('searchItem')
    if searchQuery:
        # searching the query in books data, it returns the rows matching with value
        searchItem=books[books['Book-Title'].str.contains(searchQuery)]
        firstRow=searchItem.iloc[0]
        bookdata = {
            'ISBN': firstRow['ISBN'],
            'Book-Title': firstRow['Book-Title'],
            'Book-Author': firstRow['Book-Author'],
            'Year-Of-Publication': firstRow['Year-Of-Publication'],
            'Publisher': firstRow['Publisher'],
            'Image-URL-S': firstRow['Image-URL-S'],
            'Image-URL-M': firstRow['Image-URL-M'],
            'Image-URL-L': firstRow['Image-URL-L']
        }
        # rating = ratings[ratings['ISBN'].str.contains(bookdata['ISBN'])]
        # rating = rating.iloc[0]
        # rating = rating['Book-Rating']
        recommendationList=KNN(books,bookdata['ISBN'],bookdata['Year-Of-Publication'])
        recommendedBooks=selectKNNBooks(books,recommendationList)
        return render_template('index.html', searchItem=bookdata, yearOfPublication=bookdata["Year-Of-Publication"],recommendedBooks=recommendedBooks)
    return render_template('index.html', books=books.sample(n=20))


def KNN(books,ISBN,yearOfPublication):
    bookList=books.values.tolist()
    distance=[]
    print(bookList[0:10])
    print("**********************************")
    print(yearOfPublication)
    for item in bookList:
        try:
            int(item[3])
        except:
            continue
        d=abs(int(yearOfPublication)-int(item[3]),)
        distance.append((item[0],d))
    distance.sort(key=lambda x:x[1])
    return distance[0:10]

def selectKNNBooks(books,recommendationList):
    recommendedBooks=list()
    for isbn,yearOfPublication in recommendationList:
        booksRow = books[books['ISBN'].str.contains(isbn)]
        firstRow = booksRow.iloc[0]
        recommendedBooks.append({
            'ISBN': firstRow['ISBN'],
            'Book-Title': firstRow['Book-Title'],
            'Book-Author': firstRow['Book-Author'],
            'Year-Of-Publication': firstRow['Year-Of-Publication'],
            'Publisher': firstRow['Publisher'],
            'Image-URL-S': firstRow['Image-URL-S'],
            'Image-URL-M': firstRow['Image-URL-M'],
            'Image-URL-L': firstRow['Image-URL-L']
        })
    return recommendedBooks


        