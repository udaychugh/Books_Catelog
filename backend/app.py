from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
        {
      "key": 1,
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "description": "A powerful story of racial injustice and the loss of innocence in the Deep South.",
      "price": 400,
      "rating": 4.5,
      "genre": "Fiction",
      "cover_image": "https://m.media-amazon.com/images/I/41j-s9fHJcL.jpg",
      "publication_date": "1960"
    },
    {
      "key": 2,
      "title": "1984",
      "author": "George Orwell",
      "description": "A dystopian novel depicting a totalitarian future society controlled by Big Brother.",
      "price": 350,
      "rating": 4.7,
      "genre": "Science Fiction",
      "cover_image": "https://m.media-amazon.com/images/I/41aM4xOZxaL._SX277_BO1,204,203,200_.jpg",
      "publication_date": "1949"
    },
    {
      "key": 3,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "description": "Set in the 1920s, this classic novel explores themes of love, wealth, and the American Dream.",
      "price": 300,
      "rating": 4.3,
      "genre": "Fiction",
      "cover_image": "https://m.media-amazon.com/images/I/51ceqZss88S._SX460_BO1,204,203,200_.jpg",
      "publication_date": "1925"
    },
    {
      "key": 4,
      "title": "Pride and Prejudice",
      "author": "Jane Austen",
      "description": "A witty and timeless romance novel following the lives of the Bennet sisters.",
      "price": 250,
      "rating": 4.6,
      "genre": "Fiction",
      "cover_image": "https://m.media-amazon.com/images/M/MV5BMTA1NDQ3NTcyOTNeQTJeQWpwZ15BbWU3MDA0MzA4MzE@._V1_.jpg",
      "publication_date": "1813"
    },
    {
      "key": 5,
      "title": "The Lord of the Rings",
      "author": "J.R.R. Tolkien",
      "description": "An epic fantasy trilogy set in the fictional world of Middle-earth.",
      "price": 800,
      "rating": 4.9,
      "genre": "Fantasy",
      "cover_image": "https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_.jpg",
      "publication_date": "1954-1955"
    },
    {
      "key": 6,
      "title": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "description": "A coming-of-age novel narrated by the rebellious teenager Holden Caulfield.",
      "price": 350,
      "rating": 4.2,
      "genre": "Fiction",
      "cover_image": "https://m.media-amazon.com/images/I/418bOQWiRBL._SY264_BO1,204,203,200_QL40_FMwebp_.jpg",
      "publication_date": "1951"
    },
    {
      "key": 7,
      "title": "Harry Potter and the Philosopher's Stone",
      "author": "J.K. Rowling",
      "description": "The first book in the Harry Potter series, introducing the magical world of Hogwarts.",
      "price": 500,
      "rating": 4.8,
      "genre": "Fantasy",
      "cover_image": "https://m.media-amazon.com/images/I/51SkIDTd9rL._SX323_BO1,204,203,200_.jpg",
      "publication_date": "1997"
    },
    {
      "key": 8,
      "title": "The Alchemist",
      "author": "Paulo Coelho",
      "description": "A philosophical novel about a young shepherd's journey to find his personal legend.",
      "price": 400,
      "rating": 4.5,
      "genre": "Fiction",
      "cover_image": "https://m.media-amazon.com/images/I/41e+TR4xPDL._SX328_BO1,204,203,200_.jpg",
      "publication_date": "1988"
    },
    {
      "key": 9,
      "title": "To the Lighthouse",
      "author": "Virginia Woolf",
      "description": "A stream-of-consciousness novel exploring the inner lives of the Ramsay family.",
      "price": 300,
      "rating": 4.1,
      "genre": "Fiction",
      "cover_image": "https://m.media-amazon.com/images/I/41GWqsNHAPL.jpg",
      "publication_date": "1927"
    },
    {
      "key": 10,
      "title": "The Hobbit",
      "author": "J.R.R. Tolkien",
      "description": "A fantasy adventure that follows Bilbo Baggins as he embarks on a quest to reclaim a treasure.",
      "price": 350,
      "rating": 4.7,
      "genre": "Fantasy",
      "cover_image": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a9/The_Hobbit_trilogy_dvd_cover.jpg/220px-The_Hobbit_trilogy_dvd_cover.jpg",
      "publication_date": "1937"
    },
    {
      "key": 11,
      "title": "The Kite Runner",
      "author": "Khaled Hosseini",
      "description": "A gripping tale of friendship and redemption set against the backdrop of Afghanistan's turbulent history.",
      "price": 400,
      "rating": 4.6,
      "genre": "Fiction",
      "cover_image": "https://m.media-amazon.com/images/I/51bt7LtryoL._SX314_BO1,204,203,200_.jpg",
      "publication_date": "2003"
    },
    {
      "key": 12,
      "title": "Brave New World",
      "author": "Aldous Huxley",
      "description": "A dystopian novel exploring a future society where happiness and stability come at a great cost.",
      "price": 300,
      "rating": 4.4,
      "genre": "Science Fiction",
      "cover_image": "https://m.media-amazon.com/images/I/41cDU2B8IyL._SX323_BO1,204,203,200_.jpg",
      "publication_date": "1932"
    },
    {
      "key": 13,
      "title": "Gone Girl",
      "author": "Gillian Flynn",
      "description": "A psychological thriller that delves into a complex marriage and a shocking disappearance.",
      "price": 350,
      "rating": 4.3,
      "genre": "Mystery/Thriller",
      "cover_image": "https://m.media-amazon.com/images/M/MV5BMTk0MDQ3MzAzOV5BMl5BanBnXkFtZTgwNzU1NzE3MjE@._V1_QL75_UY281_CR1",
      "publication_date": "2012"
    },
    {
      "key": 14,
      "title": "The Da Vinci Code",
      "author": "Dan Brown",
      "description": "A gripping mystery that intertwines art, history, and religion in a quest for a hidden secret.",
      "price": 400,
      "rating": 4.2,
      "genre": "Mystery/Thriller",
      "cover_image": "https://upload.wikimedia.org/wikipedia/en/e/e9/The_da_vinci_code_final.jpg",
      "publication_date": "2003"
    },
    {
      "key": 15,
      "title": "The Hunger Games",
      "author": "Suzanne Collins",
      "description": "A dystopian trilogy following Katniss Everdeen as she battles for survival in a televised fight to the death.",
      "price": 500,
      "rating": 4.7,
      "genre": "Young Adult/Dystopian",
      "cover_image": "https://m.media-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_.jpg",
      "publication_date": "2008-2010"
    },
    {
      "key": 16,
      "title": "The Girl on the Train",
      "author": "Paula Hawkins",
      "description": "A psychological thriller centered around a woman who becomes entangled in a missing person investigation.",
      "price": 350,
      "rating": 4.1,
      "genre": "Mystery/Thriller",
       "cover_image": "https://m.media-amazon.com/images/M/MV5BMTY1NTY3ODc2N15BMl5BanBnXkFtZTgwNTAwNjQzMTE@._V1_.jpg",
      "publication_date": "2015"
    },
    {
      "key": 17,
      "title": "The Picture of Dorian Gray",
      "author": "Oscar Wilde",
      "description": "A novel exploring the corrupting influence of beauty and the pursuit of pleasure.",
      "price": 300,
      "rating": 4.6,
      "genre": "Fiction",
      "cover_image": "https://m.media-amazon.com/images/I/51ojsVxjIsS._SX460_BO1,204,203,200_.jpg",
      "publication_date": "1890"
    },
    {
      "key": 18,
      "title": "The Chronicles of Narnia",
      "author": "C.S. Lewis",
      "description": "A series of fantasy novels that take readers on a journey through the magical land of Narnia.",
      "price": 800,
      "rating": 4.8,
      "genre": "Fantasy",
      "cover_image": "https://m.media-amazon.com/images/M/MV5BMTc0NTUwMTU5OV5BMl5BanBnXkFtZTcwNjAwNzQzMw@@._V1_.jpg",
      "publication_date": "1950-1956"
    },
    {
      "key": 19,
      "title": "The Help",
      "author": "Kathryn Stockett",
      "description": "A moving story set in 1960s Mississippi, where three women come together to challenge racial boundaries.",
      "price": 400,
      "rating": 4.5,
      "genre": "Historical Fiction",
      "cover_image": "https://m.media-amazon.com/images/M/MV5BMTM5OTMyMjIxOV5BMl5BanBnXkFtZTcwNzU4MjIwNQ@@._V1_.jpg",
      "publication_date": "2009"
    },
    {
      "key": 20,
      "title": "Sapiens: A Brief History of Humankind",
      "author": "Yuval Noah Harari",
      "description": "An engaging exploration of the history and impact of Homo sapiens on the world.",
      "price": 450,
      "rating": 4.4,
      "genre": "Non-fiction",
      "cover_image": "https://m.media-amazon.com/images/I/41yu2qXhXXL._SX324_BO1,204,203,200_.jpg",
      "publication_date": "2014"
    }
    
    
]



# Define routes
@app.route('/books', methods=['GET'])
def get_books():
    # Retrieve books from the database and return as JSON
    return jsonify(books)

@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    # Search books by title, author, or category
    results = [book for book in books if query.lower() in book['title'].lower() or
               query.lower() in book['author'].lower() or query.lower() in book['genre'].lower()]
    return jsonify(results)

def filter_books():
    genre = request.args.get('genre')
    min_price = float(request.args.get('min_price'))
    max_price = float(request.args.get('max_price'))
    # Filter books by genre and price range
    results = [book for book in books if book['genre'].lower() == genre.lower() and
               min_price <= book['price'] <= max_price]
    return jsonify(results)


@app.route('/')
def home():
    return books



# Implement other routes for CRUD operations, shopping cart, orders, etc.

# Run the Flask app
if __name__ == '__main__':
    app.run()
