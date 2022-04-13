from typing import Dict
import requests
import random
import uuid
from apiconfig import (number_of_users, 
                       max_posts_per_user, 
                       max_likes_per_user)

# Utils
def get_credentials():
    credentials = f"TestUser{uuid.uuid4()}"
    return credentials

def get_token(username: str, password: str):
    request = requests.post("http://127.0.0.1:8000/api/token/",
                              json={"username": username, "password": password})
    token = request.json()["access"]
    print(f"Getting token for user: '{username}'")
    print(f"Status code is: {request.status_code}", "\n")
    return f"Bearer {token}"

# Signup users
def generate_users(n: int) -> Dict[str, str]:
    users = {}
    for i in range(n):
        credentials_ = get_credentials()
        request = requests.post("http://127.0.0.1:8000/api/users/register/", json={
                                "username": credentials_,
                                "password": credentials_,
                                "first_name": credentials_,
                                "last_name":credentials_,
                                "email": f"TestUser{credentials_}@gmail.com"
                                })
        users[credentials_] = credentials_
        print("\n", "Creating a user....")
        print(f"Status code is: {request.status_code}")
    return users
created_users = generate_users(number_of_users)
print(f"Created users: {created_users.keys()}", "\n")

# Create post/s
def create_post(n: int):
    posts_id = []
    for username, password in created_users.items():
        token = get_token(username, password)
        for i in range(random.randint(0, n)):
            request = requests.post("http://127.0.0.1:8000/api/posts/", headers={"Authorization": token},
                                json={"title": f"Post{random.randint(1, 100)}"})
            post_id = request.json()["pk"]
            posts_id.append(post_id)
            print("Creating post ....")
            print(f"Status code is: {request.status_code}", "\n")
    return posts_id
created_posts = create_post(max_posts_per_user)

# Post like/s
def like_post(n: int, posts_id: list):
    if n > len(posts_id):
        n = len(posts_id)
    for username, password in created_users.items():
        token = get_token(username, password)
        likes_num = random.randint(0, n)
        posts_to_like = random.sample(posts_id, k=likes_num)
        for post in posts_to_like:
            request = requests.post(f"http://127.0.0.1:8000/api/posts/{post}/like/create/", headers={"Authorization": token})
            print("Like post ....")
            print(f"Status code is: {request.status_code}", "\n")
start_like_post = like_post(max_likes_per_user, created_posts)

# Analytics about how many likes was made (date_format: YYYY-MM-DD)
def count_likes(date_from:str, date_to:str):
    random_user = random.sample(list(created_users), k=1)[0]
    token = get_token(random_user, random_user)
    request = requests.get(f"http://127.0.0.1:8000/api/posts/analytics/?date_from={date_from}&date_to={date_to}", headers={"Authorization": token})
    print(f"Calculating likes ....")
    print(f"Status code is: {request.status_code}")
    print(f"Total likes from {date_from} to {date_to} is: {request.content}","\n")
likes = count_likes("2022-04-12", "2022-04-14")


# Display User activity
def user_activity(pk:int = 1):
    random_user = random.sample(list(created_users), k=1)[0]
    token = get_token(random_user, random_user)
    request = requests.get(f"http://127.0.0.1:8000/api/users/{pk}/user_activity/", headers={"Authorization": token},)
    print(f"Displaying user activity ....")
    print(f"Status code is: {request.status_code}")
    print(f"Activity of user '{random_user}': {request.json()}")
display_user_activity = user_activity()

