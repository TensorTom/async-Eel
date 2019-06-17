import async_eel, os, random
import asyncio


loop = asyncio.get_event_loop()


@async_eel.expose
def pick_file(folder):
    if os.path.isdir(folder):
        return random.choice(os.listdir(folder))
    else:
        return 'Not valid folder'


async def main():
    async_eel.init('web')
    await async_eel.start('file_access.html', size=(320, 120))


if __name__ == '__main__':
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()
