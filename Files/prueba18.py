# Here is an example of a python inbuilt iterator
# value can be anything which can be iterate
iterable1 = 'Geeks'


iterable_obj = iter(iterable1)
 
while True:
    try:
 
        # Iterate by calling next
        #item = next(iterable_obj)
        #print(item)
        print(next(iterable_obj))
    except StopIteration:
 
        # exception will happen when iteration will over
        break