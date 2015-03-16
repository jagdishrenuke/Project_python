
ten_things = "apple orange crows telephone light sugar"

print "wait there are not 10 things in that list."

stuff = ten_things.split(' ')

more_stuff = ["day","night","song","girl","frisbee","cool","banana","boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ",next_one
    stuff.append(next_one)
    print "there are %d items now." % len(stuff)
	
print "We have : ",stuff

print "Let's do something with the stuff..."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])	
