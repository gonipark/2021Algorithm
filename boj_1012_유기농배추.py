def bfs(y,x):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue=[[y,x]]

    while(queue):
        nowy,nowx=queue.pop(0)
        for d in range(4):
            nextx=nowx+dx[d]
            nexty=nowy+dy[d]

            if 0<=nexty<n and 0<=nextx<m and box[nexty][nextx]==1:
                box[nexty][nextx]=0
                queue.append([nexty,nextx])

tc=int(input())

for _ in range(tc):
    count=0
    m, n, k = map(int, input().split())
    baechu=[]
    box = [[0]*m for i in range(n)]
    for __ in range(k):
        temp=list(map(int,input().split()))
        baechu.append(temp)
        box[temp[1]][temp[0]]=1

    for y in range(n):
        for x in range(m):
            if box[y][x]==1:
                bfs(y,x)
                box[y][x]=0
                count+=1

    print(count)
