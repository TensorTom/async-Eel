from __future__ import print_function	# For Py2/3 compatibility
import async_eel, random
import asyncio

loop = asyncio.get_event_loop()


@async_eel.expose
def py_random():
    return random.random()


async def main():
    async_eel.init('web')
    await async_eel.start('sync_callbacks.html', block=False, size=(400, 300))
    # Synchronous calls must happen after start() is called

    # Get result returned synchronously by
    # passing nothing in second brackets
    #                       v
    data = await async_eel.js_random()()
    print('Got this from Javascript:', data)


if __name__ == '__main__':
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()
