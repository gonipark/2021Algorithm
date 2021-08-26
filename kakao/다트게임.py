def solution(dartResult):
    turn = 0
    answer = 0

    tmp1 = 0
    tmp2 = 0
    for index, i in enumerate(dartResult):
        if i.isdigit():
            if int(i) == 1:
                if dartResult[index + 1] == '0':
                    answer += tmp1
                    tmp1 = tmp2
                    tmp2 = 10

                else:
                    answer += tmp1
                    tmp1 = tmp2
                    tmp2 = 1

            elif int(i) == 0:
                if dartResult[index - 1] != '1':
                    answer += tmp1
                    tmp1 = tmp2
                    tmp2 = int(i)

            else:
                answer += tmp1
                tmp1 = tmp2
                tmp2 = int(i)

            turn += 1


        elif i.isalpha:
            if i == 'D':
                tmp2 *= tmp2
            elif i == 'T':
                tmp2 = tmp2 * tmp2 * tmp2

            elif i == '*':
                if turn == 1:
                    tmp2 *= 2
                else:
                    tmp1 *= 2
                    tmp2 *= 2

            elif i == '#':
                tmp2 = -tmp2

    answer += tmp1
    answer += tmp2

    return answer

# solution('1D2S#10S')