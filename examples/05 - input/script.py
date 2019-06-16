from __future__ import print_function	# For Py2/3 compatibility
import async_eel

async_eel.init('web')                     # Give folder containing web files

@async_eel.expose                         # Expose this function to Javascript
def handleinput(x):
    print('%s' % x)

async_eel.say_hello_js('connected!')   # Call a Javascript function

async_eel.start('main.html', size=(500, 200))    # Start
