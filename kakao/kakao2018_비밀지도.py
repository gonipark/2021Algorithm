def solution(n, arr1, arr2):
    answer = []
    
    bin_num_1=[]
    bin_num_2=[]
    for dec in arr1:
        temp = bin(dec)[2:]
        ''.join(temp)
        if len(temp)!=n:
            for i in range(n-len(temp)):
                temp = '0' + temp
        bin_num_1.append(temp)
        
    for dec in arr2:
        temp = bin(dec)[2:]
        ''.join(temp)
        if len(temp)!=n:
            for i in range(n-len(temp)):
                temp = '0' + temp
        bin_num_2.append(temp)
        
    for first,second in zip(bin_num_1,bin_num_2):
        new=''
        for a,b in zip(first,second):
            if a=="0" and b=="0":
                new+=" "
            else:
                new+='#'
        answer.append(new)
    print(answer)
    return answer
