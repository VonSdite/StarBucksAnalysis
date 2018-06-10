# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com
from geohash.geohash import encode, decode
import pickle

if __name__ == '__main__':
    # with open("config/directory.pickle", "rb") as f:
    #     csv_file = pickle.load(f)
    #
    # help(geohash.geohash)

    hashList = []

    for lat in range(0, 91):
        for lon in range(0, 181):
            hashList.append(encode(lat, lon))

    hashList.sort()
    for ele in hashList:
        print(ele, decode(ele))
        input()
