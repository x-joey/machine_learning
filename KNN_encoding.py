'''
目标：实现KNN编码
思路：
1.存入200正样本，200负样本
2.
3.根据公式计算距离，这里可用2个公式
4.排序这些距离，然后得到前K个
5.判断前K个中正样本有多少个
6.然后的在前K个中正样本的百分比作为向量

排序之后怎么知道哪些值属于正样本，万一值重复怎么办
'''
BLOSUM62 = {'AA': 4, 'RA': 1, 'AR': 1, 'RR': 5, 'NA': -2, 'AN': -2, 'NR': 0, 'RN': 0, 'NN': 6, 'DA': -2, 'AD': -2,
            'DR': -2, 'RD': -2, 'DN': 1, 'ND': 1, 'DD': 6, 'CA': 0, 'AC': 0, 'CR': -3, 'RC': -3, 'CN': -3, 'NC': -3,
            'CD': -3, 'DC': -3, 'CC': 9, 'QA': -1, 'AQ': -1, 'QR': 1, 'RQ': 1, 'QN': 0, 'NQ': 0, 'QD': 0, 'DQ': 0,
            'QC': -3, 'CQ': -3, 'QQ': 5, 'EA': -1, 'AE': -1, 'ER': 0, 'RE': 0, 'EN': 0, 'NE': 0, 'ED': 2, 'DE': 2,
            'EC': -4, 'CE': -4, 'EQ': 2, 'QE': 2, 'EE': 5, 'GA': 0, 'AG': 0, 'GR': -2, 'RG': -2, 'GN': 0, 'NG': 0,
            'GD': -1, 'DG': -1, 'GC': -3, 'CG': -3, 'GQ': -2, 'QG': -2, 'GE': -2, 'EG': -2, 'GG': 6, 'HA': -2, 'AH': -2,
            'HR': 0, 'RH': 0, 'HN': 1, 'NH': 1, 'HD': -1, 'DH': -1, 'HC': -3, 'CH': -3, 'HQ': 0, 'QH': 0,
            'HE': 0, 'EH': 0, 'HG': -2, 'GH': -2, 'HH': 8, 'IA': -1, 'AI': -1, 'IR': -3, 'RI': -3, 'IN': -3, 'NI': -3,
            'ID': -3, 'DI': -3, 'IC': -1, 'CI': -1, 'IQ': -3, 'QI': -3, 'IE': -3, 'EI': -3, 'IG': -4, 'GI': -4,
            'IH': -3, 'HI': -3, 'II': 4, 'LA': -1, 'AL': -1, 'LR': -2, 'RL': -2, 'LN': -3, 'NL': -3, 'LD': -4, 'DL': -4,
            'LC': -1, 'CL': -1, 'LQ': -2, 'QL': -2, 'LE': -3, 'EL': -3, 'LG': -4, 'GL': -4, 'LH': -3, 'HL': -3,
            'LI': 2, 'IL': 2, 'LL': 4, 'KA': -1, 'AK': -1, 'KR': 2, 'RK': 2, 'KN': 0, 'NK': 0, 'KD': -1, 'DK': -1,
            'KC': -3, 'CK': -3, 'KQ': 1, 'QK': 1, 'KE': 1, 'EK': 1, 'KG': -2, 'GK': -2, 'KH': -1, 'HK': -1,
            'KI': -3, 'IK': -3, 'KL': -2, 'LK': -2, 'KK': 5, 'MA': -1, 'AM': -1, 'MR': -1, 'RM': -1, 'MN': -2, 'NM': -2,
            'MD': -3, 'DM': -3, 'MC': -1, 'CM': -1, 'MQ': 0, 'QM': 0, 'ME': -2, 'EM': -2, 'MG': -3, 'GM': -3,
            'MH': -2, 'HM': -2, 'MI': 1, 'IM': 1, 'ML': 2, 'LM': 2, 'MK': -1, 'KM': -1, 'MM': 5, 'FA': -2, 'AF': -2,
            'FR': -3, 'RF': -3, 'FN': -3, 'NF': -3, 'FD': -3, 'DF': -3, 'FC': -2, 'CF': -2, 'FQ': -3, 'QF': -3,
            'FE': -3, 'EF': -3, 'FG': -3, 'GF': -3, 'FH': -1, 'HF': -1, 'FI': 0, 'IF': 0, 'FL': 0, 'LF': 0,
            'FK': -3, 'KF': -3, 'FM': 0, 'MF': 0, 'FF': 6, 'PA': -1, 'AP': -1, 'PR': -2, 'RP': -2, 'PN': -2, 'NP': -2,
            'PD': -1, 'DP': -1, 'PC': -3, 'CP': -3, 'PQ': -1, 'QP': -1, 'PE': -1, 'EP': -1, 'PG': -2, 'GP': -2,
            'PH': -2, 'HP': -2, 'PI': -3, 'IP': -3, 'PL': -3, 'LP': -3, 'PK': -1, 'KP': -1, 'PM': -2, 'MP': -2,
            'PF': -4, 'FP': -4, 'PP': 7, 'SA': 1, 'AS': 1, 'SR': -1, 'RS': -1, 'SN': 1, 'NS': 1, 'SD': 0, 'DS': 0,
            'SC': -1, 'CS': -1, 'SQ': 0, 'QS': 0, 'SE': 0, 'ES': 0, 'SG': 0, 'GS': 0, 'SH': -1, 'HS': -1,
            'SI': -2, 'IS': -2, 'SL': -2, 'LS': -2, 'SK': 0, 'KS': 0, 'SM': -1, 'MS': -1, 'SF': -2, 'FS': -2,
            'SP': -1, 'PS': -1, 'SS': 4, 'TA': 0, 'AT': 0, 'TR': -1, 'RT': -1, 'TN': 0, 'NT': 0, 'TD': -1, 'DT': -1,
            'TC': -1, 'CT': -1, 'TQ': -1, 'QT': -1, 'TE': -1, 'ET': -1, 'TG': -2, 'GT': -2, 'TH': -2, 'HT': -2,
            'TI': -1, 'IT': -1, 'TL': -1, 'LT': -1, 'TK': -1, 'KT': -1, 'TM': -1, 'MT': -1, 'TF': -2, 'FT': -2,
            'TP': -1, 'PT': -1, 'TS': 1, 'ST': 1, 'TT': 5, 'WA': -3, 'AW': -3, 'WR': -3, 'RW': -3, 'WN': -4, 'NW': -4,
            'WD': -4, 'DW': -4, 'WC': -2, 'CW': -2, 'WQ': -2, 'QW': -2, 'WE': -3, 'EW': -3, 'WG': -2, 'GW': -2,
            'WH': -2, 'HW': -2, 'WI': -3, 'IW': -3, 'WL': -2, 'LW': -2, 'WK': -3, 'KW': -3, 'WM': -1, 'MW': -1,
            'WF': 1, 'FW': 1, 'WP': -4, 'PW': -4, 'WS': -3, 'SW': -3, 'WT': -2, 'TW': -2, 'WW': 11, 'YA': -2, 'AY': -2,
            'YR': -2, 'RY': -2, 'YN': -2, 'NY': -2, 'YD': -3, 'DY': -3, 'YC': -2, 'CY': -2, 'YQ': -1, 'QY': -1,
            'YE': -2, 'EY': -2, 'YG': -3, 'GY': -3, 'YH': 2, 'HY': 2, 'YI': -1, 'IY': -1, 'YL': -1, 'LY': -1,
            'YK': -2, 'KY': -2, 'YM': -1, 'MY': -1, 'YF': 3, 'FY': 3, 'YP': -3, 'PY': -3, 'YS': -2, 'SY': -2,
            'YT': -2, 'TY': -2, 'YW': 2, 'WY': 2, 'YY': 7, 'VA': 0, 'AV': 0, 'VR': -3, 'RV': -3, 'VN': -3, 'NV': -3,
            'VD': -3, 'DV': -3, 'VC': -1, 'CV': -1, 'VQ': -2, 'QV': -2, 'VE': -2, 'EV': -2, 'VG': -3, 'GV': -3,
            'VH': -3, 'HV': -3, 'VI': 3, 'IV': 3, 'VL': 1, 'LV': 1, 'VK': -2, 'KV': -2, 'VM': 1, 'MV': 1,
            'VF': -1, 'FV': -1, 'VP': -2, 'PV': -2, 'VS': -2, 'SV': -2, 'VT': 0, 'TV': 0, 'VW': -3, 'WV': -3,
            'VY': -1, 'YV': -1, 'VV': 4, 'OA': -4, 'AO': -4, 'OR': -4, 'RO': -4, 'ON': -4, 'NO': -4, 'OD': -4, 'DO': -4,
            'OC': -4, 'CO': -4, 'OQ': -4, 'QO': -4, 'OE': -4, 'EO': -4, 'OG': -4, 'GO': -4, 'OH': -4, 'HO': -4,
            'OI': -4, 'IO': -4, 'OL': -4, 'LO': -4, 'OK': -4, 'KO': -4, 'OM': -4, 'MO': -4, 'OF': -4, 'FO': -4,
            'OP': -4, 'PO': -4, 'OS': -4, 'SO': -4, 'OT': -4, 'TO': -4, 'OW': -4, 'WO': -4, 'OY': -4, 'YO': -4,
            'OV': -4, 'VO': -4, 'OO': 1}


distance_temp = list()                  # 每个序列通过公式算出来的距离列表
result_list = list()                    # 最后结果列表
score_temp_list = list()                # 每个序列获得的分数列表
positvie_sample = list()                # 截取正样本列表


def GetSample(filename):

    '''
    读取200个样本,运行两次该函数，因为有正负两个样本
    :param filename:文件路径和文件名
    :return:data_list是读取文件后的一维数组
    '''

    data_list = list()
    with open(filename) as f:
        while (f.readline() != ''):
            data_list.append(f.readline().strip('\n'))
    return data_list

def Sim(a, b):

    '''
    计算相似性，根据公式写就行,在这里通过BLOSUM62矩阵获取相似性
    :param a: 氨基酸
    :param b: 氨基酸
    :return: 返回相似性分数
    '''

    max_num = max(BLOSUM62.values())                    # 矩阵最大值
    min_num = min(BLOSUM62.values())                    # 矩阵最小值
    distance = 0
    if a+b in BLOSUM62:
        distance = BLOSUM62[a+b]                        # 通过键值对获取值
    result = (distance - min_num)/(max_num - min_num)   # 公式
    return result

def dist(s1, s2):
    '''
    计算距离，公式
    :param s1:
    :param s2:
    :return:
    '''
    sim_sum = 0
    for i in range(0, 25):
        sim_sum += Sim(s1[i], s2[i])

    Dist = 1 - sim_sum/25
    return Dist


filename1 = 'positive2.txt'         # 调用读取正负样本文件
filename2 = 'negative2.txt'
s1 = GetSample(filename1)           # 一维数组，200个25长度的序列
s2 = GetSample(filename2)
s3 = s1 + s2                        # 读取正负样本文件并拼接

NUM = 10                            # 表示样本总数，这里测试所以是10
k_account = 4                        # 控制k有多少个，这里k取三个，分别为2，4，8

for i in range(0, NUM):                                 # 控制对每个样本的遍历
    for j in range(0, NUM):                             # 控制一个样本跟每个样本都比较
        distance_temp.append(dist(s3[i], s3[j]))        # 样本和正样本,每个序列与其他有399个距离

    positvie_sample = distance_temp[0:int(NUM/2)]       # 获取正样本，因为前半部分是，所以切片可得
    temp = positvie_sample.copy()                       # 将值赋值给中间变量temp，方便下面对正样本的还原
    distance_temp.sort()                                # 排序方便获得K最邻近的距离

    for p in range(1, k_account):                       # 控制每个序列生成多少维向量，即K有多少个
        k = pow(2, p)                                   # 获取K最邻近的值，为2的p次方
        temp_k_list = distance_temp[0:k]                # 排序后的距离切片前k个
        positvie_sample = temp.copy()                   # 对删除值后的正样本距离列表进行还原（由于下面每次发现K邻近中有该距离在正样本中就flag+1，然后正样本距离列表就把该值删除）
        flag = 0
        for n in temp_k_list:                           # 得到K邻近中有多少个正样本数据
            for m in positvie_sample:
                if n == m:
                    flag = flag + 1
                    positvie_sample.remove(m)

        score_temp_list.append(flag/k)                  # 算正样本占K多少
    result_list.append(list(score_temp_list))           # 最终结果
    score_temp_list.clear()
    distance_temp.clear()
print(result_list)

