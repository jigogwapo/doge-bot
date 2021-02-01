from datetime import date
from models.User import User

def save_birthday(discord_id, year, month, day):
    user = User.objects(discord_id=discord_id).get()
    birthday_obj = date(year, month, day)
    user.birthday = birthday_obj
    user.save()