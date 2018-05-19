# -*- coding: utf-8 -*-
# __Author__: Sdite, amyy4, JX-Soleil, hzgege
# __Email__ : a122691411@gmail.com

import os
import pickle
import pandas as pd
from random import randint
import plotly.offline as py
from plotly.graph_objs import *
from PyQt5.QtCore import QUrl

from findTopK import findTopK
from findRange import findRange

mapbox_access_token = 'pk.eyJ1Ijoic2RpdGUiLCJhIjoiY2pmajloaWJxMGw2NjJ4dW1za2c2cDNkZiJ9.KNk-JYP0chw-NFPffGs0eg'


def drawBar(data, fileName="html/bar.html", title=''):
    dataDict = dict(data.value_counts())
    dataName = [key for key in dataDict]
    dataValues = [dataDict[key] for key in dataDict]

    layout = Layout(title=title)
    fig = dict(data=[Bar(x=dataName, y=dataValues)], layout=layout)
    py.plot(fig, filename=fileName, auto_open=False)


def drawPie(data, fileName="html/pie.html", title=''):
    dataDict = dict(data.value_counts())
    dataName = [key for key in dataDict]
    dataValues = [dataDict[key] for key in dataDict]

    layout = Layout(title=title)
    fig = dict(data=[Pie(labels=dataName, values=dataValues,
                         hoverinfo='label+percent', textinfo="none")],
               layout=layout)
    py.plot(fig, filename=fileName, auto_open=False)


def drawColorMaps(countryData, fileName="html/colorMap.html", title=''):
    with open('config/countryTwoLettersToThree.pickle', 'rb') as f:
        changeCountryCode = pickle.load(f)

    country_dict = dict(countryData.replace(
        set(countryData),
        [changeCountryCode[c] for c in set(countryData)]
    ).value_counts())

    country = [key for key in country_dict]
    values = [country_dict[key] for key in country_dict]

    data = [
        dict(
            type='choropleth',
            colorscale=[[0, "rgb(172, 10, 5)"],
                        [0.35, "rgb(190, 60, 40)"],
                        [0.5, "rgb(245, 100, 70)"],
                        [0.94, "rgb(245, 120, 90)"],
                        [0.95, "rgb(247, 137, 106)"],
                        [0.96, "rgb(247, 172, 144)"],
                        [0.97, "rgb(247, 205, 192)"],
                        [0.98, "rgb(247, 217, 210)"],
                        [0.99, "rgb(247, 225, 220)"],
                        [1, "rgb(220, 220, 220)"]],
            reversescale=True,
            autocolorscale=False,
            locations=country,
            locationmode="ISO-3",
            z=values,
        )
    ]

    layout = Layout(title=title,
                    autosize=True,
                    hovermode='closest',
                    mapbox=dict(accesstoken=mapbox_access_token,
                                bearing=0,
                                pitch=0,
                                zoom=1))
    fig = dict(data=data, layout=layout)
    py.plot(fig, validate=False, filename=fileName, auto_open=False)


def drawMap(csv_file, fileName="html/map.html", title=''):
    timeZoneDict = dict(csv_file['Timezone'].value_counts())

    def timeZoneToCount(timeZone):
        return timeZoneDict[timeZone]

    csv_file['TimeZoneCount'] = csv_file['Timezone'].map(timeZoneToCount)

    # 店铺基本信息
    def int64ToStr(count):
        return str(count)

    csv_file = csv_file.fillna('Not set')
    csv_file['info'] = "Store Number: " + csv_file["Store Number"] + "</br></br>" \
                       + "Store Name: " + csv_file["Store Name"] + "</br>" \
                       + "Street Address: " + csv_file["Street Address"] + "</br>" \
                       + "Postcode: " + csv_file["Postcode"] + "</br>" \
                       + "Phone Number: " + csv_file["Phone Number"] + "</br>" \
                       + "Timezone:" + csv_file['Timezone'] + "</br>" \
                       + "count:" + csv_file['TimeZoneCount'].map(int64ToStr)

    data = []
    data.append(Scattermapbox(
        lat=csv_file['Latitude'],
        lon=csv_file['Longitude'],
        mode='markers',
        marker=Marker(size=10, color=list(csv_file['TimeZoneCount']),
                      colorscale=[[0, "rgb(172, 10, 5)"],
                                  [0.35, "rgb(190, 60, 40)"],
                                  [0.5, "rgb(245, 100, 70)"],
                                  [0.97, "rgb(245, 131, 103)"],
                                  [0.98, "rgb(245, 150, 131)"],
                                  [0.99, "rgb(245, 171, 141)"],
                                  [1, "rgb(255, 186, 163)"]
                                  ],
                      reversescale=True,
                      showscale=True,
                      ),
        text=csv_file['info'],
        textposition='top left',
        hoverinfo='text',
    ))

    layout = Layout(
        title=title,
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0, zoom=1),
    )

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename=fileName, auto_open=False)


def drawTopKMap(csv_file, lon, lat, topK, keyWord, fileName="html/topKMap.html", title=''):
    if keyWord == "":
        topKInfo = findTopK(csv_file, lon, lat, topK)
    else:
        return

    topKInfo = topKInfo.fillna('Not set')  # 将空值设为Not set
    topKInfo['info'] = "Store Number: " + topKInfo["Store Number"] + "</br></br>" \
                       + "Store Name: " + topKInfo["Store Name"] + "</br>" \
                       + "Street Address: " + topKInfo["Street Address"] + "</br>" \
                       + "Postcode: " + topKInfo["Postcode"] + "</br>" \
                       + "Phone Number: " + topKInfo["Phone Number"] + "</br>"

    data = []
    data.append(Scattermapbox(
        lat=topKInfo['Latitude'],
        lon=topKInfo['Longitude'],
        mode='markers',
        marker=Marker(size=10, color='blue'),
        text=topKInfo['info'],
        textposition='top left',
        hoverinfo='text',
        name="topK点",
    ))

    data.append(Scattermapbox(
        lat=[lat],
        lon=[lon],
        mode='markers',
        marker=Marker(size=10, color='red'),
        text=["标记点</br></br>经度:%f  纬度: %f" % (lon, lat)],
        textposition='top left',
        hoverinfo='text',
        name="标记点",
    ))

    layout = Layout(
        title=title,
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0, zoom=1),
    )

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename=fileName, auto_open=False)


def drawRangeMap(csv_file, lon, lat, range, fileName="html/rangeMap.html", title=''):
    rangeInfo = findRange(csv_file, lon, lat, range)

    rangeInfo = rangeInfo.fillna('Not set')

    # 将数值强转成str,后续用于字符串拼接
    rangeInfo["Distance"] = [str(key) + "km" for key in rangeInfo["Distance"]]

    rangeInfo['info'] = "Store Number: " + rangeInfo["Store Number"] + "</br></br>" \
                        + "Store Name: " + rangeInfo["Store Name"] + "</br>" \
                        + "Street Address: " + rangeInfo["Street Address"] + "</br>" \
                        + "Postcode: " + rangeInfo["Postcode"] + "</br>" \
                        + "Phone Number: " + rangeInfo["Phone Number"] + "</br>" \
                        + "Distance: " + rangeInfo["Distance"] + "</br>"
    data = []
    data.append(Scattermapbox(
        lat=rangeInfo['Latitude'],
        lon=rangeInfo['Longitude'],
        mode='markers',
        marker=Marker(size=10, color='blue'),
        text=rangeInfo['info'],
        textposition='top left',
        hoverinfo='text',
        name="距离标记点 < range的点",
    ))

    data.append(Scattermapbox(
        lat=[lat],
        lon=[lon],
        mode='markers',
        marker=Marker(size=10, color='red'),
        text=["标记点</br></br>经度:%f  纬度: %f 半径: %f" % (lon, lat, range)],
        textposition='top left',
        hoverinfo='text',
        name="标记点",
    ))

    layout = Layout(
        title=title,
        showlegend=True,
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0, zoom=1),
    )

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename=fileName, auto_open=False)

if __name__ == '__main__':
    csv_file = pd.read_csv('directory.csv')
    drawRangeMap(csv_file, 113, 23, 50)
