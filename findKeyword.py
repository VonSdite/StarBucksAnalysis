import pandas as pd
import jieba
from calcDistance import calcDistance
import difflib
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def findkw(csv_file, Keyword, k, longitude, latitude):
    csv_file = csv_file.fillna("")
    csv_file['kw'] = "Store Number: " + csv_file["Store Number"] + " " \
                       + "Store Name: " + csv_file["Store Name"] + " " \
                       + "Street Address: " + csv_file["Street Address"] + " " \
                       + "Postcode: " + csv_file["Postcode"] + " " \
                       + "Phone Number: " + csv_file["Phone Number"] + " " \
                       + "Timezone:" + csv_file['Timezone'] + " "

    ratio = [""]*25600
    csv_file.insert(0, 'ratio', ratio)

    i = 0
    for w in csv_file['kw']:
        csv_file['ratio'][i] = difflib.SequenceMatcher(None, Keyword, w).quick_ratio()
        i += 1

    csv_file = csv_file.sort_values(by='ratio', ascending=False)
    print(csv_file)

    #选取k前后相似度相同的行，计算距离排序
    k = int(k)
    j = k
    while j-1 >= 0 and csv_file['ratio'][j] == csv_file['ratio'][j-1]:
        j -= 1

    x = k
    while csv_file['ratio'][x] == csv_file['ratio'][x + 1]:
        x += 1

    kfile = csv_file.head(j)

    if j == x:
        return kfile

    jkfile = csv_file.iloc[j:x]
    jkfile['Distance'] = jkfile.apply(
        lambda a:calcDistance(longitude, latitude, a.Longitude, a.Latitude),axis=1)
    jkfile.sort_values(by=['Distance'])
    jkfile = jkfile.head(k-j)

    kfile.apply(jkfile)

    return kfile

