n=int(input())
s=input()+'.'
l=[]
last=-1
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        l.append([s[i],str(i-last)])
        last=i
s=''
print (1)
for i in l:
    s+="\""+i[0]+"\""+"*"+i[1]+"+"
s=s[0:len(s)-1]
print ("print("+s+")")
#print("all"*2)
    