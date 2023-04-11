# list can be ordered,chanageable,can have duplicate values

sampleList=["vikash","rahul","monika"]
print("==============List=======================")
print(sampleList[2])
sampleList[2]="Rakesh"
print(sampleList[2])
print(len(sampleList))
print(sampleList[0],sampleList[1],sampleList[2])
for x in sampleList:
    print(x)
print("==============Tuple=======================")
# tuples is ordered and unchangable,allow duplicate values
sampleTuple=("vikash","rahul","monika")
print(len(sampleTuple[2]))
print(len(sampleTuple))
print(sampleTuple[0],sampleTuple[1],sampleTuple[2])
for x in sampleTuple:
    print(x)

print("============range===")
somerange=range(6,1,2)
for n in somerange:
    print(n)

sampleDict={
    "name":"Vikash",
    "age":"50",
    "year":"1970"
}
print(sampleDict)
print(sampleDict["name"])
print(sampleDict["age"])