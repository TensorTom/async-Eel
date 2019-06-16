import async_eel, os, random

async_eel.init('web')

@async_eel.expose
def pick_file(folder):
    if os.path.isdir(folder):
        return random.choice(os.listdir(folder))
    else:
        return 'Not valid folder'

async_eel.start('file_access.html', size=(320, 120))
