
count = [1,2,3,4,5,6]
fruits = ['apple','mango','grapes','pears']
change = [1,'pennies',2,'dimes',3,'quarters']

# this first kind of for-loop goes through a list

for num in count:
    print "This is count %d " % num

# same as above

for fruit in fruits:
    print "these are fruits %s " % fruits

# also we can go through mixes lists 
# notice we have to use %r since we don't know type

for i in change:
    print "I got change %r " % change

# we can make lists, and first start with empty list

elements = []

# use the range function to do 0 to 5 counts

for j in range(0,6):
    print "adding %d to the list." % j
    # append is a function that understands
    elements.append(j)
	
for j in elements:
    print "these are the new elements added %d ." % j
   	
	