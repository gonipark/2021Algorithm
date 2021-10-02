import copy
n,m=map(int,input().split())

box=[]

for i in range(n):
    box.append(list(map(int,input().split())))
newbox=copy.deepcopy(box)
def isFinised():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    stack=[]

    while(stack):
        for k in range(4):
            if isBound(j + dx[k], i + dy[k]):
                if box[j + dx[k]][i + dy[k]] == 0:
                    count += 1

    newbox[j][i] -= count
    if newbox[j][i] < 0:
        newbox[j][i] = 0
    return True
    #두덩이 이상이면 Flase, 아니면 True
def isBound(j,i):
    if 0<=j<n and 0<=i<m:
        return True
    else:
        return False

def reduceBox(j,i):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    count=0
    for k in range(4):
        if isBound(j+dx[k],i+dy[k]):
            if box[j+dx[k]][i+dy[k]]==0:
                count+=1

    newbox[j][i]-=count
    if newbox[j][i]<0:
        newbox[j][i]=0

while(isFinised()):
    box = copy.deepcopy(newbox)
    for i in range(m):
        for j in range(n):
            if box[j][i]!=0:
                reduceBox(j,i)
    break
print(newbox)