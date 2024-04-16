import os
from sklearn.model_selection import KFold
from itertools import zip_longest
import numpy as np
import csv

file_path = './process_list_autogen.csv'
split_file_path = './split_result'
if not os.path.exists(split_file_path):
    os.makedirs(split_file_path)
data_list = []

with open(file_path) as f:
    data = csv.reader(f)
    for case in data:
        data_list.append(case[0].split('.')[0])
    f.close()
    data_list = data_list[1:]

kf = KFold(n_splits=5, shuffle=True)
i = 0
for train_indexs, test_indexs in kf.split(data_list):
    train_case_list = []
    test_case_list = []
    for train_index in train_indexs:
        train_case_list.append(data_list[train_index])
    for test_index in test_indexs:
        test_case_list.append(data_list[test_index])
    rows = zip_longest(train_case_list, test_case_list)
    split_fold_path = os.path.join(split_file_path, 'fold_'+str(i)+'.csv')
    header = ['train', 'val']
    with open(split_file_path, 'a', newline='') as file:
        result = csv.writer(file)
        result.writerow(header)
        for row in rows:
            result.writerow(row)
        i = i + 1


