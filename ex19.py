
def chees_and_crackers(chees_count, boxes_of_crackers):
    print "You have %d cheeses!" % chees_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for part!"
    print "Get the blanket.\n"
	
	
print "We can just give the function numbers directly..."
chees_and_crackers(10,20)

print "or , we can use variables from our script:"
a = 15
b = 20

chees_and_crackers(a,b)

print "We can even do math inside."
chees_and_crackers(10+2,20+4)
