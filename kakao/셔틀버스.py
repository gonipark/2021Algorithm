#50점

import datetime as dt
def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()

    now=dt.datetime.strptime('09:00', "%H:%M")
    bus=[now]
    for i in range(n-1):
        now=now+dt.timedelta(minutes=t)
        bus.append(now)

    full=0
    turn=0

    for j in range(len(timetable)):
        if full==m:
            turn+=1
            full=0
        if turn==len(bus):
            full=0
            break

        if dt.datetime.strptime(timetable[j], "%H:%M")<=bus[turn] and full<m:
            full+=1
            last=dt.datetime.strptime(timetable[j], "%H:%M")
        elif dt.datetime.strptime(timetable[j], "%H:%M")>bus[turn]:
            turn+=1
            full=0

            for i in bus[turn:]:
                if dt.datetime.strptime(timetable[j], "%H:%M")<=i:
                    full=1
                    break
            last=dt.datetime.strptime(timetable[j], "%H:%M")
            #print(timetable[j])

    if full<m:
        answer=str(bus[-1])[11:16]
    else:
        answer=str(last-dt.timedelta(minutes=1))[11:16]



    return answer

print(solution(1,	1	,5	,["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,	10,	2,	["09:10", "09:09", "08:00"]))
print(solution(2,	1	,2	,["09:00", "09:00", "09:00", "09:00"]))
print(solution(1,	1	,5,	["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1,	1	,1,	["23:59"]))
print(solution(10,	60	,45,	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))