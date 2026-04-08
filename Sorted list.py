#imports for making unsorted list
import random
#randomly makes unsorted list
unsortedList=[]
for n in range(0,10,1):
    unsortedList.append(random.randint(0,100))
#sorts the list
sortedList=sorted(unsortedList)
#adds a footer
sortedList.append("last")
#makes list to store the finished output
oneItemPerList=[]
#algorithm that iterates over the list and checks if item in spot n and n+1 are different
#if they are different add item in spot n to oneItemPerList
for n in range(0,len(sortedList),1):
    if n+1!=len(sortedList):
        if sortedList[n]!=sortedList[n+1]:
            oneItemPerList.append(sortedList[n])

#print output
print(unsortedList)
print(sortedList)
print(oneItemPerList)
