# -*- coding: utf-8 -*-

import urllib.request, urllib.error
import sys

#main flow
if __name__ == "__main__":

 usersys=sys.argv
 usersyslen= len(usersys)

 if usersyslen > 1:
  url=usersys[1]
 else:
  url="http://www.python-izm.com"


 opener = urllib.request.build_opener()
 opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]

 htmldata = opener.open(url)
 print(str(htmldata.read(),"utf-8"))

 htmldata.close()
 opener.close()
