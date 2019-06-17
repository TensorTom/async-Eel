from __future__ import print_function  # For Py2/3 compatibility
import async_eel
import asyncio

loop = asyncio.get_event_loop()


@async_eel.expose  # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)


options = {
    'mode': 'custom',
    'args': ['node_modules/electron/dist/electron.exe', '.']
}


async def main():
    try:
        # Set web files folder
        async_eel.init('web')
        await async_eel.start('hello.html', options=options)
        # await eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])

        say_hello_py('Python World!')
        async_eel.say_hello_js('Python World!')  # Call a Javascript function
    except Exception:
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()
