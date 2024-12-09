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
    # for book in books:
    #     print(book)

    book = book_collection.find_one({"Title": "Clara Callan"}, {"_id": 0, "Title": 1, "Author": 1, "ISBN": 1})
    # Count the number of books with the title "Clara Callan"
    count = book_collection.count_documents({"Title": "Clara Callan"})
    print(book, count)

    other_books = book_collection.find({"Ratings.UserId": ObjectId("525867733a93bb219814602c")},
                                       {"_id": 0, "Title": 1, "Author": 1, "ISBN": 1})
    #     print(list(other_books))

    # db.Book.find({"Ratings.Value": 10}).count()
    values_10 = book_collection.count_documents({"Ratings.Value": 10})
    # db.Book.find({"Ratings.Value": {$gte: 9}}).count()
    values_gte_9 = book_collection.count_documents({"Ratings.Value": {"$gte": 9}})
    values_in = book_collection.find({"Ratings.Value": {"$in": [1, 2, 4, 5]}})
    # print(values_gte_9)
    # print(list(values_in))

    # {"Ratings": {"$elemMatch": {"UserId": ObjectId("525867753a93bb2198148dc0"), "Value": 8}}}
    # print(list(book_collection.find({"Ratings": {"$elemMatch": {"UserId": ObjectId("525867753a93bb2198148dc0"),
    #                                                             "Value": 8}}})))

    # db.Book.find({"Ratings": {"$elemMatch": {"UserId": ObjectId("525867753a93bb2198148dc0"), "Value": 8}}}).sort(
    # {Title: 1})
    # print(list(book_collection.find({
    #     "Ratings": {
    #         "$elemMatch": {
    #             "UserId": ObjectId("525867753a93bb2198148dc0"),
    #             "Value": 8
    #         }
    #     }
    # }).sort({"Title": 1})))

    # book_collection.insert_one({"Title": "NEW BOOKING BOOK"})
    book_collection.update_one({"_id": ObjectId("67572e103626330c8a56b8a6")},
                               {"$set": {"Title": "Just a NEW BOOK"}})

    book_collection.delete_one({"_id": ObjectId("67572e103626330c8a56b8a6")})
    # book_collection.delete_many({"Title": "Some title"})

    db.close_connection()


if __name__ == '__main__':
    run_queries()
