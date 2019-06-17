from __future__ import print_function	# For Py2/3 compatibility
import async_eel
import asyncio


loop = asyncio.get_event_loop()


@async_eel.expose                         # Expose this function to Javascript
def handleinput(x):
    print('%s' % x)


async def main():
    async_eel.init('web')                     # Give folder containing web files
    await async_eel.start('main.html', size=(500, 250))    # Start
    await async_eel.say_hello_js('connected!')   # Call a Javascript function


if __name__ == '__main__':
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()
