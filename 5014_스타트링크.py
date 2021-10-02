def isBound(num):
    if 1<=num<=f:
        return True
    else:
        return False

f,s,g,u,d=map(int,input().split())

queue=[(s, 0)]
ans=[]
dx=[u,-d]
visited=[float('inf') for _ in range(f+1)]
count=0
while(queue):
    now,count=queue.pop(0)
    if now == g:
        ans.append(count)
        break

    for i in range(2):
        next=now+dx[i]
        if isBound(next):
            if visited[next]>count+1 :
                visited[next] = count+1
                queue.append((next, count + 1))


if ans:
    print(min(ans))
else:
    print('use the stairs')