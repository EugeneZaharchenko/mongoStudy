from connect import BookstoreDB


def run():
    db = BookstoreDB()

    # Update or insert
    # db.upsert_collection("BookReads", {"Title": "New book",
    #                                    "Author": "Taras Shevch", "ISBN": "7777777333"})

    # Atomic update document using update_one()
    result = db.get_book_collection('BookReads').update_one(
        {"ISBN": "1452264465"},  # Filter to match the document
        {"$inc": {"ReadCount": 1.5}}  # Update operation to increment ReadCount by 1.5
    )

    # Print the number of modified documents
    print(f"Number of documents modified: {result.modified_count}")


if __name__ == '__main__':
    run()
