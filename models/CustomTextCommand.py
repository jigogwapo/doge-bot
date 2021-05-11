from mongoengine import Document
from mongoengine.fields import ObjectIdField, StringField

class CustomCommand(Document):
    command_text = StringField(required=True, unique=True, min_length=1, max_length=10)
    custom_text = StringField(required=True, min_length=1, max_length=280)