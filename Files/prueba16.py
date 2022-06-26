# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class Test:

	# Constructor
	def __init__(self, limit):
		self.limit = limit

	# Creates iterator object
	# Called when iteration is initialized
	def __iter__(self):
		self.x = 10
		return self

	# To move to next element. In Python 3,
	# we should replace next with __next__
	def __next__(self):

		# Store current value ofx
		x = self.x

		# Stop iteration if limit is reached
		if x > self.limit:
			raise StopIteration

		# Else increment and return old value
		self.x = x + 1;
		return x

# Prints numbers from 10 to 15


iterable_value = Test(25)
iterable_obj = iter(iterable_value)
 
 
 
print(next(iterable_obj))
print(next(iterable_obj))
print(next(iterable_obj))
print(next(iterable_obj))

'''
while True:
    try:


 
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:
 
        # exception will happen when iteration will over
        break
        
'''

