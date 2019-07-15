import async_eel
import asyncio


loop = asyncio.get_event_loop()


async def main():
    # Set web files folder and optionally specify which file types to check for eel.expose()
    async_eel.init('web')

    # disable_cache now defaults to True so this isn't strictly necessary. Set it to False to enable caching.
    await async_eel.start('disable_cache.html', size=(300, 200), disable_cache=True)  # Start


if __name__ == '__main__':
    asyncio.run_coroutine_threadsafe(main(), loop)
    loop.run_forever()

