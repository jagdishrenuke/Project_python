
class parent(object):
   
    def override(self):
	    print "Parent override ."

    def implicit(self):
        print "Parent Implicit."

    def alter(self):
        print "Parent alter."

class child(parent):
   
    def override(self):
        print "Child override ."
 
 
    def alter(self):
        print "Child alter."
        super(child,self).alter()
        print "Child, parent alter."


dad = parent()
son = child()

dad.override()
son.override()

dad.implicit()
son.implicit()

dad.alter()
son.alter()





	