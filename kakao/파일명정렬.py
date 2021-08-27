def solution(files):
    answer = []
    new_files = []
    for file in files:
        temp = []
        i = 0

        while (not file[i].isdigit()):
            i += 1
        temp.append([file[0:i].upper(), file[0:i]])
        j = i

        while (file[i].isdigit() and i<len(file)-1):
            i += 1

        if i==len(file)-1:
            temp.append([int(file[j:i+1]), file[j:i+1]])
        else:
            temp.append([int(file[j:i]), file[j:i]])
            temp.append(file[i:])

        new_files.append(temp)
    #print(new_files)
    new_files.sort(key=lambda x: (x[0][0], x[1][0]))

    # print(file)
    for file in new_files:
        temp = ''
        temp += file[0][1]
        temp += file[1][1]
        if len(file)==3:
            temp += file[2]
        answer.append(temp)
    return answer

solution( ["img12", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])