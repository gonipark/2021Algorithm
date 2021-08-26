def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    first = []
    second = []

    dict1 = {}
    dict2 = {}

    for i in range(len(str1) - 1):
        temp = str1[i] + str1[i + 1]
        if temp.isalpha():
            first.append(temp)
            if temp not in dict1:
                dict1[temp] = 1
            else:
                dict1[temp] += 1

    for j in range(len(str2) - 1):
        temp = str2[j] + str2[j + 1]
        if temp.isalpha():
            second.append(temp)
            if temp not in dict2:
                dict2[temp] = 1
            else:
                dict2[temp] += 1

    union_list = list(set(first) | set(second))
    intersection = 0
    union = 0

    if not union_list:
        intersection = 1
        union = 1
    else:
        for each in union_list:
            if (each in dict1) and (each in dict2):
                intersection += min(dict1[each], dict2[each])
                union += max(dict1[each], dict2[each])
            elif each in dict1:
                union+=dict1[each]
            elif each in dict2:
                union+=dict2[each]

    answer = int(intersection / union * 65536)
    return answer