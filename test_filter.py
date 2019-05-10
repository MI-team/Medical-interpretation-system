import csv

def labevents_filter(path,list):
    num = 0
    fin_path = r'C:\Users\47050\Desktop\data\labevents_empty_filter.csv'
    fout_path = path
    with open(fout_path, 'w') as fout:
        fout.write('SUBJECT_ID,HADM_ID,ITEMID,CHARTTIME,VALUE,VALUENUM,VALUEUOM,FLAG\n')
        with open(fin_path, 'r') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                for i in list:
                    if(int(row['ITEMID']) == i):
                        if not(num == 0):
                            fout.write('\n')
                        fout.write(row['SUBJECT_ID'] + ',' + row['HADM_ID'] + ',' + row['ITEMID'] + ',' +
                                   row['CHARTTIME'] + ',' + row['VALUE'] + ',' + row['VALUENUM'] + ',' +
                                   row['VALUEUOM'] + ',' + row['FLAG'])
                        num = num + 1


#血常规
blood_filter_path = r'C:\Users\47050\Desktop\data\labevents_blood_filter.csv'
blood_item_id = [51133, 51146, 51200, 51221, 51222, 51244, 51248, 51249, 51250,
                 51254, 51254, 51256, 51265, 51277, 51279, 51284, 51301]
labevents_filter(blood_filter_path, blood_item_id)

#凝血功能
coagulation_filter_path = r'C:\Users\47050\Desktop\data\labevents_coagulation_filter.csv'
coagulation_item_id = [51274, 51297, 51214, 51275]
labevents_filter(coagulation_filter_path, coagulation_item_id)

#尿常规
labevents_urine_filter_path = r'C:\Users\47050\Desktop\data\labevents_urine_filter.csv'
urine_item_id = [51492, 51478, 51486, 51484, 51514, 51464, 51498, 51491, 51487, 51466]
labevents_filter(labevents_urine_filter_path,urine_item_id)

# #血生化
biochem_filter_path = r'C:\Users\47050\Desktop\data\labevents_biochem_filter.csv'
biochem_item_id = [50861, 50912, 51006, 50931, 51000, 50907]
labevents_filter(biochem_filter_path, biochem_item_id)

#肝功能
liver_filter_path = r'C:\Users\47050\Desktop\data\labevents_liver_filter.csv'
liver_item_id = [50861, 50878, 50863, 50927, 50885, 50883, 50976, 50862, 50930, 50884]
labevents_filter(liver_filter_path, liver_item_id)

#血脂
bloodfat_filter_path = r'C:\Users\47050\Desktop\data\labevents_bloodfat_filter.csv'
bloodfat_item_id = [51000, 50907]
labevents_filter(bloodfat_filter_path, bloodfat_item_id)

#乙肝
hepaB_filter_path = r'C:\Users\47050\Desktop\data\labevents_hepaB_filter.csv'
hepaB_item_id = [50941, 50940, 50942]
labevents_filter(hepaB_filter_path, hepaB_item_id)

#甲功检查
thyroid_filter_path = r'C:\Users\47050\Desktop\data\labevents_thyroid_filter.csv'
thyroid_item_id = [51001, 50994, 50995, 50993]
labevents_filter(thyroid_filter_path, thyroid_item_id)

#肾功能检查
renal_filter_path = r'C:\Users\47050\Desktop\data\labevents_renal_filter.csv'
renal_item_id = [51006, 50912, 51007, 51492, 51069, 50881]
labevents_filter(renal_filter_path, renal_item_id)

#肿瘤标志物检查
tumour_filter_path = r'C:\Users\47050\Desktop\data\labevents_tumour_filter.csv'
tumour_item_id = [50864, 50900, 50892, 50974, 50946, 50858, 50898]
labevents_filter(tumour_filter_path, tumour_item_id)
