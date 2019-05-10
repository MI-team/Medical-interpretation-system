import csv


def hadmid_filter():
    """
    根据体检项目筛选的病人HADM_ID，不重复
    """

    files = [r'C:\Users\47050\Desktop\data\labevents_blood_filter.csv',
             r'C:\Users\47050\Desktop\data\labevents_coagulation_filter.csv',
             r'C:\Users\47050\Desktop\data\labevents_urine_filter.csv',
             r'C:\Users\47050\Desktop\data\labevents_biochem_filter.csv',
             r'C:\Users\47050\Desktop\data\labevents_liver_filter.csv',
             r'C:\Users\47050\Desktop\data\labevents_bloodfat_filter.csv',
             r'C:\Users\47050\Desktop\data\labevents_hepaB_filter.csv',
             r'C:\Users\47050\Desktop\data\labevents_thyroid_filter.csv',
             r'C:\Users\47050\Desktop\data\labevents_renal_filter.csv',
             r'C:\Users\47050\Desktop\data\labevents_tumour_filter.csv']
    fout_path = r'C:\Users\47050\Desktop\data\hadmID_filter.csv'
    tempid = 'null'
    num = 0
    with open(fout_path, 'w+') as fout:
        fout.write('HADM_ID\n')
        writer = csv.DictReader(fout)
        for file in files:
            print(file)
            with open(file, 'r') as fin:
                reader = csv.DictReader(fin)
                for row in reader:
                    if(row['HADM_ID'] == tempid):
                        continue
                    for row2 in writer:     #如果文件里已经写过
                        if(row['HADM_ID'] == row2['HADM_ID']):
                            tempid = row['HADM_ID']
                            break
                    else:
                        if not(num == 0):
                            fout.write('\n')
                        fout.write(row['HADM_ID'])
                        tempid = row['HADM_ID']
                        num = num + 1

hadmid_filter()
