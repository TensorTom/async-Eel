import os
import platform
import sys
import asyncio
# Use latest version of Eel from parent directory
sys.path.insert(1, '../../')
import async_eel


loop = asyncio.get_event_loop()


@async_eel.expose                         # Expose this function to Javascript
async def say_hello_py(x):
    print('Hello from %s' % x)


async def main():
    # Use the same static files as the original Example
    os.chdir(os.path.join('..', '01 - hello_world'))

    # Set web files folder and optionally specify which file types to check for eel.expose()
    async_eel.init('web', allowed_extensions=['.js', '.html'])

    # Launch example in Microsoft Edge only on Windows 10 and above
    if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
        await async_eel.start('hello.html', mode='edge')
    else:
        raise EnvironmentError('Error: System is not Windows 10 or above')

    # # Launching Edge can also be gracefully handled as a fall back
    # try:
    #     await async_eel.start('hello.html', mode='chrome-app', size=(300, 200))
    # except EnvironmentError:
    #     # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
    #     if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
    #         await async_eel.start('hello.html', mode='edge')
    #     else:
    #         raise

    await say_hello_py('Python World!')
    await async_eel.say_hello_js('Python World!')()  # Call a Javascript function
    print("OK")


if __name__ == '__main__':
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()
