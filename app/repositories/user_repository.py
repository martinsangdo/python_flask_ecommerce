from app.db.mongodb import db
from bson import ObjectId

collection = db["users"]

# def create_user(user_data: dict):
#     result = collection.insert_one(user_data)
#     return str(result.inserted_id)

def get_users():
    users = []
    for user in collection.find():
        users.append({
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        })
    return users

def get_user(user_id: str):
    user = collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        }
    return None

def delete_user(user_id: str):
    return collection.delete_one({"_id": ObjectId(user_id)})