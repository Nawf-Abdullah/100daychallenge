from time import sleep

def delay_decorater(function):
	def wrapper_function():
		sleep(2)
		function()
	return wrapper_function

@delay_decorater
def say_hello():
	print('Hello')

say_hello()