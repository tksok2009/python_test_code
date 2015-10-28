#python 3 code
#http://osksn2.hep.sci.osaka-u.ac.jp/~taku/osx/python/encoding.html
#http://docs.python.jp/3.3/tutorial/inputoutput.html


import sys;

#‚Ç‚¿‚ç‚à“®ì‚Í“¯‚¶‚¾‚ª
for line in open('test.txt','rb+'):
 print(line)

#‚±‚¿‚ç‚Í©•ª‚Åclose‚·‚éƒpƒ^[ƒ“
f = open('test.txt','rb+')
for line in f:
 print(line),

f.close()