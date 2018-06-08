# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

plotlyJsFilePath = './plotly.js'

def plot(data, layout, fileName='html/plot.html'):
    # 画图模板字符串
    template = '''
<html>
<head>
    <meta charset="utf-8" />
</head>
<body>
    <script src="{plotlyJsFilePath}"></script>
'''.format(plotlyJsFilePath=plotlyJsFilePath) \
               + '''    <div id="chartId" style="height: 100%; width: 100%;" class="plotly-graph-div"></div>
    <script type="text/javascript">
''' \
               + '''    var data = {data},
'''.format(data=data) \
               + '''    layout = {layout};
'''.format(layout=layout) \
               + '''    window.PLOTLYENV = window.PLOTLYENV || {};
    window.PLOTLYENV.BASE_URL = "https://plot.ly";
    Plotly.newPlot("chartId", data, layout, { "showLink": false, "linkText": "Export to plot.ly" })
    </script>
    <script type="text/javascript">
    window.addEventListener("resize", function() { Plotly.Plots.resize(document.getElementById("chartId")); });
    </script>
</body>
</html>
'''
    # python True False 转换成 js的true false
    template = template.replace('True', 'true').replace('False', 'false')
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(template)

if __name__ == '__main__':
    # plot()
    pass