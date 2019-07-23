'''
我的思路是什么
1.从文件序列中得到的氨基酸在原始序列中比较
2.如果在的话，取原始序列的下标，
3.然后在字符串中的相应位置把值置为1
4.难点是在字符串特定位置换值，取字符下标
'''
acid_types = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'O']
# temp = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
temp_list = list()
result_list = list()
with open('test.txt','r') as reader:
    while (reader.readline() != ''):
        data = reader.readline().strip('\n')
        print(data)

        for i in data:
            temp = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
            for type in acid_types:
                if(i == type):
                    index_num = acid_types.index(type)
                    temp[index_num] = '1'
                    temp_list += temp
        result_list.append(list(temp_list))
        temp_list.clear()
    print(result_list)