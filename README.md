# StarBucksAnalysis
星巴克数据分析

## Iteration 5
星巴克数据分析工具 需求5

- 显示店铺信息
    + 用户点击查询到的店铺，弹出对话框显示店铺信息（包括店铺基本信息和评价信息）
    
- 对店铺进行评分
    + 用户可以对所选择的店铺进行评分，下次查询时展示该评分
    
- 计算店铺平均评分
    + 若某店铺被多次输入评分，将所有评分进行记录，并计算其平均分
    
- 特殊标明高分店铺
    + 若某店铺平均评分高于8分，则在top-k、range、top-k+关键词的查询结果里用特殊记号标明

- 完善功能+重构
    + 之前迭代中可能存在了很多遗留问题没有解决，在本轮迭代中解决它们

- 将整个项目打包成一个exe文件
    + 无需安装环境就可以执行
    

### 小组的计划

#### 用户故事、排序、相关的估计
- 用户故事及估算

    + 点击显示店铺信息 -> (**3人/天, 3点**)

    ![用户故事](README_IMG/iteration5_story1.png)
    
    + 对店铺进行评分 -> (**7人/天, 7点**)

    ![用户故事](README_IMG/iteration5_story2.png)
    
    + 计算店铺平均分 -> (**2人/天, 2点**)

    ![用户故事](README_IMG/iteration5_story3.png)
    
    + 特殊标明高分店铺 -> (**3人/天, 3点**)

    ![用户故事](README_IMG/iteration5_story4.png)

    + 完善功能+重构 -> (**7人/天, 7点**)

    ![用户故事](README_IMG/iteration5_story5.png)

    + 将整个项目打包成一个exe文件 -> (**3人/天, 3点**)

    ![用户故事](README_IMG/iteration5_story6.png)
          
    
 - 排序
    + **优先级1**： 点击显示店铺信息
    + **优先级2**： 对店铺进行评分
    + **优先级3**： 计算店铺平均分
    + **优先级4**： 特殊标明高分店铺
    + **优先级5**： 完善功能+重构
    + **优先级6**： 将整个项目打包成一个exe文件
    
    
### 小组的速度

- 第四次迭代所有用户故事均完成，开发速度为 3+7+2+3+7+3=**25点**
- 第三次迭代所有用户故事均完成，开发速度为 1+3+7+1+7+3+2=**24点**
- 第二次迭代开发速度为 **25点**
- 小组的平均开发速度 **25点**

### 第五次迭代功能展示

#### 1. 点击店铺，能进行店铺的评分(即时变化)

- 点击店铺前，鼠标指向的店铺点会展示该店铺的信息
- 若该店铺没被评分过，会显示**暂无评分** 和 **评分次数0次**

![](README_IMG/iteration5_0.png)

- 点击店铺点， 会显示该店铺的信息， 并有一个**下拉框**可以进行评分

![](README_IMG/iteration5_1.png)

- 下拉框的取值为 **0-10分**
- 下拉框默认选中**8分**

![](README_IMG/iteration5_2.png)

#### 2. 店铺平均分计算，高于8分用紫色点标注(即时变化)

- 多次评分， 点会显示 **平均分** 和 **评分次数**
- 评分**高于8分**， 会用紫色标注出来

![](README_IMG/iteration5_3.png)

- 若有**高于8分**的店铺， **右侧**图例会显示出来
- 并可以通过**点击**图例来隐藏掉相应的点

![](README_IMG/iteration5_4.png)

![](README_IMG/iteration5_5.png)

#### 3. 下次查询评分会被记录

- 程序关闭时， 会将所有本次运行的**历史评分记录到csv中**
- 下图中 `AvgScore`是平均分， `Score`是评分历史记录

![](README_IMG/iteration5_6.png)

#### 4. 打包成.exe

![](README_IMG/iteration5_7.png)

#### 5. 完善功能+重构

- 由于之前迭代的功能基本实现， 所以功能完善所做的事情较少
- 代码目录结构
    + `config`目录 -> 保存着相应的配置文件， 如jquery, plotly.js等
    + `historyIteration`目录 -> 保存着历史迭代记录
    + `html`目录 -> 保存程序生成的html
    + `image`目录 -> 保存着程序所需要用到图片资源文件
    + `README_IMG`目录 -> 保存着`README.md`的图片
    + `Test`目录 -> 保存着相应的**测试文件**
    + `calcDistance.py` -> 计算两个经纬度点间距离
    + `calcRelative.py` -> 计算关键词和数据项的相关性
    + `directory.csv` -> 数据集
    + `draw.py` -> 相关的绘图函数
    + `drawThread.py` -> 绘图函数调用的线程类(属于helper类)
    + `findRange.py` -> 找出range范围内的数据项
    + `findTopK.py` -> 找出距离最近的topK 或 与关键词相关性最大的数据项
    + `main.py` -> 主程序
    + `plot.py` -> 自己封装plotly.js的绘制地图库的接口函数
    + `pythonJsInteractObject.py` -> 实现python 与 js 交互的类
    + `ui.py` -> 界面类
    + `README.md` -> 介绍文档

![](README_IMG/iteration5_8.png)

### 总结

- *本次迭代遇到**较多**的问题*

#### 店铺在地图上点的点击事件响应

- **问题1:** 店铺点击响应
    + 由于地图的绘制使用的是 第三方库 `plotly`， 该库python版**没有**相应的绑定事件的接口(因为python只能利用接口进行绘制html，交互实际上是在网页上)
    + 而通过**观察**生成的html， 实际生成的html都是有`plotly.js`来实现的
    + 也就是说python的plotly库仅仅是靠封装`plotly.js`来实现的
    + 所以方向变成了使用**js**来实现点击响应
    + 解决思路： 自己使用python**封装** plotly.js， 并封装上相应的js代码响应即可

- **问题2:** 店铺评分即时显示和计算
    + 因为评分是在网页上实现的，评分的数据是在网页上的
    + 要完成店铺评分即时显示仍然只能从**js**下手
    + 每次计算完平均分还需要重绘地图(因为地图hoverInfo的数据已经被写入到html中，需要重绘才能显示)

- **问题3:** 由于店铺评分即时显示，高于8分店铺也需要即时特殊标注
    + 本来高于8分的店铺的标注想用别的形状来标注
    + 但是官方文档却表明别的形状标注不受设置的颜色和大小影响
    + 不好控制， 所以选择**紫色**作为特殊标注的颜色
    + 当然问题不仅再此， 要实现实时改变颜色
    + 需要使用两个数组来维护
    + 一个维护着低于8分的数据， 一个维护着高于8分的数据
    + 低于8分的数据在一次评分中若平均分高于8分，需要移至高于8分的数组
    + 高于8分的数据在一次评分中若平均分低于8分，需要移至低于8分的数组

![](README_IMG/iteration5_9.png)

- **问题4:** python与js数据交互
    + 由于数据应回传给python
    + 然后最终由python来保存数据
    + 这就需要在python和Js之间建立一个**channel**通道来实现数据的交互

#### 打包exe程序或者源代码在不同电脑上的差异

- 部分电脑可以运行源代码以及exe
- 但是有一部分电脑**却不能运行**(配置， 代码， 操作系统一致)
- (问题出现在了自己宿舍中， 宿舍4人， 2人能运行， 2人不能运行)

#### 代码重构

- 本次迭代并没有对代码深入重构， 但由于之前良好的编码习惯， 使代码冗余度小， 灵活扩展，便于维护， 虽然并未使用过多的**设计模式**
- 后续仍需进行重构以及对之前的geoHash算法进行研究

---

## Iteration 4
星巴克数据分析工具 需求4

- 显示查询执行的进度条：
    + 如果查询执行较慢，则需要显示查询执行的进度条

- 距离range查询：
    + 用户输入经纬度和一个参数r，展示这个经纬度半径r内的所有星巴克
    + 具体要求：
        1. 直接根据经纬度计算距离即可，无需考虑建筑物、道路等因素的影响
        2. 如果用户输入的经纬度不合法，需要提示用户。
        3. 对用户的每一次输入，展示查询时延（即从查询发出，到结果返回所需要的时间）

- 关键字+距离top-k查询:
    + 用户输入经纬度，一个参数k以及一个关键词key
    + 具体要求：
        1. 关键词的相关度根据fuzzywuzzy库来实现
        2. 如果用户输入的经纬度不合法，需要提示用户。
        3. 对用户的每一次输入，展示查询时延（即从查询发出，到结果返回所需要的时间）
    

### 小组的计划

#### 用户故事、排序、相关的估计
- 用户故事及估算
    
    + 查询时显示进度 -> (**2人/天, 2点**)

    ![用户故事](README_IMG/iter4_story1.png)

    + 在地图展示range-r店铺 -> (**1人/周, 7点**)
    
    ![用户故事](README_IMG/iter4_story2.png)
    
    + 设计关键词相似度算法 -> (**1人/周, 7点**)
    
    ![用户故事](README_IMG/iter4_story3.png)
    
    + Topk+关键词搜索 -> (**1人/周, 7点**)
    
    ![用户故事](README_IMG/iter4_story4.png)
    
    + 查询时延显示 -> (**3人/天, 3点**)
    
    ![用户故事](README_IMG/iter4_story5.png)

- 排序
    + **优先级1**： 查询时显示进度
    + **优先级2**： 在地图展示range-r店铺
    + **优先级3**： 设计关键词相关度算法
    + **优先级4**： Topk+关键词搜索 
    + **优先级5**： 查询时延显示

### 小组的速度

- 第四次迭代所有用户故事均完成，开发速度为 2+7+7+7+3=**26点**
- 第三次迭代所有用户故事均完成，开发速度为 1+3+7+1+7+3+2=**24点**
- 第二次迭代开发速度为 **25点**
- 小组的平均开发速度 **25点**

#### 软件介绍

- **软件主体窗口**

    ![软件主体窗口](README_IMG/iter4_mainWindow.png)

---

- **软件窗体扩展**
    
    ![extension](README_IMG/extension.png)

---

- **查询加载时loading**
    ![loading](README_IMG/loading.png)

---

- **菜单栏打开文件**
    
    + 用于打开csv文件

    + 快捷键为Ctrl+O

    ![菜单栏打开文件](README_IMG/iter4_openFile.png)

---

- **RANGE**
    
    + 用户输入经纬度，以及一个参数r

    + 显示以此经纬度为圆心的，半径为r范围的星巴克

    ![RANGE](README_IMG/iter4_range.png)

    ![RANGE](README_IMG/iter4_range1.png)

---

- **关键词+top-k**
    
    + 用户输入经纬度和一个参数k以及关键词key

    + 显示相似度最高以及最近的k个商铺

    ![关键词+top-k查询](README_IMG/iter4_keyTop-k.png)

    ![关键词+top-k查询](README_IMG/iter4_keyTop-k1.png)

- **查询时延显示**
    
    ![时延](README_IMG/showtime.png)

    ![时延](README_IMG/showtime1.png)

- **输入检查**
    
    ![检查](README_IMG/lacklon.png)
    ![检查](README_IMG/lacklat.png)
    ![检查](README_IMG/lackrange.png)
    ![检查](README_IMG/lackk.png)
    ![检查](README_IMG/errorlon.png)
    ![检查](README_IMG/errorlat.png)

#### iter4 总结

##### 1.topk算法验证

- 验证pandas的nsmallest， quicksort， heapsort， mergesort
    
    + pandas 官网标注nsmallest比使用quicksort等排序快

    ![fast](README_IMG/faster.png)

+ **验证如下 **

+ 总体来看nsmallest确实比较快， quicksort有突然的高峰，表明quicksort的不稳定性
+ 且随着k值增大，耗时是有逐步变大的趋势
+ **nsmallest** 平均时延约为 **2ms**
+ **mergesort** 平均时延约为 **4ms**
+ **quicksort** 平均时延约为 **4ms**
+ **heapsort** 平均时延约为 **5ms**
+ 
    ![compare](README_IMG/compare0.png)

+ nsmallest 与 quciksort， 取k值属于1w-1w8来看，nsmallest确实比quicksort快
+ 原因可能是nsmallest内部有进行优化，或者使用了大顶堆算法

    ![compare](README_IMG/compare1.png)

+ 由图可知nsmallest 优于 mergesort 优于 heapsort

    ![compare](README_IMG/compare2.png)
    
##### 2.geohash

+ 由于使用pandas自带的nsmallest方法效率足够快，并未使用geohash方法
+ 并且geohash仅是对经纬度哈希，虽然能减少topK距离筛选的数量，但不能用于关键字搜索

##### 3.关键词搜索

+ 本轮迭代的关键词搜索是使用**fuzzywuzzy库**的模糊匹配来实现的，并不涉及到关键词语义的分析
+ 例如**‘美国’** 与 **‘加利福利亚’** 实际是有关联度的，但fuzzywuzzy不能做到**语义分析**
+ 尝试使用**百度api**进行短文本语义分析得出相似度，但是处理**2w条数据**一次需要**35.5分钟**，最终放弃语义分析

##### 4.range-r搜索

+ 给定经纬度找出以该**经纬度为圆心半径**为**r**的所有星巴克店铺
+ 虽然能找出星巴克店铺，但在**可视化**的时候无法画出该经纬度为圆心半径为r的**圆**，导致**观感不够直接**
+ 该问题实现有**一定困难性**，因为地图生成使用的是第三方库**plotly**，该库没有提供相应的接口，小组**暂未有能力实现**

##### 5.测试驱动开发

+ 通过写ui扩展窗体样例，实现原本ui界面的扩展窗体
+ 通过编写部分样例，来考察关键字相似度算法的可靠性



## Iteration 3

星巴克数据分析工具 需求3

- 不同时区店铺数量渐变图：

    + 是第2轮迭代中“在将属于不同时区的店铺用不同颜色的点显示”的修改版

    + 用渐变色标识每个时区的店铺数量

    + 举例：店铺数量多的时区中的点用深红色、数量中等用正红色、数量少用浅红色

- 距离top-k查询：
    + 用户输入经纬度和一个参数k，展示距离其最近的k个星巴克

    + 具体要求：
        1. 直接根据经纬度计算距离即可，无需考虑建筑物、道路等因素的影响
        2. 如果用户输入的经纬度不合法，需要提示用户。
        3. 对用户的每一次输入，展示查询时延（即从查询发出，到结果返回所需要的时间）
        4. 用户输入经纬度，可视化展示随着k的增长查询时延的变化


### 小组的计划

#### 用户故事、排序、相关的估计

- 用户故事及估算
    + 统计每个时区的店铺数量 -> (**1人/天, 1点**)

    ![用户故事](README_IMG/iter3_story1.png)

    + 渐变色标识每个时区的店铺数量 -> (**3人/天, 3点**)

    ![用户故事](README_IMG/iter3_story2.png)

    + 距离top-k查询界面以及接口设置 -> (**1人/周, 7点**)

    ![用户故事](README_IMG/iter3_story3.png)

    + 设计经纬度计算距离算法 -> (**1人/天, 1点**)

    ![用户故事](README_IMG/iter3_story4.png)

    + 设计获取top-K的店铺信息算法 -> (**1人/周, 7点**)
    
    ![用户故事](README_IMG/iter3_story5.png)

    + 在地图展示top-K店铺，并显示时延 -> (**3人/天, 3点**)

    ![用户故事](README_IMG/iter3_story6.png)

    + 可视化展示随着k的增长查询时延的变化 -> (**2人/天，2点**)

    ![用户故事](README_IMG/iter3_story7.png)

- 排序
    + **优先级1**： 统计每个时区的店铺数量
    + **优先级2**： 渐变色标识每个时区的店铺数量
    + **优先级3**： 设计经纬度计算距离算法
    + **优先级4**： 距离top-k查询界面以及接口设置
    + **优先级5**： 设计获取top-K的店铺信息算法
    + **优先级6**： 在地图展示top-K店铺，并显示时延
    + **优先级7**： 可视化展示随着k的增长查询时延的变化

#### 小组的速度

- 第三次迭代所有用户故事均完成，开发速度为 1+3+7+1+7+3+2=**24点**
- 第二次迭代开发速度为 **25点**
- 小组的平均开发速度 **24.5点**

#### 软件介绍

- **软件主体窗口**

![软件主体窗口](README_IMG/iter3_mainWindow.png)

---

- **菜单栏打开文件**
    
    + 用于打开csv文件

    + 快捷键为Ctrl+O

![菜单栏打开文件](README_IMG/iter3_openFile.png)

---

- **星巴克时区店铺数量渐变色世界分布图**
    
    + 该图显示了星巴克店铺在全球**不同时区的数量**渐变分布

    + 时区中星巴克店铺**数量越多**，点的颜色**越深**；店铺数量**越少**，点的颜色**越浅**

    + 鼠标指向某一个星巴克店铺时，会显示该店铺的详细信息，包括编号、名称、地址、邮编、电话

![店铺世界分布图](README_IMG/iter3_map.png)

![店铺世界分布图](README_IMG/iter3_map2.png)

---

- **星巴克店铺国家区域分布密度渐变图**
    
    + 该图显示了星巴克在不同国家分布的密度情况

    + 区域颜色越红，说明该区域星巴克店铺数量越多

    + 区域颜色为纯白色时，表明该区域无星巴克店铺

![星巴克店铺国家区域分布密度渐变图](README_IMG/colorMap.png)

---

- **用户输入经纬度和一个参数k，展示距离其最近的k个星巴克**

    + 用户输入一个点的**经纬度**，以及参数**k**

    + 地图显示距离该点最近的**k个星巴克**

![用户输入经纬度和一个参数k，展示距离其最近的k个星巴克](README_IMG/iter3_topK.png)

---

- **数据统计并可视化**

    + 在迭代1中，已经做了较为详尽的数据分析

    + 按本次需求，仅做了星巴克店铺时区分布和国家分布的柱状图和饼图

    + 由时区柱状图和饼图可知，时区GMT-05:00 America/New_York出现次数最多，且星巴克主要分布在美国时区中

    + 由国家分布柱状图和饼图可知， 星巴克店铺也是主要分布在美国

![星巴克时区店铺柱状图](README_IMG/timezoneBar.png)

![星巴克时区店铺饼图](README_IMG/timezonePie.png)

![星巴克国家店铺柱状图](README_IMG/countryBar.png)

![星巴克国家店铺饼图](README_IMG/countryPie.png)

#### 开发过程总结

##### 关于时区问题的探讨
- 上网搜索了下GMT与UTC的区别
- 发现GMT其实与UTC是几乎是同一种概念，只是GMT是基于地球的自转和公转来计算时间，UTC是基于原子钟来计算时间的
- 而且我们数据中的GMT数据只是details数据，可以去掉
![UTC与GMT](README_IMG/UTCGMT.png)

![GMTDetails](README_IMG/GMT_Details.png)

- 但是对数据进行清洗去除后缀后，发现如下情况

![去掉后缀](README_IMG/时区数据去后缀.png)

- 发现数据里面相同时区却是不同的字符串来表示，同时还存在着时区GMT+5:30等数据
- 所以我们放弃了去掉GMT数据后缀来划分时区，转向用经纬度换算时区的方式，绘制出如下图
![24UTC](README_IMG/24UTC.png)
- 与不去除后缀的时区渐变图相差不大， 但**保留后缀的时区渐变图**带有**国家信息**，分布更加**详细**，所以选择使用带有后缀的时区进行绘图

---

##### 对top-k算法的分析
***注: 可能因计算机环境不同，耗时不同***

- 快速选择算法 平均时间复杂度 O(n), 最坏情况为O(n^2)

- 大顶堆求前k小值 时间复杂度 O(nlogk)

- pandas自带.nsmallest()函数

- 注： 还可使用geohash算法，本次迭代没有使用

![时间耗时](README_IMG/时间耗时.png)

![pandas与heap](README_IMG/heapq_pandas.png)
![pandas与quickSelect](README_IMG/quickSelect_pandas.png)


- 由图可知
    + 一次遍历计算一个点与两万个点间距离的时间耗时大约是**1s**

    + 大顶堆的时间大部分在将近**20ms**处， 快速选择大部分在将近**50ms**处， pandas自带.nsmallest()函数时间在**1ms-5ms**左右

    + 快速选择最初在**k值较小**时，用时**比较少**，而且从图中可以看到有较多的**高峰**出现，显然该选择确实是个**不稳定**的算法

    + 大顶堆的时间**比较稳定**，用时相对来说比较少

    + pandas自带的函数**用时少**，且也很**稳定**

    + 因此我们topK的获取算法使用 pandas自带.nsmallest()

- 测试代码如下: 
```python
# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import time
import heapq
import pandas as pd
from math import radians, atan, tan, sin, cos, acos

import plotly.offline as py
from plotly.graph_objs import *


ra = 6378.140  # 赤道半径 (km)
rb = 6356.755  # 极半径 (km)
flatten = (ra - rb) / ra  # 地球扁率
def calcDistance(lon_a, lat_a, lon_b, lat_b):
    rad_lat_A = radians(lat_a)
    rad_lng_A = radians(lon_a)
    rad_lat_B = radians(lat_b)
    rad_lng_B = radians(lon_b)
    pA = atan(rb / ra * tan(rad_lat_A))
    pB = atan(rb / ra * tan(rad_lat_B))
    xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
    c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
    c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (xx + dr)
    return distance

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
    csv_file = pd.read_csv("directory.csv")

    start = time.clock()
    distance = csv_file.apply(
        lambda x:calcDistance(0, 0, x.Longitude, x.Latitude),
                              axis=1)
    end = time.clock()

    print('遍历计算点间距离时间: %fs' % (end - start))

    useTime = dict()
    useTime['heap'] = []
    useTime['qSelect'] = []
    useTime['pandas'] = []

    for k in range(1, 25601):
        start = time.clock()
        topKHeap(distance, k)
        end = time.clock()
        h = end - start
        useTime['heap'].append(h)


        start = time.clock()
        qSelect(list(distance), k)
        end = time.clock()
        q = end - start
        useTime['qSelect'].append(q)


        start = time.clock()
        distance.nsmallest(k)
        end = time.clock()
        n = end - start
        useTime['pandas'].append(n)

        print("k: %d 大顶堆: %.15fs  快速选择: %.15fs  pandas: %.15fs" % (k, h, q, n))

    import pickle
    with open('config/tmp.pickle', 'wb') as f:
        pickle.dump(useTime, f)

    # with open('config/tmp.pickle', 'rb') as f:
    #     useTime = pickle.load(f)
    #
    # trace1 = Bar(
    #     y=useTime['heap'],
    #     x=list(range(1, 25601)),
    #     name='大顶堆'
    # )
    # trace2 = Bar(
    #     y=useTime['qSelect'],
    #     x=list(range(1, 25601)),
    #     name='快速选择'
    # )
    # trace3 = Bar(
    #     y=useTime['pandas'],
    #     x=list(range(1, 25601)),
    #     name='pandas'
    # )
    # data = [trace1, trace2, trace3]
    # layout = Layout(
    #     barmode='group'
    # )
    # fig = Figure(data=data, layout=layout)
    # py.plot(fig, filename='html/时间比较.html')

```

##### 测试驱动相关

- 编写findTopK函数的测试:
![findTopK函数测试](README_IMG/findTopK函数测试.png)
![findTopK函数测试结果](README_IMG/resultToFindTopK.png)


---

## Iteration 2
星巴克数据的分析工具 需求2

- 在世界地图上显示所有店铺的位置
    + 当选中某个店铺时，可以看到店铺的详细信息，如编号、名称、地址、邮编、电话等

- 将属于不同时区的店铺用不同颜色的点显示，统计每个时区中店铺的数量或密度，并可视化的展示统计结果

- 根据国家和经纬度将地图划分成不同的区域，用渐变色标识每个区域店铺数量
    
    + 举例：区域涂为深红色表示店铺数量/密度最高、正红色表示表示店铺数量/密度中等、浅红色表示表示店铺数量/密度较低、白色表示该区域没有店铺

- 统计每个国家拥有店铺的数量/密度，并可视化地给出统计结果


### 小组的计划

#### 用户故事、排序、相关的估计

- 用户故事及估算
    + 世界地图显示所有店铺(Show Shops in Map) -> (**1人/周, 7点**)

    ![用户故事](README_IMG/story1.png)

    + 显示店铺详细信息(Show Shop's Details) -> (**2人/天, 2点**)

    ![用户故事](README_IMG/story2.png)

    + 不同时区店铺用不同颜色标记(Differ Shops by Timezone) -> (**1人/周, 7点**)

    ![用户故事](README_IMG/story3.png)

    + 统计可视化数量/密度(Statistics and Visualization) -> (**2人/天, 2点**)

    ![用户故事](README_IMG/story4.png)

    + 渐变色标识每个区域店铺颜色(Gradient Color Identifies Each Area Shops) -> (**1人/周, 7点**)
    
    ![用户故事](README_IMG/story5.png)

- 排序
    + **优先级1**： 统计可视化数量/密度
    + **优先级2**： 世界地图显示所有店铺
    + **优先级3**： 显示店铺详细信息
    + **优先级4**： 不同时区店铺用不同颜色标记
    + **优先级5**： 渐变色标识每个区域店铺颜色

#### 小组的速度

- 第二次迭代所有用户故事均完成，开发速度为**25点**


#### 软件介绍

- **软件主体窗口**

![软件主体窗口](README_IMG/mainWindow1.png)

![软件主体窗口](README_IMG/mainWindow2.png)


- **菜单栏打开文件**
    
    + 用于打开csv文件

    + 快捷键为Ctrl+O

![菜单栏打开文件](README_IMG/openFile.png)


- **星巴克店铺世界分布图**
    
    + 该图显示了星巴克店铺在全球分布情况

    + 不同时区的星巴克店铺用不同的颜色标记

    + 鼠标指向某一个星巴克店铺时，会显示该店铺的详细信息，包括编号、名称、地址、邮编、电话

![店铺世界分布图](README_IMG/map.png)

![店铺世界分布图](README_IMG/map2.png)


- **星巴克店铺国家区域分布密度渐变图**
    
    + 该图显示了星巴克在不同国家分布的密度情况

    + 区域颜色越红，说明该区域星巴克店铺数量越多

    + 区域颜色为纯白色时，表明该区域无星巴克店铺

![星巴克店铺国家区域分布密度渐变图](README_IMG/colorMap.png)

- **数据统计并可视化**

    + 在迭代1中，已经做了较为详尽的数据分析

    + 按本次需求，仅做了星巴克店铺时区分布和国家分布的柱状图和饼图

    + 由时区柱状图和饼图可知，时区GMT-05:00 America/New_York出现次数最多，且星巴克主要分布在美国时区中

    + 由国家分布柱状图和饼图可知， 星巴克店铺也是主要分布在美国

![星巴克时区店铺柱状图](README_IMG/timezoneBar.png)

![星巴克时区店铺饼图](README_IMG/timezonePie.png)

![星巴克国家店铺柱状图](README_IMG/countryBar.png)

![星巴克国家店铺饼图](README_IMG/countryPie.png)


#### 开发过程总结

- Iteration1 与 Iteration2的不同

    + 迭代1过程中
        + 用户需求较为模糊，偏向于先对数据进行统计分析

    + 迭代2过程中
        + 用户提出较为详细的需求，使得开发的方向较为明确
        + 根据用户的需求，分析可知迭代1中所需要使用的工具还需要加入plotly库
        + 本次过程，大致估算出小组的开发速度

- 测试驱动的开发
    - 本次开发虽没有使用测试驱动开发，但是还是做了一定的了解

>单元测试语法
>
>进行单元测试时，使用到的Python方法如下：
>
>assert: 编写个人声明的基本方式
>
>assertEqual(a,b):检查a和b的是否等价
>
>assertNotEqual(a,b):检查a和b的是否非等价
>
>assertIn(a,b):检查是否存在b中
>
>assertNotIn(a,b): 检查是否不存在b中
>
>assertFalse(a):检查a的值是否为False
>
>assertTrue(a):检查a的值是否为Ture
>
>assertIsInstance(a,TYPE):检查a是否为“TYPE”类型
>
>assertRaises(ERROR,a,args):以参数args调用a时，检查是否会出现ERROR
>
---> 详情见 http://python.jobbole.com/81305/


---

## Iteration 1
 星巴克数据的分析工具 需求1

- 小组成员名单， 大致工作分配

- 数据集概述
    + 数据集包含哪些属性(列)
    + 表格中的值都代表什么
    + 可以从数据集中获取到哪些有用的信息

- 预期要使用（或要学习）的语言或工具

### 预期要使用（或要学习）的语言或工具

- 预计需要学习的语言
    + python
        + pandas库, numpy库(数据分析)
        + matplotlib库(图表绘制), basemap(绘制地图)
        + PyQt5库(界面编程)

- 工具
    + pycharm(python IDE)
    + excel


### 数据集概述
总共有25600个数据, 13个属性

- 数据集中的属性(列)
    - Brand(品牌)
        + 共有25600个品牌数据
        + 共有Starbucks, Teavana, Evolution Fresh, Coffee House Holdings 四种品牌
        + Starbucks             
            * 出现 25249次
            * 分布情况: US(13311次) CN(2734次) CA(1415次) JP(1237次) KR(993次) GB(英国,901次) MX(墨西哥, 579次) ... etc.
        + Teavana               
            * 出现 348次
            * 分布在US(294次), CA(53次), PR(波多黎各,1次)三个国家
            * 三个国家均在北美洲
        + Evolution Fresh       
            * 出现 2次
            * 均在US
        + Coffee House Holdings
            * 出现 1次
            * 仅出现在US

    - Store Number(店面编号)
        + 共有25600个数据, 其中有25599个不同店面店面编号数据
        + 其中19773-160973出现了2次，后发现是两条重复的数据，其中一条数据缺少了经纬度
        + 重复的数据为: 
            + Starbucks,19773-160973,Yoido IFC Mall - 1F,Joint Venture,"23 & 23-1, Yoido-Dong, Yongdongpo-Gu, 1F, #101",Seoul,11,KR,153-023,,GMT+09:00 Asia/Seoul,126.92,37.53

    - Store Name(店面名称)
        + 共有25600个数据, 其中有25364个不同的店面名称数据
        + 出现频率最高的店面名称是"Starbucks", 共出现224次
 
    - Ownership Type(所有权类型)
        + 共有25600个数据
        + 共有Licensed, Joint Venture, Company Owned, Franchise 四种类型
        + Licensed      出现 9375次
        + Joint Venture 出现 3976次
        + Company Owned 出现 11932次
        + Franchise     出现 317次

    - Street Address(街道地址)
        + 共有25598个街道地址数据, 其中有25353个不同的街道地址数据
        + 出现频率最高的街道地址为"Circular Building #6, Guard Post 8", 共出现11次
        + 缺少街道地址的数据为:
            + Starbucks,30997-103902,베네시티점,Joint Venture,,부산,26,KR,612-020,051-742-1655,GMT+09:00 Asia/Seoul,129.15,35.16
            + Starbucks,1329-152826,광주충장로점,Joint Venture,,광주,29,KR,501-013,062-224-8344,GMT+09:00 Asia/Seoul,126.91,35.15

    - City(城市)
        + 共有25585个城市数据, 其中有5469个不同的城市数据
        + 出现频率最高的城市是"上海市", 共出现542次

    - State/Province(州/省份)
        + 共有25600个数据, 其中有338个不同的州/省份数据
        + 出现频率最高的数据是"CA"(美国加利福利亚州), 共出现2821次

    - Country(国家)
        + 共有25600个数据, 其中有73个不同的国家数据
        + 出现频率最高的数据是"US"(美国), 共出现13608次

    - Postcode(邮政编码)
        + 共有24078个数据, 其中有18887个不同的邮政编码数据
        + 出现频率最高的邮政编码是"0", 共出现101次, 邮政编码为0无意义, 是无效数据

    - Phone Number(电话号码)
        + 共有18739个数据, 其中有18559个不同的电话号码数据
        + 出现频率最高的电话号码是"773-686-6180", 共出现17次

    - Timezone(时区)
        + 共有25600个数据, 其中有101个不同的时区数据
        + 出现频率最高的时区数据是"GMT-05:00 America/New_York", 共出现4889次

    - Longitude(经度)、Latitude(纬度)
        + 共有25599个数据
        
### 数据初步分析

#### 星巴克世界分布图
![星巴克世界分布图](README_IMG/starbucks_map.png)

- 从星巴克世界分布图可知，星巴克店铺主要分布在北美洲，欧洲，亚洲，且主要分布在沿岸地区

---

#### 星巴克Brand(品牌)属性分析

- 共有4种品牌, Starbucks, Teavana, Evolution Fresh, Coffee House Holdings 

![星巴克主要国家分布饼图](README_IMG/world_distribution.png)

- 从饼图可知，星巴克主要分布在美国，加拿大，中国，日本这四大国家
- 饼图中的others是星巴克出现所在国家次数<1000的集合

---

![星巴克Starbucks主要国家分布饼图](README_IMG/Starbucks_distribution.png)

- 从饼图可知，星巴克以Starbucks为名的店面主要分布在美国，中国，加拿大，日本这四大国家
- 饼图中的others是星巴克出现所在国家次数<1000的集合
- Starbucks（数据统计）             
    * 出现 25249次
    * 分布情况: US(13311次) CN(2734次) CA(1415次) JP(1237次) KR(993次) GB(英国,901次) MX(墨西哥, 579次) ... etc.

---

![星巴克Teavana国家分布饼图](README_IMG/Teavana_distribution.png)

- 从饼图可知，星巴克以Teavana为名的店面分布在美国，加拿大，波多黎各三个国家，主要是在美国
- Teavana               
    * 出现 348次
    * 分布在US(294次), CA(53次), PR(波多黎各,1次)三个国家
    * 三个国家均在北美洲

---

**其他品牌: **

- Evolution Fresh       
    * 出现 2次
    * 均在US
- Coffee House Holdings 
    * 出现 1次
    * 仅出现在US

#### 星巴克街道地址属性分析

![星巴克街道地址属性](README_IMG/街道地址出现3次以上.png)

- 从柱状图可知，Circular Building #6, Guard Post 8 出现了11次
- 且有34条街道出现次数在3次以上，表明该街道可能是一个人流密集，适合经营的地段
