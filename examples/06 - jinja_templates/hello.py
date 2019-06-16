from __future__ import print_function	# For Py2/3 compatibility
import async_eel

async_eel.init('web')                     # Give folder containing web files

@async_eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

say_hello_py('Python World!')
async_eel.say_hello_js('Python World!')   # Call a Javascript function

async_eel.start('templates/hello.html', size=(300, 200), jinja_templates='templates')    # Start
