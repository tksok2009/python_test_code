#sys is get array for command line option array. 
import sys

sysargv=sys.argv
sysargvs=len(sysargv)

#print sysargvs

if sysargvs > 1:
 print sysargv[1]
 print sysargvs

if sysargvs==0:
 print"please command line option"

print"END"
