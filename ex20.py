from sys import argv

script,new_file = argv

def print_all(f):
     print f.read()
	 

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print line_count,f.readline()


current_file = open(new_file)

print "first let's print the whole file.."	

print_all(current_file)

print "now let's rewind , kind of like tape."

rewind(current_file)

print "let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
