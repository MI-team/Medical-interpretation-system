import csv
import pymongo

#连接数据库mimic
conn = pymongo.MongoClient()
db = conn.mimic

#def filter()



def insertdata(table, path, col_name):
    print(table)
    print("\n")
    table.remove()
    with open(path, 'r') as f:
        #按行读取，返回迭代对象
        reader = csv.DictReader(f)
        for row in reader:
            for col in col_name:
                #向数据库中插入数据
                table.insert_one({col: row[col]})


#调用函数将数据插入数据库
#diag_icd 主要使用病人ID和ICD9_CODE SEQ_NUM(疾病的顺序？需要吗)
diag_icd = db.DIAGNOSES_ICD
path = 'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\DIAGNOSES_ICD_DATA_TABLE.csv'
col_ls = ['ROW_ID', 'SUBJECT_ID', 'ICD9_CODE']
insertdata(diag_icd, path, col_ls)

#d_icd 要与diag_icd相连，解释ICD9_CODE
d_icd = db.D_ICD_DIAGNOSES
path = 'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\D_ICD_DIAGNOSES_DATA_TABLE.csv'
col_ls = ['ROW_ID', 'ICD9_CODE', 'SHORT_TITLE', 'LONG_TITLE']
insertdata(d_icd, path, col_ls)

#items
d_items = db.D_ITEMS
path = 'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\D_ITEMS_DATA_TABLE.csv'
col_ls = ['ROW_ID', 'ITEMID', 'LABEL', 'CATEGORY']
insertdata(d_items, path, col_ls)

#d_labitems 与labevents对应
#ITEMID 检查项目编码
#FLUID描述检测的液体是什么，血液/尿液/...
#CATEGORY 方式 血液/物理/注射...
#LOINC_CODE是检查项目的标准编码
d_labitems = db.D_LABITEMS
path = 'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\D_LABITEMS_DATA_TABLE.csv'
col_ls = ['ROW_ID', 'ITEMID', 'LABEL', 'FLUID', 'CATEGORY', 'LOINC_CODE']
insertdata(d_labitems, path, col_ls)

#通过SUBJECT_ID与PATIENTS表关联
#通过HADM_ID与ADMISSIONS表关联
#通过ITEMID与D_LABITEMS表关联
labevents = db.LABEVENTS
path = 'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\LABEVENTS_DATA_TABLE.csv'
col_ls = ['ROW_ID', 'SUBJECT_ID', 'ITEMID', 'VALUE', 'VALUENUM', 'VALUEUOM', 'FLAG']
insertdata(labevents, path, col_ls)


patients = db.PATIENTS
path = 'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\PATIENTS_DATA_TABLE.csv'
col_ls = ['ROW_ID', 'SUBJECT_ID', 'GENDER']
insertdata(patients, path, col_ls)

#没有CHARTEVENTS_DATA_TABLE、NOTEEVENTS_DATA_TABLE、DRGCODES_DATA_TABLE
#LABEVENTS_DATA之前的import完毕了



