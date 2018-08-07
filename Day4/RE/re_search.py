import re
line = "Cats are smarter than dogs than"

searchObj = re.search('are', line)
if searchObj :
    print "search --> searchObj.group():",searchObj.group()
else :
    print "Nothing found!!"
