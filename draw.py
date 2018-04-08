# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import os
import pickle
import pandas as pd
from random import randint
import plotly.offline as py
from plotly.graph_objs import *

mapbox_access_token = 'pk.eyJ1Ijoic2RpdGUiLCJhIjoiY2pmajloaWJxMGw2NjJ4dW1za2c2cDNkZiJ9.KNk-JYP0chw-NFPffGs0eg'

def drawBar(data, fileName="html/bar.html", title=''):
    dataDict = dict(data.value_counts())
    dataName = [key for key in dataDict]
    dataValues = [dataDict[key] for key in dataDict]

    layout = Layout(title=title)
    fig = dict(data=[Bar(x=dataName, y=dataValues)], layout=layout)
    py.plot(fig, filename=fileName)

def drawPie(data, fileName="html/pie.html", title=''):
    dataDict = dict(data.value_counts())
    dataName = [key for key in dataDict]
    dataValues = [dataDict[key] for key in dataDict]

    layout = Layout(title=title)
    fig = dict(data=[Pie(labels=dataName, values=dataValues,
               hoverinfo='label+percent', textinfo="none")],
               layout=layout)
    py.plot(fig, filename=fileName)

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
    py.plot(fig, validate=False, filename=fileName)

def drawMap(csv_file, fileName="html/map.html", title=''):
    # 店铺基本信息
    csv_file['info'] = "Store Number: " + csv_file["Store Number"] + "</br></br>" \
                       + "Store Name: " + csv_file["Store Name"] + "</br>" \
                       + "Street Address: " + csv_file["Street Address"] + "</br>" \
                       + "Postcode: " + csv_file["Postcode"] + "</br>" \
                       + "Phone Number: " + csv_file["Phone Number"]

    # 根据不同时区设置颜色点
    timeZoneSet = set(csv_file["Timezone"])
    # if not os.path.isfile('config/colorMap.pickle'):
    timeZoneColorMap = dict()
    colorVis = []
    for timeZone in timeZoneSet:
        color = 'rgb(%d, %d, %d)' \
                % (randint(0, 255), randint(0, 255), randint(0, 255))
        if color not in colorVis:
            timeZoneColorMap[timeZone] = color
            colorVis.append(color)
        # with open('config/colorMap.pickle', 'wb') as f:
            # pickle.dump(timeZoneColorMap, f)
    del colorVis
    # else:
        # with open('config/colorMap.pickle', 'rb') as f:
            # timeZoneColorMap = pickle.load(f)

    data = []
    dataGroups = csv_file.groupby("Timezone")
    for timeZone in timeZoneSet:
        group = dataGroups.get_group(timeZone)
        data.append(Scattermapbox(
            lat=group["Latitude"],
            lon=group["Longitude"],
            mode='markers',
            marker=Marker(size=6, color=timeZoneColorMap[timeZone]),
            text=group["info"],
            textposition="top left",
            name=timeZone,
            hoverinfo="text",
        ))

    layout = Layout(
                    title=title,
                    autosize=True,
                    hovermode='closest',
                    mapbox=dict(accesstoken=mapbox_access_token,
                                bearing=0,
                                pitch=0, zoom=1),
                    )

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename=fileName)


