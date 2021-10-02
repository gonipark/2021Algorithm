import heapq as hq
import sys
left=[]
right=[]

n=int(input())

for i in range(n):
    a=int(sys.stdin.readline())
    if len(left)==len(right):
        hq.heappush(left,(-a,a))
    else:
        hq.heappush(right, (a, a))

    if left and right and left[0][1]>right[0][1]:
        q,w=hq.heappop(left)
        e,r=hq.heappop(right)

        hq.heappush(left,(-e,r))
        hq.heappush(right, (-q, w))


    print(left[0][1])