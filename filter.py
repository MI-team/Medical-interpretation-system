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


def labevents_filter():
    """
    对labevents_data_table的处理，HADM_ID为空的删除，因为诊断都是对住院病人进行的诊断
    保存的字段有：SUBJECT_ID、HADM_ID、ITEMID、CHARTTIME、VALUE、VALUENUM、VALUEUOM、FLAG
    是否可以每个HADM_ID代表一个新病人，删除SUBJECT_ID字段？
    """
    with open(r'C:\Users\47050\Desktop\data\labevents_filter.csv', 'w') as fout:
        fout.write('SUBJECT_ID' + ',' + 'HADM_ID' + ',' + 'ITEMID' + ',' + 'CHARTTIME' + ','
                   + 'VALUE' + ',' + 'VALUENUM' + ',' + 'VALUEUOM,FLAG' + '\n')
        fin = r'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\LABEVENTS_DATA_TABLE.csv'
        with open(fin, 'r') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                if not(len(row['HADM_ID']) == 0):
                    fout.write(row['SUBJECT_ID'] + ',' + row['HADM_ID'] + ',' + row['ITEMID'] + ',' + row['CHARTTIME']
                               + ',' + row['VALUE'] + ',' + row['VALUENUM'] + ',' + row['VALUEUOM'] + ','+row['FLAG'])
                    fout.write('\n')
#                    print(row['ROW_ID'])
#                    print("\n")


def diagnoses_icd_filter():
    """
    三个表可以一起删
    ICD9_CODE 中E开头的为意外事故（车祸、割腕等）可以删除
    之后可以对admissions表中 每个HAMD_ID去diagnoses_icd_data表中找，
    若ICD_CODE不是以E或V开头（即是数字）则保存到新表
    """



#labevents_abnormal()
#labevents_filter()





