# -*- coding: utf-8 -*-
# __Author__: Sdite, amyy4, JX-Soleil, hzgege
# __Email__ : a122691411@gmail.com

import pandas as pd
from calcDistance import calcDistance
from calcRelativity import calcRelativity

def findTopK(csv_file, longitude, latitude, topK):
    csv_file['Distance'] = csv_file.apply(
        lambda x: calcDistance(longitude, latitude, x.Longitude, x.Latitude),
        axis=1)

    return csv_file.nsmallest(topK, 'Distance')


def findTopKWithKeyWord(csv_file, longitude, latitude, topK, keyWord, data):
    csv_file['Distance'] = csv_file.apply(
        lambda x: calcDistance(longitude, latitude, x.Longitude, x.Latitude),
        axis=1)

    csv_file['Relativity'] = calcRelativity(csv_file, keyWord, data)
    return csv_file.sort_values(by=['Relativity', 'Distance']).head(topK)




