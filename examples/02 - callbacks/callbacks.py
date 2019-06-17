from __future__ import print_function	# For Py2/3 compatibility
import async_eel
import random
import asyncio


loop = asyncio.get_event_loop()


@async_eel.expose
async def py_random():
    return random.random()


async def print_num(n):
    """callback of js_random"""
    print('Got this from Javascript:', n)


async def main():
    try:
        async_eel.init('web')
        await async_eel.start('callbacks.html', size=(400, 300))

        # Call Javascript function, and pass explicit callback function
        future = await async_eel.js_random()
        await future(print_num)

        # Do the same with an inline callback
        future = await async_eel.js_random()
        await future(lambda n: print('2Got this from Javascript:', n))
    except Exception:
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()
