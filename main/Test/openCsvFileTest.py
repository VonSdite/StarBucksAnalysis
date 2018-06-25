# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import time
import pickle
import pandas as pd

if __name__ == '__main__':
    start = time.clock()
    csv_file = pd.read_csv('../directory.csv')
    end = time.clock()
    print('\t\t\t\t\t\t\t\t\t使用pandas打开csv的耗时:    ', end - start, 's')

    start = time.clock()
    with open('../config/directory.pickle', 'rb') as f:
        csv_file = pickle.load(f)
    end = time.clock()
    print('\t\t\t\t\t\t\t\t\t使用pickle缓存打开csv的耗时: ', end - start, 's')