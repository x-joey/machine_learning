gram_list=list()
origin_data=list()
temp_list=list()
acid_types = list()
acid_types_one = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'O']
acid_types_two = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'O']
#生成任意两个搭配的字符串
for i in range(0,len(acid_types_one)):
    for j in range(0,len(acid_types_two)):
        acid_types.append(acid_types_one[i]+acid_types_two[j])
print(acid_types)
#读取文件中氨基酸序列
with open('test.txt','r') as reader:
    while (reader.readline() != ''):
        data = reader.readline().strip('\n')  #GLSLNDRKKLLAKDLRGEMTLPATD
        #print(data)
        squ = [i for i in data]
        print(squ)
        for k in range(0,len(data)):
            if(k<24):
                origin_data.append(squ[k]+squ[k+1])
        print(origin_data)
        for type in acid_types:
            num = 0
            for i in origin_data:
                if(i == type):
                    num +=1
            frs = num/24
            temp_list.append(frs)
        del origin_data[:]  #把前面生成两个字符删掉，因为已经计算完了
        gram_list.append(list(temp_list))
    print(gram_list)