# -*- coding: utf-8 -*-
# __Author__: Sdite, amyy4, JX-Soleil, hzgege
# __Email__ : a122691411@gmail.com

from calcDistance import calcDistance

def findRange(csv_file, longitude, latitude, range):
    csv_file['Distance'] = csv_file.apply(
        lambda x:calcDistance(longitude, latitude, x.Longitude, x.Latitude),
                              axis=1)

    return csv_file[csv_file['Distance'] <= range]