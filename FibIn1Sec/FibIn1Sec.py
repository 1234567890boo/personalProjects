#imports
import time,cProfile,functools
#func for debugging
@functools.lru_cache(maxsize=None)
def main(startTime,endTime,bitmask,fib,count):
    fibA=fib[0]
    fibB=fib[1]
    #runloop
    while time.perf_counter()<=endTime:
        #does the fibonacci loop
        fibA+=fibB&bitmask
        fibB+=fibA&bitmask
        #adds 2 to the count because the above loop fints the next 2 fibonacci numbers
        count+=2
    #prints it
    length=time.perf_counter()-startTime
    print(str(count)+" in "+str(length)+" Sec")
    
#cProfile.run("main(time.perf_counter(),time.perf_counter()+1,(1<<16)&0xFFFF,[0,1],0)")
main(time.perf_counter(),time.perf_counter()+1,(1<<16)&0xFFFF,tuple([0,1]),0)
