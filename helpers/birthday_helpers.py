from datetime import date
from models.User import User

def save_birthday(discord_id, month, day):
    user = User.objects(discord_id=discord_id).get()
    birthday_obj = date(2000, month, day)
    user.birthday = birthday_obj
    user.save()

def get_birthdays():
    users_with_bdays = User.objects(birthday__exists=True).only('discord_id', 'birthday').order_by('birthday')
    return users_with_bdays

def get_birthdays_on(month, day):
    birthday_obj = date(2000, month, day)
    return User.objects(birthday=birthday_obj)

def get_birthdays_today():
    today = date.today()
    today = today.replace(year=2000)
    users_with_bdays_today = User.objects(birthday=today)
    return users_with_bdays_today