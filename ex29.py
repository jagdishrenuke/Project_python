
# this is example of implicit

class parent(object):

    def implicit(self):
	    print "Parent implicit()."

		
class child(parent):
    pass       # show nothing to define or declare 
	
dad = parent()
son = child()

dad.implicit()
son.implicit()


# this is example of explicit

class father(object):

    def overide(self):
	    print "parent Override example."

class son(father):

    def overide(self):
	    print "child override example."
		
dad = father()

beta = son()

dad.overide()
beta.overide()


# this is example of override parent on child

class mammy(object):
     
    def alter(self):
        print "Parent alter :"

class da(mammy):


    def alter(self):
        print "child alter :"
        super(da,self).alter()
        print "child, after parent alter()"
		
m = mammy()
n = da()

m.alter()
n.alter()

