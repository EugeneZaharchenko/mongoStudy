from bson import ObjectId
from connect import BookstoreDB


def run_queries():
    # Create an instance of the BookstoreDB class
    db = BookstoreDB()

    # List all databases
    databases = db.list_databases()
    print("Databases:", databases)

    # Get the 'Book' collection
    book_collection = db.get_book_collection()

    # Query the 'Book' collection and limit the result to 3 documents
    books = book_collection.find().limit(3)

    # Print the retrieved books
    for book in books:
        print(book)

    book = book_collection.find_one({"Title": "Clara Callan"}, {"_id": 0, "Title": 1, "Author": 1, "ISBN": 1})
    # Count the number of books with the title "Clara Callan"
    count = book_collection.count_documents({"Title": "Clara Callan"})
    print(book, count)

    other_books = book_collection.find({"Ratings.UserId": ObjectId("525867733a93bb219814602c")},
                                       {"_id": 0, "Title": 1, "Author": 1, "ISBN": 1})
    print(list(other_books))

    db.close_connection()


if __name__ == '__main__':
    run_queries()
