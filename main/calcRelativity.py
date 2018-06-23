# -*- coding: utf-8 -*-
# __Author__: Sdite, amyy4, JX-Soleil, hzgege
# __Email__ : a122691411@gmail.com

from fuzzywuzzy import process
import pandas as pd


def calcRelativity(csv_file, keyWord, data):
    csv_file_tmp = csv_file.fillna("").astype(str)
    data = [x[1] for x in process.extractWithoutOrder(keyWord, data)]
    data = pd.DataFrame({
        'Relativity': data
        }
    )
    return data
