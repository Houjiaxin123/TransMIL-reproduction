from sklearn.model_selection import KFold
import numpy as np
import csv

file_path = 'F:/CAMELYON16/training/CLAM_SEG_20X/process_list_autogen.csv'
split_file_path = 'C:/Users/12sigma/PycharmProjects/pythonProject1/dataset_csv/camelyon16/split_result.csv'
data_list = []

with open(file_path) as f:
    data = csv.reader(f)
    for case in data:
        data_list.append(case[0].split('.')[0])
    f.close()
    data_list = data_list[1:]

kf = KFold(n_splits=5, shuffle=True)
for train_indexs, test_indexs in kf.split(data_list):
    train_case_list = []
    test_case_list = []
    for train_index in train_indexs:
        train_case_list.append(data_list[train_index])
    for test_index in test_indexs:
        test_case_list.append(data_list[test_index])
    with open(split_file_path, 'a') as file:
        result = csv.writer(file)
        result.writerow(train_case_list)
        result.writerow(test_case_list)