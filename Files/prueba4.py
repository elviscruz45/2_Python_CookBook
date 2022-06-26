
# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']
  
# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal:animal.upper()+"hla", animals))
  
print(uppered_animals)