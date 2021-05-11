from models.CustomTextCommand import CustomCommand

def create_command(command_text, custom_text):
    custom_command = CustomCommand(command_text=command_text, custom_text=custom_text)
    custom_command.save()

def edit_command(command_text, new_custom_text):
    try:
        custom_command = CustomCommand.objects(command_text=command_text).get()
        custom_command.custom_text = new_custom_text
        custom_command.save()
    except:
        create_command(command_text=command_text, custom_text=new_custom_text)

def get_commands():
    return CustomCommand.objects