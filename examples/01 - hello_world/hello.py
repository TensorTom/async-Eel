from __future__ import print_function	# For Py2/3 compatibility
import async_eel
import asyncio

loop = asyncio.get_event_loop()


@async_eel.expose                         # Expose this function to Javascript
async def say_hello_py(x):
    print('Hello from %s' % x)


async def main():
    # Set web files folder
    async_eel.init('web')
    await async_eel.start('hello.html', size=(300, 200))    # Start

    await say_hello_py('Python World!')
    await async_eel.say_hello_js('Python World!')()  # Call a Javascript function
    print("OK")


if __name__ == '__main__':
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()

