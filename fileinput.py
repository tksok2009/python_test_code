#python 3 code
#http://osksn2.hep.sci.osaka-u.ac.jp/~taku/osx/python/encoding.html
#http://docs.python.jp/3.3/tutorial/inputoutput.html


import sys;

#どちらも動作は同じだが
for line in open('test.txt','rb+'):
 print(line)

#こちらは自分でcloseするパターン
f = open('test.txt','rb+')
for line in f:
 print(line),

f.close()