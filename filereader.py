
def reader(path, num):
    """
    取f2:PROCEDUREEVENTS_MV_DATA_TABLE表的前num行,在path路径下创建f1
    表为病人使用药品的信息
    """
    with open(r'C:\Users\47050\Desktop\MIMIC\PRESCRIPTIONS.csv', 'wb') as f1:
        with open(path, 'rb') as f2:
            for i in range(num):
                f1.write(f2.readline())

path = r'D:\BaiduNetdiskDownload\MIMIC_III\MIMIC_III\PROCEDUREEVENTS_MV_DATA_TABLE.csv'
reader(path, 100000)