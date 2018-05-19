# -*- coding: utf-8 -*-
# __Author__: Sdite, amyy4, JX-Soleil, hzgege
# __Email__ : a122691411@gmail.com

import pandas as pd
from calcDistance import calcDistance
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def findTopK(csv_file, longitude, latitude, topK):
    csv_file['Distance'] = csv_file.apply(
        lambda x:calcDistance(longitude, latitude, x.Longitude, x.Latitude),
                              axis=1)

    return csv_file.nsmallest(topK, 'Distance')

def findTopKWithKeyWord(csv_file, longitude, latitude, topK, keyWord):
    csv_file['Distance'] = csv_file.apply(
            lambda x:calcDistance(longitude, latitude, x.Longitude, x.Latitude),
                                  axis=1)


if __name__ == '__main__':
    # csv_file = pd.read_csv("directory.csv")
    # findTopKWithKeyWord(csv_file, 113, 23, 50, "广州")

    print(fuzz.ratio("113 23", "23 113"))
    print(fuzz.ratio("113 23", "23 113"))
    print(fuzz.ratio("东莞", "广东"))
    print(fuzz.partial_ratio("美国", "加利福利亚"))
    print(fuzz.ratio("美国", "中国"))







