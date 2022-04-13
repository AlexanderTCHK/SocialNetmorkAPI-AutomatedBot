# SocialNetmorkAPI-AutomatedBot
Simple Social Network API (via [Django REST framework](http://www.django-rest-framework.org/)) with Automated Bot to demonstrate functionality of API

## Requirements
- Python 3.8
- Django 4.0.3
- Django REST Framework 3.13.1
- Django-filter 21.1
- Django REST Framework Simplejwt 5.1.0 

## Installation
After you cloned the repository, you can create a virtual environment, so you have a clean python installation. After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html).

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have three resources, `Tokens`, `Users` and `Posts`, so we will use the following URLS (endpoints):
 - `api/token/` 
    - _HTTP Method - POST_
    - _Result - Get toketn_
 - `api/token/refresh/`
    - _HTTP Method - POST_
    - _Result - Refresh token_

 - `/api/users/` 
    - _HTTP Method - GET_
    - _Result - Create a new user_
 - `/api/users/register/`
    - _HTTP Method - POST_
    - _Result - Sign up user_
 - `/api/users/<int:pk>/user_activity/` 
    - _HTTP Method - GET_
    - _Result - Display user activity_

 - `/api/posts/` 
    - _HTTP Method - GET POST_
    - _Result - Get/Create post_
 - `/api/posts/<int:pk>/like/create/`
    - _HTTP Method - POST_
    - _Result - Like a post_
 - `/api/posts/<int:pk>/like/delete/` 
    - _HTTP Method - POST_
    - _Result - Dislike a post_
 - `/api/posts/analytics/` 
    - _HTTP Method - GET_
    - _Result - Display like analytics_

## Use
We can test the API directly throught test_script.py (modify apiconfig.py if needed), or you can use [Postman](https://www.postman.com/).

To start up Django's development server run:
```
python manage.py runserver
```

