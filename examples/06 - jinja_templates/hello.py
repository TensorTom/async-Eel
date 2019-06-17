from __future__ import print_function	# For Py2/3 compatibility
import async_eel
import asyncio


loop = asyncio.get_event_loop()


@async_eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)


async def main():
    try:
        async_eel.init('web')                     # Give folder containing web files
        await async_eel.start('templates/hello.html', size=(300, 200), jinja_templates='templates')    # Start

        say_hello_py('Python World!')
        await async_eel.say_hello_js('Python World!')  # Call a Javascript function
    except Exception:
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()
