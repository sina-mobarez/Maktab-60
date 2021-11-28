from mongo_service import Database

db = Database()


def create_book(book_data):
    try:
        book_entry = db.book_collection.insert_one(book_data)
        return book_entry.inserted_id
    except:
        print("Inserting Error Log Failed. Data:", book_data)
        pass


def create_user(user_data):
    try:
        user_entry = db.user_collection.insert_one(user_data)
        return user_entry.inserted_id
    except:
        print("Inserting Error Log Failed. Data:", user_data)


def create_like_book(book_id, user_id):  # uniqueness
    try:
        like_book = db.book_collection.update_one({book_id}, {"$push": {"likes": {"user": user_id}}},
                                                  {'$inc': {'likes': {"count": 1}}})
        return like_book
    except:
        print("Inserting Error Log Failed. Data:", book_id, user_id)


def delete_like_book(book_id, user_id):
    try:
        delete_like = db.book_collection.update_one({book_id}, {"$pull": {"likes": {"user": user_id}}},
                                                    {'$dec': {'likes': {"count": 1}}})
        return delete_like
    except:
        print("Inserting Error Log Failed. Data:", book_id, user_id)


def create_comment_book(book_id, user_id, comment):
    try:
        comment_book = db.book_collection.update_one({book_id}, {
            "$push": {"comments": {"comment": {"user": user_id, "text": comment}}}},
                                                     {'$inc': {'comment': {"count": 1}}})
        return comment_book
    except:
        print("Inserting Error Log Failed. Data:", book_id, user_id)


def get_all_books(tag=None):  # order by like count - include only comment count
    # if tag is not none filter by tag
    try:
        if tag == None:
            all_book = db.book_collection.find({}, {"tags": 1, "likes": 1, "author": 1, "comment": {"count": 1}}).sort(
                {"likes": {"count": -1}})
            return all_book
        else:
            all_book_tag = db.book_collection.find({"tags": {"$in": [tag]}},
                                                   {"tags": 1, "likes": 1, "author": 1, "comment": {"count": 1}}).sort(
                {"likes": {"count": -1}})
            return all_book_tag


    except:
        print("There is nothing to show")


def get_all_book_comments(book_id, count, index):  # order by latest
    try:
        all_comment = db.book_collection.find({book_id}, {"comments": 1}).limit(count).skip(index)
        return all_comment
    except:
        print("Inserting Error Log Failed. Data:", book_id)


def get_all_user_liked_book(user_id):
    try:
        all_user_liked = db.book_collection.find({"likes": {"$in": [user_id]}})
        return all_user_liked
    except:
        print("Inserting Error Log Failed. Data:", user_id)


def get_all_user_liked_and_taked_comment_book(user_id):
    try:
        user_both_like_comment = db.book_collection.aggregate([{
            '$match': {'likes': {'$in': [user_id]}, 'comment': {'$in': [{'$match': {'user': user_id}}]}}
        }])
        return user_both_like_comment
    except:
        print("Inserting Error Log Failed. Data:", user_id)


def get_books_tag_count(book_id):
    try:
        count = db.book_collection.aggregate([
            {
                '$match': {
                    book_id
                }
            },
            {
                '$project': {
                    'count': {'$size': '$tags'}
                }
            }
        ])
        return count
    except:
        print("Inserting Error Log Failed. Data:", book_id)
