import time

currentNumber=1
largestPrime=0
endTime=time.time()+1


#check if it is prime
while time.time()<endTime:
    if currentNumber%2!=0 or currentNumber==2:
        for n in range(2,currentNumber+1,1):
            if  currentNumber%n==0 and currentNumber!=n:break
            if currentNumber==n:largestPrime=currentNumber
    currentNumber+=1
print("prime=",largestPrime,"number of iterations=",currentNumber)
