def solution(n, t, m, p):
    answer = ''
    candi = '0'
    for i in range(50):
        candi += change(n, i)

    now = p - 1
    while (len(answer) != t):
        print(now)
        answer += candi[now]
        now += m
    # print(answer)
    return answer


def change(n, t):
    temp = ''
    while t > 0:
        t, mod = divmod(t, n)
        if mod == 10:
            mod = 'A'
        elif mod == 11:
            mod = 'B'
        elif mod == 12:
            mod = 'C'
        elif mod == 13:
            mod = 'D'
        elif mod == 14:
            mod = 'E'
        elif mod == 15:
            mod = 'F'
        temp += str(mod)
    return temp[::-1]

print(solution(2,	4	,2	,1	))