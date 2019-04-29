import csv
import pandas as pd


filename1 = r"C:\Users\47050\Desktop\Medical-interpretation-system\LABEVENTS_DATA_TABLE.csv"
filename2 = r"C:\Users\47050\Desktop\Medical-interpretation-system\D_LABITEMS_DATA_TABLE.csv"
file1 = pd.read_csv(filename1, header=0)
file2 = pd.read_csv(filename2, header=0)

# 以ITEMID为重叠的列名合并两个表
data = pd.merge(file1, file2, on='ITEMID')
data.to_csv(r"C:\Users\47050\Desktop\Medical-interpretation-system\main_data.csv")





