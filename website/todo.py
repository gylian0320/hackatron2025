from flask_login import current_user
import json


def load_users(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def get_current_user_tasks(user_id):
    data = load_users("instance/todo_list.json")
    for user in data:
        if user['ID'] == user_id:
            return user['Task']
    return []


