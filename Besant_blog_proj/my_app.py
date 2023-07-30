import requests

res = requests.get("http://127.0.0.1:8000/").json()

print(res)
print(type(res))


# django-admin startproject Besant_blog

# cd Besant_blog

# python manage.py startapp besantblogapp
