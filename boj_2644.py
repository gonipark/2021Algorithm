nums=int(input())
targetA,targetB=map(int,input().split())
edge_num=int(input())
tree=[]
visited=[0 for _ in range(nums+1)]
result=[0 for _ in range(nums+1)]

for _ in range (edge_num):
    a,b=map(int,input().split())
    tree.append([a,b])
    tree.append([b,a])

def bfs(x):
    que=[x]
    flag=False
    while que:
        now=que.pop(0)
        visited[now]=1
        for each in tree:
            if each[0]==now and visited[each[1]]==0:
                que.append(each[1])
                result[each[1]]=result[each[0]]+1
                if each[1]==targetB:
                    flag=True
                    break
        if flag:
            break

bfs(targetA)
print(result[targetB] if result[targetB] != 0 else -1)
