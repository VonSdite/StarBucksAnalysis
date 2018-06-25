# -*- coding: utf-8 -*-
# __Author__: Sdite, amyy4, JX-Soleil, hzgege
# __Email__ : a122691411@gmail.com

import pickle
from findTopK import findTopK, findTopKWithKeyWord
from findRange import findRange
from plot import plot

mapbox_access_token = 'pk.eyJ1Ijoic2RpdGUiLCJhIjoiY2pmajloaWJxMGw2NjJ4dW1za2c2cDNkZiJ9.KNk-JYP0chw-NFPffGs0eg'

# 店铺是否有评分
def hasScore(score):
    if score == 0:
        return '暂无评分'
    else:
        return str(score) + '分'

# 店铺评分次数
def scoreNum(score):
    if len(score) == 0:
        return '0次'
    else:
        return str(len(score.strip().split(' '))) + '次'

# int转字符
def intToStr(num):
    if num == 'Not set':
        return ''
    return str(num)

# 字符转int
def strToInt(string):
    return int(string)

def drawBar(data, fileName="html/bar.html", title=''):
    dataDict = dict(data.value_counts())
    dataName = [key for key in dataDict]
    dataValues = [dataDict[key] for key in dataDict]

    data = [
        dict(
            type="bar",
            x=dataName,
            y=dataValues
        )
    ]
    layout = dict(title=title)

    plot(data, layout, fileName=fileName)

def drawPie(data, fileName="html/pie.html", title=''):
    dataDict = dict(data.value_counts())
    dataName = [key for key in dataDict]
    dataValues = [dataDict[key] for key in dataDict]

    data = [
        dict(
            type="pie",
            labels=dataName,
            values=dataValues,
            hoverinfo='label+percent',
            textinfo='none'
        )
    ]
    layout = dict(title=title)

    plot(data, layout, fileName=fileName)

def drawLineChart(data, fileName='html/line.html'):
    trace = []
    for info in data:
        trace.append(
            dict(
                type="scatter",
                y=info[0],  # info[0]时延耗时
                x=info[1],  # k或r值大小
                name=info[2],  # 哪种查询
                mode='lines+markers',
                showlegend=True
            )
        )

    layout = dict(
        title='时延图',
    )

    plot(trace, layout, fileName=fileName)

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

    layout = dict(
        title=title,
        autosize=True,
        hovermode=True,
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0,
            zoom=1
        )
    )

    plot(data, layout, fileName=fileName)

def drawMap(csv_file, fileName="html/map.html", title=''):
    timeZoneDict = dict(csv_file['Timezone'].value_counts())

    def timeZoneToCount(timeZone):
        return timeZoneDict[timeZone]

    csv_file['TimeZoneCount'] = csv_file['Timezone'].map(timeZoneToCount)

    csv_file = csv_file.fillna('Not set')

    csv_file['info'] = "Store Number: " + csv_file["Store Number"] + "</br></br>" \
                       + "Store Name: " + csv_file["Store Name"] + "</br>" \
                       + "Street Address: " + csv_file["Street Address"] + "</br>" \
                       + "Postcode: " + csv_file["Postcode"] + "</br>" \
                       + "Phone Number: " + csv_file["Phone Number"] + "</br>" \
                       + "Timezone: " + csv_file['Timezone'] + "</br>" \
                       + "Number of stores: " + csv_file['TimeZoneCount'].map(
        intToStr) + "</br>" \
                       + '平均评分: ' + csv_file['AvgScore'].map(hasScore) + "</br>" \
                       + '评分次数: ' + csv_file['Score'].map(scoreNum)

    data = [
        dict(
            type='scattermapbox',
            lat=list(csv_file['Latitude']),
            lon=list(csv_file['Longitude']),
            mode='markers',
            marker=dict(
                size=10,
                color=list(csv_file['TimeZoneCount']),
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
            text=list(csv_file['info']),
            textposition='top left',
            hoverinfo='text',
        ),
    ]

    layout = dict(
        title=title,
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0, zoom=1),
    )

    plot(
        data,
        layout,
        list(csv_file['Id'].map(strToInt)),
        list(csv_file['Score'].map(intToStr)),
        fileName
    )

def drawTopKMap(csv_file, lon, lat, topK, keyWord, data, fileName="html/topKMap.html",
                title=''):
    if keyWord == "":
        topKInfo = findTopK(csv_file, lon, lat, topK)
    else:
        topKInfo = findTopKWithKeyWord(csv_file, lon, lat, topK, keyWord, data)

    topKInfo = topKInfo.fillna('Not set')  # 将空值设为Not set
    topKInfo['info'] = "Store Number: " + topKInfo["Store Number"] + "</br></br>" \
                       + "Store Name: " + topKInfo["Store Name"] + "</br>" \
                       + "Street Address: " + topKInfo["Street Address"] + "</br>" \
                       + "Postcode: " + topKInfo["Postcode"] + "</br>" \
                       + "Phone Number: " + topKInfo["Phone Number"] + "</br>" \
                       + "Timezone: " + topKInfo['Timezone'] + "</br>" \
                       + '平均评分: ' + topKInfo['AvgScore'].map(hasScore) + "</br>" \
                       + '评分次数: ' + topKInfo['Score'].map(scoreNum)

    data = [
        dict(
            type='scattermapbox',
            lat=list(topKInfo['Latitude']),
            lon=list(topKInfo['Longitude']),
            mode='markers',
            marker=dict(
                size=10,
                color='blue'
            ),
            text=list(topKInfo['info']),
            textposition='top left',
            hoverinfo='text',
            name="topK点",
        ),
        dict(
            type='scattermapbox',
            lat=[lat],
            lon=[lon],
            mode='markers',
            marker=dict(
                size=10,
                color='red'
            ),
            text=["标记点</br></br>经度:%f  纬度: %f" % (lon, lat)],
            textposition='top left',
            hoverinfo='text',
            name="标记点",
        )
    ]

    layout = dict(
        title=title,
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            center=dict(
                lat=lat,
                lon=lon
            ),
            bearing=0,
            pitch=0,
            zoom=1
        ),
    )
    plot(
        data,
        layout,
        list(topKInfo['Id'].map(strToInt)),
        list(topKInfo['Score'].map(intToStr)),
        fileName
    )

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
                        + "Timezone: " + rangeInfo['Timezone'] + "</br>" \
                        + "Distance: " + rangeInfo["Distance"] + "</br>" \
                        + '平均评分: ' + rangeInfo['AvgScore'].map(hasScore) + "</br>" \
                        + '评分次数: ' + rangeInfo['Score'].map(scoreNum)

    data = [
        dict(
            type='scattermapbox',
            lat=list(rangeInfo['Latitude']),
            lon=list(rangeInfo['Longitude']),
            mode='markers',
            marker=dict(
                size=10,
                color='blue'
            ),
            text=list(rangeInfo['info']),
            textposition='top left',
            hoverinfo='text',
            name="距离标记点 <= range的点",
        ),
        dict(
            type='scattermapbox',
            lat=[lat],
            lon=[lon],
            mode='markers',
            marker=dict(
                size=10,
                color='red'
            ),
            text=["标记点</br></br>经度:%f  纬度: %f 半径: %f" % (lon, lat, range)],
            textposition='top left',
            hoverinfo='text',
            name="标记点",
        )
    ]

    layout = dict(
        title=title,
        showlegend=True,
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            center=dict(
                lat=lat,
                lon=lon
            ),
            bearing=0,
            pitch=0, zoom=1),
    )

    plot(
        data,
        layout,
        list(rangeInfo['Id'].map(strToInt)),
        list(rangeInfo['Score'].map(intToStr)),
        fileName
    )

