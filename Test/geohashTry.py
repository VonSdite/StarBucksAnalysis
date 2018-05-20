# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import geohash
import pandas as pd

if __name__ == '__main__':
    csv_file = pd.read_csv('../directory.csv')
    csv_file['Decode'] = csv_file.apply(lambda x:geohash.encode(x.Latitude, x.Longitude), axis=1)
    print(csv_file['Decode'].sort_values())
