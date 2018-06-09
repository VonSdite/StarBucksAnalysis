# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

def plot(data, layout, identify=[], score=[], fileName='html/plot.html'):
    # 画图模板字符串
    template = '''
<html>
<head>
    <meta charset="utf-8" />
</head>
<body>
    <script type="text/javascript" src="../config/qwebchannel.js"></script>  
    <script src="../config/plotly.js"></script>
    <div id="chartId" style="height: 100%; width: 100%;" class="plotly-graph-div"></div>
    <script type="text/javascript">
''' \
               + '''    var data = {data},
    identify = {id},
    scoreArr = {score},
    layout = {layout};
'''.format(data=data, id=identify, score=score, layout=layout) \
               + '''    window.PLOTLYENV = window.PLOTLYENV || {};
    window.PLOTLYENV.BASE_URL = "https://plot.ly";
    
    function set(myPlot) {
        Plotly.newPlot("chartId", data, layout, { "showLink": false, "linkText": "Export to plot.ly" });
        if (data[0].type == 'scattermapbox')
        {
            myPlot = document.getElementById('chartId');
            myPlot.on('plotly_click', function(d){
                    var point = d.points[0];
                    if (point.text.substr(0, 3) == '标记点') return;
    
                    var index = data[0].text.indexOf(d.points[0].text),
                        str = point.text.replace(new RegExp('</br></br>|</br>', 'gm'), '\\n'),
                        score = prompt(str + '\\n评分: ');
                    if (score > 10 || score < 0)
                    {
                        alert('请输入评分在0-10分间')
                    }
                    else if (score <= 10 && score >= 0 && score != null && score != "")
                    {
                        new QWebChannel(qt.webChannelTransport, function(channel)
                        {
                            //Get Qt interact object
                            var interactObj = channel.objects.interactObj;
                            interactObj.JSSendMessage(identify[index] + " "+ score);
                        });
                        scoreArr[index] = scoreArr[index] + score + ' ';
                        var scores = scoreArr[index].substr(0, scoreArr[index].length-1).split(' '),
                            sum = eval(scores.join('+')),
                            numOfScores = scores.length,
                            avgScore = sum / numOfScores;
                        data[0].text[index] =
                            data[0].text[index].replace(new RegExp('平均评分: .*?分</br>'), '平均评分: ' + avgScore + '分</br>');
                        data[0].text[index] =
                            data[0].text[index].replace(new RegExp('评分次数: .*?次'), '评分次数: '+ numOfScores + '次');
                        alert('评分成功!');
                        set(myPlot);
                    }
                }
            );
        }
    }
    var myPlot = document.getElementById('chartId');
    set(myPlot);
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