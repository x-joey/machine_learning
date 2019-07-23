origin_data=list()
gram_list=list()
temp_list=list()#暂存一个片段
num =0
index=0
acid_types = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'O']
with open('test.txt','r') as reader:
    while (reader.readline() != ''):
        data = reader.readline().strip('\n')  #GLSLNDRKKLLAKDLRGEMTLPATD
        print(data)
        for type in acid_types:
            num = 0
            for i in data:
                if(i == type):
                    num +=1
            fr = num/25
            temp_list.append(fr)
        gram_list.append(list(temp_list))
    print(gram_list)