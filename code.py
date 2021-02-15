from io import RawIOBase
from sys import stdin,stdout
import math
version=2
local=True
f=open("input.txt","r")
M=pow(10,9)+7 
def mt(n,m,val=0):
	i=0
	ta=[]
	while i<n:ta.append([val]*m);i+=1
	return ta
def io(n,sep=" "):
	stdout.write(str(n))
	stdout.write(sep)
def so(st,sep='\n'):
	stdout.write(st)
	stdout.write(sep)
def lo(out,sep='\n'):
	stdout.write(" ".join(str(x) for x in out ))
	stdout.write(sep)
def cl(n):return int(math.ceil(n))
def si():
	return (f.readline() if local else stdin.readline())
def li():
	return (map(int,si().split()) if (local and version<3) else list(map(int,si().split())))
def ii():return (input() if version<3 else int(input()))
for _ in xrange(ii()):
        n,k=li()
        if n>k:
                print 1
        else:
                
