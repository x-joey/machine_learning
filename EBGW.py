C1 = ['A', 'F', 'G', 'I', 'L', 'M', 'P', 'V', 'W']
C2 = ['C', 'N', 'Q', 'S', 'T', 'Y']
C3 = ['K', 'H', 'R']
C4 = ['D', 'E']
# H1 = C1+C2
# H2 = C1+C3
# H3 = C1+C4

H1 = ['A', 'F', 'G', 'I', 'L', 'M', 'P', 'V', 'W', 'C', 'N', 'Q', 'S', 'T', 'Y']
H2 = ['A', 'F', 'G', 'I', 'L', 'M', 'P', 'V', 'W', 'K', 'H', 'R']
H3 = ['A', 'F', 'G', 'I', 'L', 'M', 'P', 'V', 'W', 'D', 'E']


#存储S，通过比较文件中氨基酸序列和列表H的序列
S1 = list()
S2 = list()
S3 = list()
result_list_33 = list()         #最终一个氨基酸序列生成33维结果
result_list = list()            #读取所有氨基酸序列结果
# 生成25维S特征向量
# H是哪一个比较序列，如果氨基酸序列data的氨基酸在H，则是1，不在则是0
# data读取文件获得的氨基酸序列
def get_S_feature_25(H, data):
    S_temp_list = list()
    for i in data:
        flag = 0
        for j in H:
            if (i == j):
                flag = 1
                S_temp_list.append(1)
                break
        if flag == 0:
            S_temp_list.append(0)
    return S_temp_list

#通过公式对S生成11维向量
def get_X_feature_11(S):
    # L is 25 ; J  is 11

    res_X_list = list()         # 存储11维向量结果
    Dj_1_list = list()          # 小片段中1的个数
    Dj_list = list()            # 该长度内有什么数据
    len_Dj_list = list()        # len_Dj_list 获得的11段小片段的长度数值
    for j in range(1, 12):
        len_Dj_list.append(round(j * 25 / 11))

    # 通过长度截取S中11个片段,都是从头开始截取
    # Dj_list[0] = S1[0:len_Dj_list[0]]
    for i in range(0, 11):
        Dj_list.append(S[0:len_Dj_list[i]])

        # 在该小片段中算出1的个数
        temp = 0
        for j in Dj_list[i]:
            if j == 1:
                temp = temp + 1
        Dj_1_list.append(temp)

    for j in range(0, 11):
        res_X_list.append(Dj_1_list[j] / len_Dj_list[j] )

    return res_X_list


with open(r"test.txt",'r') as f:
    while (f.readline() !=  ''):
        data = f.readline().strip('\n')       # 去掉氨基酸序列行\n   GLSLNDRKKLLAKDLRGEMTLPATD

        #得到S1，2，3的25维向量
        S1 = get_S_feature_25(H1, data)
        reslut_list_1 = get_X_feature_11(S1)

        S2 = get_S_feature_25(H2, data)
        reslut_list_2 = get_X_feature_11(S2)

        S3 = get_S_feature_25(H3, data)
        reslut_list_3 = get_X_feature_11(S3)

        #拼接起来
        result_list_33 = reslut_list_1+reslut_list_2+reslut_list_3
        result_list.append(list(result_list_33))
        result_list_33.clear()

    print(result_list)


