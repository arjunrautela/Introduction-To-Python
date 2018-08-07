import re
line = "Cats are smarter than dogs"

matchObj = re.match( 'Cats', line, re.M|re.I)
if matchObj :
    print "match --> matchObj.group():",matchObj.group()
else :
    print "No match!!"

