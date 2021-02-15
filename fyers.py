f=open("airlines.csv","r")
d={}
maxTimes=0
minTimes=1e9
column=f.readline()
while True:
    line=f.readline()
    if not line:
        break
    else:
        line=line.split(",")
        airport=line[1]+', '+line[2]
        try:
            d[airport]+=1
        except KeyError:
            d[airport]=1
        maxTimes=max(maxTimes,d[airport])
airports=d.keys()
for airport in airports:
    minTimes=min(minTimes,d[airport])
output1=d
output2={}
output3={}
for airport in airports:
    if d[airport]==maxTimes:
        output2[airport]=maxTimes
    if d[airport]==minTimes:
        output3[airport]=minTimes
print (output1)
print(output2)
print(output3)