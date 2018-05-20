# -*- coding: utf-8 -*-
# __Author__: Sdite, amyy4, JX-Soleil, hzgege
# __Email__ : a122691411@gmail.com

import time
import heapq
import pandas as pd
import sys
sys.path.append("../")
from calcDistance import calcDistance

import plotly.offline as py
from plotly.graph_objs import *

# 大顶堆求前k小
def topKHeap(A, k):
    res = []
    for elem in A:
        elem = -elem
        if len(res) < k:
            heapq.heappush(res, elem)
        else:
            topkSmall = res[0]
            if elem > topkSmall:
                heapq.heapreplace(res, elem)

    return list(map(lambda x: -x, res))

# 非递归实现
def qSelect(A, k):
    if len(A) < k:
        return A

    s = []
    res = []
    s.append(A)

    while s:
        B = s.pop()
        if not B:
            break
        pivot = B[0]
        left = [x for x in B[1:] if x < pivot] + [pivot]
        lLen = len(left)
        if lLen == k:
            res += left
        elif lLen > k:
            s.append(left)
        else:
            res += left
            k -= lLen
            right = [x for x in B[1:] if x >= pivot]
            s.append(right)

    return res

if __name__ == '__main__':
    # csv_file = pd.read_csv("../directory.csv")
    #
    # start = time.clock()
    # distance = csv_file.apply(
    #     lambda x: calcDistance(0, 0, x.Longitude, x.Latitude), axis=1)
    # end = time.clock()
    #
    # print('遍历计算点间距离时间: %fs' % (end - start))
    #
    # useTime = dict()
    # useTime['heap'] = []
    # useTime['qSelect'] = []
    # useTime['pandas_n'] = []
    # useTime['pandas_q'] = []
    # useTime['pandas_m'] = []
    # useTime['pandas_h'] = []
    #
    #
    # for k in range(1, 25601):
    #     start = time.clock()
    #     topKHeap(distance, k)
    #     end = time.clock()
    #     h = end - start
    #     useTime['heap'].append(h)
    #
    #
    #     start = time.clock()
    #     qSelect(list(distance), k)
    #     end = time.clock()
    #     q = end - start
    #     useTime['qSelect'].append(q)
    #
    #
    #     start = time.clock()
    #     distance.nsmallest(k)
    #     end = time.clock()
    #     n = end - start
    #     useTime['pandas_n'].append(n)
    #
    #     start = time.clock()
    #     distance.sort_values(kind='quicksort').head(k)
    #     end = time.clock()
    #     pq = end - start
    #     useTime['pandas_q'].append(pq)
    #
    #     start = time.clock()
    #     distance.sort_values(kind='mergesort').head(k)
    #     end = time.clock()
    #     pm = end - start
    #     useTime['pandas_m'].append(pm)
    #
    #     start = time.clock()
    #     distance.sort_values(kind='heapsort').head(k)
    #     end = time.clock()
    #     ph = end - start
    #     useTime['pandas_h'].append(ph)
    #
    #
    #
    #     print("k: %d 大顶堆: %.15fs  快速选择: %.15fs  pn: %.15fs pq: %.15fs ph: %.15fs ph: %.15fs"
    #           % (k, h, q, n, pq, pm, ph))
    #
    # import pickle
    # with open('tmp.pickle', 'wb') as f:
    #     pickle.dump(useTime, f)

    import pickle
    with open('tmp.pickle', 'rb') as f:
        useTime = pickle.load(f)
    #
    trace1 = Scatter(
        y=useTime['heap'],
        x=list(range(1, 25601)),
        name='大顶堆',
        mode='lines+markers'
    )
    trace2 = Scatter(
        y=useTime['qSelect'],
        x=list(range(1, 25601)),
        name='快速选择',
        mode='lines+markers'
    )
    trace3 = Scatter(
        y=useTime['pandas_n'],
        x=list(range(1, 25601)),
        name='pandas_nsmallest',
        mode='lines+markers'
    )

    trace4 = Scatter(
        y=useTime['pandas_q'],
        x=list(range(1, 25601)),
        name='pandas_quicksort',
        mode='lines+markers'
    )
    trace5 = Scatter(
        y=useTime['pandas_m'],
        x=list(range(1, 25601)),
        name='pandas_mergesort',
        mode='lines+markers'
    )
    trace6 = Scatter(
        y=useTime['pandas_h'],
        x=list(range(1, 25601)),
        name='pandas_heapsort',
        mode='lines+markers'
    )
    data = [trace1, trace2, trace3, trace4, trace5, trace6]

    py.plot(data, filename='../html/时间比较.html')