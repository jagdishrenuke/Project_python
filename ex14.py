
from sys import argv

script,user_name ,game= argv

prompt = '-->'

print "hii %s , I am the %s script ." %(user_name,script)

print "I'd like to ask you a few questions ."

print "Do you like me %s ." % user_name
likes = raw_input(prompt)

print "Where do you live ?"
lives = raw_input(prompt)

print "What kind of computer you have ?"
computer = raw_input(prompt)

print "Which is your favourite game on computer"
favourite = raw_input(prompt)

print """
   Alright, so you said %r about liking me.
   you live in %r. Not sure where that is.
   and you have a %r computer. Nice.
   and %s is your favourite game.
   Its really nice .....
   """ % (likes,lives,computer,favourite)
