import csv


def labevents_abnormal():
    """
    所有检查为abnormal的保存在一起
    """
    with open(r'C:\Users\47050\Desktop\data\ab_labevents.csv', 'w') as fout:
        fin = r'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\LABEVENTS_DATA_TABLE.csv'
        with open(fin, 'r') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                if row['FLAG'] == 'abnormal':
                    fout.write(row['ROW_ID'] + ',' + row['SUBJECT_ID'] + ',' + row['ITEMID'] + ',' +
                               row['VALUE'] + ',' + row['VALUENUM'] + ',' + row['VALUEUOM'] + ','+row['FLAG'])
                    fout.write('\n')
#                    print(row['ROW_ID'])
#                    print("\n")

def in_HADM(hadm_id):
    """
    判断是否在HADM_ID_EV表里
    """
    path = r'C:\Users\47050\Desktop\data\HADM_ID_EV.csv'
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if(row['HADM_ID']==hadm_id):
                return 1
            else:
                continue
        return 0

def labevents_filter():
    """
    对labevents_data_table的处理，HADM_ID为空的删除,in_HADM的删除
    保存的字段有：SUBJECT_ID、HADM_ID、ITEMID、CHARTTIME、VALUE、VALUENUM、VALUEUOM、FLAG
    是否可以每个HADM_ID代表一个新病人，删除SUBJECT_ID字段？
    """
    num = 0     #计数 看运行到哪了
    num_row = 0
    with open(r'C:\Users\47050\Desktop\data\labevents_filter.csv', 'w') as fout:
        fout.write('SUBJECT_ID,HADM_ID,ITEMID,CHARTTIME,VALUE,VALUENUM,VALUEUOM,FLAG\n')
        fin = r'C:\Users\47050\Desktop\data\labevents_empty_filter.csv'
        with open(fin, 'r') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                num_row = num_row + 1
                if(num_row%1000 == 0):
                    print(num_row)
                if(binary_search(row['HADM_ID']) == 1):
                    if not(num == 0):
                        fout.write('\n')
                    fout.write(row['SUBJECT_ID'] + ',' + row['HADM_ID'] + ',' + row['ITEMID'] + ',' + row['CHARTTIME']
                               + ',' + row['VALUE'] + ',' + row['VALUENUM'] + ',' + row['VALUEUOM'] + ','+row['FLAG'])
                    num = num+1

def hadm_id_EV():
    """
    ICD9_CODE 中E开头的为意外事故（车祸、割腕等）可以删除
    ICD9_CODE 中V开头的也删除
    将ICD9_CODE中以E或V开头的HADM_ID保存成新表
    之后可以对admissions表、diagnoses表、d_diagnoses表进行处理，
    """
    num = 0
    finpath = 'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\DIAGNOSES_ICD_DATA_TABLE.csv'
    foutpath = r'C:\Users\47050\Desktop\data\HADM_ID_EV.csv'
    with open(finpath, 'r') as fin:    #读diagnoses表
        with open(foutpath, 'w') as fout:
            fout.write('HADM_ID')
            fout.write("\n")
            reader = csv.DictReader(fin)
            for row in reader:
                if(row['ICD9_CODE'].startswith('E') or row['ICD9_CODE'].startswith('V')):
                    if(not(num == 0)):
                        fout.write('\n')
                    fout.write(row['HADM_ID'])
                    num = num + 1


def admission_filter():
    """
    在ICD9_filter1()中生成的csv文档中循环 更新admissions表
    admission表保留SUBJECT_ID,HADM_ID,ADMITTIME,DISCHTIME,ADMISSION_TYPE,DIAGNOSIS
    """
    num = 0
    fin_path = 'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\ADMISSIONS_DATA_TABLE.csv'
    fout_path = r'C:\Users\47050\Desktop\data\ADMISSIONS_ICD_filter.csv'
    with open(fout_path, 'w') as fout:
        fout.write('SUBJECT_ID,HADM_ID,ADMITTIME,DISCHTIME,ADMISSION_TYPE,DIAGNOSIS\n')
        with open(fin_path, 'r') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                if(in_HADM(row['HADM_ID']) == 0):
                    if(not(num == 0)):
                        fout.write('\n')
                    fout.write(row['SUBJECT_ID']+','+row['HADM_ID']+','+row['ADMITTIME']+',')
                    fout.write(row['DISCHTIME'] + ',' + row['ADMISSION_TYPE'] + ',' + row['DIAGNOSIS'])
                    num = num + 1
                    print(num)
                    print('\n')


def diagnoses_filter():
    """
    在ICD9_filter1()中生成的csv文档中循环 更新diagnoses_icd_data表
    diagnose表保留SUBJECT_ID	,HADM_ID,SEQ_NUM,ICD9_CODE
    """
    num = 0
    fin_path = 'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\DIAGNOSES_ICD_DATA_TABLE.csv'
    fout_path = r'C:\Users\47050\Desktop\data\DIAGNOSES_ICD_filter.csv'

    with open(fout_path, 'w') as fout:
        fout.write('SUBJECT_ID,HADM_ID,SEQ_NUM,ICD9_CODE\n')
        with open(fin_path, 'r') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                if(in_HADM(row['HADM_ID'])==0):
                    if(not(num == 0)):
                        fout.write('\n')
                    fout.write(row['SUBJECT_ID']+','+row['HADM_ID']+',')
                    fout.write(row['SEQ_NUM'] + ',' + row['ICD9_CODE'])
                    num = num + 1
                    print(num)
                    print('\n')

def count():
    num = 0
    fin_path = r'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\LABEVENTS_DATA_TABLE.csv'
    with open(fin_path, 'r') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            num = num + 1
    print(num)


def empty_filter():
    """
    把labevents表中没有住院号的删掉
    """
    num = 0     #计数 看运行到哪了
    with open(r'C:\Users\47050\Desktop\data\labevents_empty_filter.csv', 'w') as fout:
        fout.write('SUBJECT_ID,HADM_ID,ITEMID,CHARTTIME,VALUE，VALUENUM，VALUEUOM,FLAG\n')
        fin = r'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\LABEVENTS_DATA_TABLE.csv'
        with open(fin, 'r') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                if not(len(row['HADM_ID']) == 0):
                    if not(num == 0):
                        fout.write('\n')
                    fout.write(row['SUBJECT_ID'] + ',' + row['HADM_ID'] + ',' + row['ITEMID'] + ',' + row['CHARTTIME']
                               + ',' + row['VALUE'] + ',' + row['VALUENUM'] + ',' + row['VALUEUOM'] + ','+row['FLAG'])
                    num = num+1
                    if(num % 1000000 == 0):
                        print(num)



def hadm_id_notEV():
    """
    遍历admission_filter表 把ham_id保存
    """
    num = 0
    finpath = r'C:\Users\47050\Desktop\data\ADMISSIONS_ICD_filter.csv'
    foutpath = r'C:\Users\47050\Desktop\data\HADM_ID_notEV.csv'
    with open(finpath, 'r') as fin:
        with open(foutpath, 'w') as fout:
            fout.write('HADM_ID\n')
            reader = csv.DictReader(fin)
            for row in reader:
                if not(num == 0):
                    fout.write('\n')
                fout.write(row['HADM_ID'])
                num = num + 1

def binary_search(data):
    """
    二分查找
    """
    #转化成list
    search_path = r'C:\Users\47050\Desktop\data\HADM_ID_notEV.csv'
    with open(search_path, 'r') as search_file:
        search_reader = csv.reader(search_file)
        search_list = list(search_reader)
    n = len(search_list)
    first = 0
    last = n-1
    while(first <= last):
        mid = (first + last) // 2   #向下取整
        if(" ".join(search_list[mid])> data):
            last = mid - 1
        elif(" ".join(search_list[mid]) < data):
            first = mid + 1
        else:
            return 1
    return 0


#count()
#empty_filter()
#hadm_id_notEV()

#labevents_abnormal()
#hadm_id_EV()
labevents_filter()





