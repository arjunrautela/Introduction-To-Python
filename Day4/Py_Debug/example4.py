import util

filename = __file__
import pdb; pdb.set_trace()
filename_path = util.get_path(filename)
print(f'path = {filename_path}')


'''
Break point using line number
$ ./example4.py 
> /code/example4.py(7)<module>()
-> filename_path = util.get_path(filename)
(Pdb) b util:5
Breakpoint 1 at /code/util.py:5
(Pdb) c
> /code/util.py(5)get_path()
-> return head
(Pdb) p filename, head, tail
('./example4.py', '.', 'example4.py')
(Pdb) 
'''

'''
Break point using function name
./example4.py 
> /code/example4.py(7)<module>()
-> filename_path = util.get_path(filename)
(Pdb) b util.get_path
Breakpoint 1 at /code/util.py:1
(Pdb) c
> /code/util.py(3)get_path()
-> import os
(Pdb) p filename
'./example4.py'
(Pdb) 
'''