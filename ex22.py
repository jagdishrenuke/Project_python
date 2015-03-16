print "let's practice everything."

print 'you\'d need to know \'about escapes with \\ that do \n newline and \t tabs'

poem = """
\t the lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition	
and requires an explanation
\n\t\t where there is none.
"""
	
print "-------------"
print poem
print "-------------"
  
five = 10-2+3-6
  
print "this should be five : %s " % five
  
def secret(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates
	
	
start = 10000
beans,jars,crates = secret(start)
	
	
print "With a starting point of : %d " % start
print "We'd have %d beans,%d jars,and %d crates." % (beans,jars,crates)
	
start = start / 10
	
print "We can also do that this way : "
print "We'd have %d beans,%d jars,and %d crates." % (beans,jars,crates)
	
