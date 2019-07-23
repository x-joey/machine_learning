temp_list = list()
result_list = list()
N = {'A':1, 'C':2, 'D':3, 'E':4,'F':5, 'G':6, 'H':7, 'I':8, 'K':9, 'L':10, 'M':11, 'N':12, 'P':13, 'Q':14, 'R':15, 'S':16, 'T':17, 'V':18, 'W':19, 'Y':20, 'O':21 }
with open('test.txt','r') as reader:
    while (reader.readline() != ''):
        data = reader.readline().strip('\n')  #GLSLNDRKKLLAKDLRGEMTLPATD
        print(data)
        data1 = data[0:12]          #截取前12个，不用循环，用切片
        data2 = data[13:25]         #截取前12个，用切片
        data3 = data1+data2
        for i in data3:
            temp_list.append(N[i])
        print(temp_list)
        result_list.append(list(temp_list))
        temp_list.clear()
print(result_list)
