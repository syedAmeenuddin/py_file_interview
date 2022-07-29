 import os
# open file use open()
f = open('hello.py','r')
# read file use read()
print(f.read())
# write (append) text in file use 'a'
w = open('hello.py','a')
w.write('new line added from test.py')
w.close()
# create a file use 'x'
cr = open('newfile.py','x')
# delete text and rewrite use 'w'
de = open('hello.py','w')
de.write('deleted and added new line')
de.close()
# delete file use os.remove('filename')
os.remove('hello.py')
