def isBound(i,j):
    if 0<=i<n and 0<=j<n:
        return True
    else:
        return False

def dfs(i,j):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    stack=[(i,j)]

    count=0

    while(stack):
        nowx,nowy=stack.pop()

        if box[nowx][nowy]==1:
            box[nowx][nowy] =0
            count += 1

        for k in range(4):
            nextx = nowx + dx[k]
            nexty = nowy + dy[k]

            if isBound(nextx,nexty):
                if box[nextx][nexty]==1:
                    stack.append((nextx,nexty))

    return count





n=int(input())

#box=[[0 for __ in range(n)] for _ in range(n)]
box=[]
ans=[]
for i in range(n):
    box.append(list(map(int,input())))

for i in range(n):
    for j in range(n):
        if box[i][j]==1:
            ans.append(dfs(i,j))

print(len(ans))
ans.sort()
for i in ans:
    print(i)



