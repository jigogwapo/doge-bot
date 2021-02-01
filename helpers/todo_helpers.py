import os
from datetime import datetime
from mongoengine import Document,EmbeddedDocument, connect
from mongoengine.base.fields import ObjectIdField
from mongoengine.fields import BooleanField, DateField, EmbeddedDocumentField, ListField, StringField, IntField, ReferenceField, DateTimeField

mongodb_uri = os.getenv('MONGODB_URI')
connect('starden', host=mongodb_uri)
print('Connected to database.')

class Todo(EmbeddedDocument):
    id = ObjectIdField()
    content = StringField(required=True, min_length=1, max_length=280)
    date_added = DateTimeField(required=True, default=datetime.utcnow)
    done = BooleanField(required=True, default=False)

class User(Document):
    discord_id = IntField(required=True, unique=True)
    todos = ListField(EmbeddedDocumentField(Todo))
    birthday = DateField()

def create_user(discord_id):
    user = User(discord_id=discord_id)
    user.save()

def add_todo(discord_id, content):
    user = User.objects(discord_id=discord_id).get()
    todo = Todo(content=content)
    user.todos.append(todo)
    user.save()

def get_todos(discord_id):
    user = User.objects(discord_id=discord_id).get()
    return user.todos

def set_todo_done(discord_id, todo_num):
    user = User.objects(discord_id=discord_id).get()
    todo = user.todos[todo_num-1]
    if todo.done:
        todo.done = False
    else:
        todo.done = True
    user.save()
    return todo

def delete_todo(discord_id, todo_num):
    user = User.objects(discord_id=discord_id).get()
    todo = user.todos.pop(todo_num-1)
    user.save()
    return todo

def set_all_done(discord_id):
    user = User.objects(discord_id=discord_id).get()
    for todo in user.todos:
        todo.done = True
    user.save()

def delete_all_todos(discord_id):
    user = User.objects(discord_id=discord_id).get()
    user.todos = []
    user.save()