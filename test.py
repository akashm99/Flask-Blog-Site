# from flask_blog import db
# from flask_blog import User, Post
#
# user_1 = User(
#     username='Akash',
#     email='A@demo.com',
#     password='password'
# )
# user_2 = User(
#     username='Corey',
#     email='C@demo.com',
#     password='password'
# )
# # db.session.add(user_1)
# # db.session.add(user_2)
# # db.session.commit()
#
# print(User.query.all())
# print(User.query.filter_by(username='Akash').all())
# user = User.query.filter_by(username='Akash').all()[0]
# print(user.id)
# print(user.query.get(1))
# print(user.posts)
#
# post_1 = Post(title='Blog 1', content="First Post Content!", user_id=user.id)
# post_2 = Post(title='Blog 2', content="Second Post Content!", user_id=user.id)
# # db.session.add(post_1)
# # db.session.add(post_2)
# # db.session.commit()
#
# print(user.posts)
#
# for post in user.posts:
#     print(post.content)
#
# print(post.author)
#
# db.drop_all()
# db.create_all()
# print(User.query.all())
# print(Post.query.all())
#

import requests
from day61.corey_tutorial.flask_blog import db, login_manager
from flask_sqlalchemy import SQLAlchemy
from day61.corey_tutorial.flask_blog.models import User, Post

response = requests.get('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Flask_Blog/snippets/posts.json')
response = response.json()


user_1 = User.query.get(1)
user_2 = User.query.get(2)

for i in range(len(response)-1):
    if i % 2 == 0:
        new_post = Post(title=response[i]['title'], content=response[i]['content'], user_id=user_1.id)
        db.session.add(new_post)
        db.session.commit()
    else:
        new_post = Post(title=response[i]['title'], content=response[i]['content'], user_id=user_2.id)
        db.session.add(new_post)
        db.session.commit()

print(User.query.all())
print(len(User.query.get(1).posts))
print(len(User.query.get(2).posts))


