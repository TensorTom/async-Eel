from __future__ import print_function	# For Py2/3 compatibility
import async_eel, random

async_eel.init('web')

@async_eel.expose
def py_random():
    return random.random()

async_eel.start('sync_callbacks.html', block=False, size=(400, 300))

# Synchronous calls must happen after start() is called

# Get result returned synchronously by
# passing nothing in second brackets
#                   v
n = async_eel.js_random()()
print('Got this from Javascript:', n)

while True:
    async_eel.sleep(1.0)
