from app.repositories import user_repository

def create_user(data):
    return user_repository.create_user(data)

def get_all_users():
    return user_repository.get_users()

def get_user_by_id(user_id: str):
    return user_repository.get_user(user_id)

def delete_user(user_id: str):
    return user_repository.delete_user(user_id)