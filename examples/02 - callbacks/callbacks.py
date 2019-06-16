from __future__ import print_function	# For Py2/3 compatibility
import async_eel
import random

async_eel.init('web')

@async_eel.expose
def py_random():
    return random.random()

def print_num(n):
    print('Got this from Javascript:', n)

# Call Javascript function, and pass explicit callback function    
async_eel.js_random()(print_num)

# Do the same with an inline callback
async_eel.js_random()(lambda n: print('Got this from Javascript:', n))

async_eel.start('callbacks.html', size=(400, 300))
