#two.py

import one

print('Top level in Two.PY')

one.func()

if __name__ == '__main__':
	print('TWO.PY is being run directly')
else:
	print('TWO.PY has been imported')