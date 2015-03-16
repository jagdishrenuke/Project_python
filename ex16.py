
from sys import argv

script,file_name = argv

print "We are going to erase file %s ." % file_name

print "If you don't want that , hit CTRL-C (^C) ."

print "If you do want that, hit RETURN ."

raw_input("?")

print "Opening the file ..."
txt = open(file_name,'w')

print "Truncating the file...goodbye !"
txt.truncate()

print "Write three lines to add in file .."

line1 = raw_input("line 1 : ")
line2 = raw_input("line 2 : ")
line3 = raw_input("line 3 : ")

print "I am going to write these lines to file.."

txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")



print "And finally close file..."
txt.close()

print "I am going to reopen the file %s " % file_name

txt = open(file_name)

print txt.read()
