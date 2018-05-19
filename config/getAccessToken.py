# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

# 忽略该文件， 调用api处理25600行进行语义分析需要35分钟

import requests

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=SzLZzbOslrD9I7XvHRdD7Z3Y&client_secret=KRonetLro6SYwD4znQ2XGc4wzGNvrNG3'

headers = {
    'Content-Type': 'application/json; charset=UTF-8',
}


def getAccessToken():
    res = requests.get(url=host, headers=headers)
    data = eval(res.text)
    return data['access_token']


if __name__ == '__main__':
    import pandas as pd
    csv_file = pd.read_csv("../directory.csv")
    # csv_file['Key'] = csv_file["Store Number"] + " " \
    #                    + csv_file["Store Name"] + " " \
    #                    + csv_file["Street Address"] + " " \
    #                    + csv_file["Postcode"] + " " \
    #                    + csv_file["Phone Number"] + " " \
    #                    +  csv_file['Timezone']
    # findTopKWithKeyWord(csv_file, 113, 23, 50, "广州")

    csv_file_tmp = csv_file.fillna("").astype(str)
    text2 = "美国"

    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet?charset=UTF-8&&access_token={access_token}'
    accessToken = getAccessToken()
    url = url.format(access_token=accessToken)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
    }

    session = requests.Session()
    import time, json

    start = time.clock()
    for index in range(len(csv_file_tmp)):
        text1 = " ".join(list(csv_file_tmp.iloc[index]))

        data = {
            "text_1": text1,
            "text_2": text2
        }

        data = json.dumps(data)
        res = session.post(url=url, headers=headers, data=data)
        print(res.text)

    end = time.clock()
    print(end - start)