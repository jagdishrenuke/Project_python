
def add(a,b):
    print "add %d + %d" % (a,b)
    return a + b

def sub(a,b):
    print "sub %d - %d" % (a,b)
    return a - b
	
def mul(a,b):
    print "mul %d * %d" % (a,b)
    return a * b
	
def div(a,b):
    print "div %d / %d " % (a,b)
    return a / b

print " Let's do some mathematics "

Add = add(12,12)
Sub = sub(10,10)
Mul = mul(3,4)
Div = div(10,5)

print "Age: %d , Sub: %d , Mul: %d , Div: %d" % (Add,Sub,Mul,Div)
