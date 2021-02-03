from models.User import User, Todo

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