from __future__ import print_function	# For Py2/3 compatibility
import async_eel

# Set web files folder
async_eel.init('web')

@async_eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

say_hello_py('Python World!')
async_eel.say_hello_js('Python World!')   # Call a Javascript function


options = {
	'mode': 'custom',
	'args': ['node_modules/electron/dist/electron.exe', '.']
}

async_eel.start('hello.html', options=options)
#eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])
