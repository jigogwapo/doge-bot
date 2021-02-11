from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import ObjectIdField, DateField, StringField, DateTimeField, BooleanField, IntField, ListField, EmbeddedDocumentField

class Todo(EmbeddedDocument):
    id = ObjectIdField()
    content = StringField(required=True, min_length=1, max_length=280)
    date_added = DateTimeField(required=True, default=datetime.utcnow)
    done = BooleanField(required=True, default=False)

class User(Document):
    discord_id = IntField(required=True, unique=True)
    birthday = DateField()
    todos = ListField(EmbeddedDocumentField(Todo))
    anon_name = StringField(max_length=20)