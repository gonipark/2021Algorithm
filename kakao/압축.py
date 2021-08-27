def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(ord('A') + i)] = i + 1

    now = 27
    j = 1
    while (j <= len(msg)):
        i=j-1
        while (msg[i:j] in dic and j<=len(msg)):
            j += 1
        answer.append(dic[msg[i:j - 1]])
        dic[msg[i:j]] = now
        now += 1
    print(answer)
    return answer

solution('TOBEORNOTTOBEORTOBEORNOT')