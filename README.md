## Problem Statement

A book recommendation system for recommending books based on user search.

## Data Set

You can download the data from [here](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)

## DATA SET DETAILS

BX-Book-Ratings.csv

- User-ID (the user who have provided the rating)
- ISBN (the ISBN of the book rated by the user)
- Book-rating (rating from 0 to 10)

BX-Books.csv

- ISBN (the ISBN of the book)
- Book-Title (the title of the book)
- Book-Author (the author of the book)
- Year-Of-Publication (the year in which the book was published)
- Publisher (publisher of the book)
- Image-URL-S (URL for a small-sized image)
- Image-URL-M (URL for a medium-sized image)
- Image-URL-L (URL for a large-sized image)

BX-Users.csv

- User-ID (the user)
- Location (the address of the user)
- Age (age of the user)

## Algorithm

The algorithm used is KNN machine learning algorith Which is actually an algorithm which look up for its Nearest neighbours.

## INSTRUCTION TO EXECUTE THE PROGRAM

1. You can clone or download the project directly from github.

2. Once you downloaded the project, you need the dataset which you can download from [here](http://www2.informatik.uni-freiburg.de/~cziegler/BX/).

3. After downloading the dataset, put it in the project directory.

4. Open up project in VSCode.

5. Fire up vscode integrated terminal.

6. Run: $ **pipenv install --ignore-pipfile** to create the same virtual environment on your machine as needed. You might need to install pipenv globally first by running $ **pip install pipenv**.

7. Vscode will detect the virtual environment and activate it. You might need to reload it once.

8. Once the virtual environment is activated, run $ **flask run**.

9. Your application will be start serving at port **5000**.

10. At home page, you will see some random books and a search box.

11. Search a book and you below that book, you will see the recommended books based on publication year.
