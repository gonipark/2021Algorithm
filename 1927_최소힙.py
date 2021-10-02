import heapq as hq
import sys

n=int(input())
heap=[]
for i in range(n):
    a=int(sys.stdin.readline())
    if a!=0:
        hq.heappush(heap,a)
    else:
        if len(heap)==0:
            print(0)
        else:
            print(hq.heappop(heap))